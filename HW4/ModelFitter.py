import numpy as np
from matplotlib import animation
from matplotlib.widgets import Button, Slider
import matplotlib.pyplot as plt
from Plotter import dataset, figret
import math
from scipy.stats import chisquare
class dataform:
    def __init__(self,data,min,max,lrate=None,name=None):
        self.data=data
        self.min=min
        self.max=max
        self.lrate=lrate
        self.name=name


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx

def find_nearest_point(arrayy,arrayx,x,y):
    arrayy = np.asarray(arrayy)
    arrayx = np.asarray(arrayx)
    newx=None
    newy=None
    for i in range(len(arrayy)):
        if(newx==None):
            newx=arrayx[i]
            newy=arrayy[i]
        else:
            r=np.abs(((newx**2) + (newy**2)) - (x**2 + y**2))
            rp = np.abs((arrayx[i]**2) + (arrayy[i]**2) - (x**2 + y**2))
            if( rp<r):
                newx = arrayx[i]
                newy = arrayy[i]
    return newx,newy

def getGradient(y: [], x: [], i: int = None, minchange: float = 1e-4, delfactor: float = 0.5):
    a = None
    b = None
    delf = None
    if (i == None):
        a = (y[-1] - y[-2])
        b = (x[-1] - x[-2])
    else:
        a = (y[i] - y[i - 1])
        b = (x[i] - x[i - 1])
    #todo add second order functionality
    if(b>0):
        if(a>0):
            print("asf")
        elif(a<0):
            print("asdflkj")
    elif(b<0):
        if(a>0):
           print("afd")
        elif(a<0):
            print("asfd")

    # if it is not greater than minchange  in x it be a factor of the y
    if (np.abs(b) >= minchange and np.abs(a)>0):
        grad = (b) / (a)
    else:
        rand = np.random.rand()
        grad = x[-1]*((rand-0.5))*5e-1
    # if (np.abs(grad) == np.nan or np.abs(grad) < minchange):
    #     grad = delfactor * a
    if(math.isnan(grad)):
        print("asfd")

    return grad


class Fitter:
    def __init__(self, func, ds: dataset, figret: figret, fargs:[dataset],max_int:int=10000,show_error:bool=False):
        tem = []
        for i in fargs:
            tem.append(i.data)
        self.dataform=fargs
        self.args = tuple(tem)
        self.ds = ds
        self.func = func
        self.figret = figret
        self.errors = []
        self.all_error=[]
        self.slider_changed=False
        self.pkfound = False
        self.error_count=0
        self.oldargs = []
        self.oldargs_byparameter=[]
        self.cur_par = 0
        self.cur_par_count = 0
        self.par_opt_len = 6
        self.learning_rate = 0.001
        self.org_learning_rate = 0.001
        self.chi=-1
        self.lcount=0
        self.maxlcount=3
        self.figret.ax.scatter(ds.x, ds.y,c="C1")
        self.maxinter=max_int+1
        self.errorplot=None
        self.show_error=show_error
        self.errorSlider=None
        self.complete=False
        self.cur_err_par=0
        self.pause=False
        self.ani = animation.FuncAnimation(figret.fig, self.update, interval=10, blit=False, repeat=False, frames=self.maxinter)
        axnext = self.figret.pyplt.axes([0.86, 0.25, 0.1, 0.075])
        self.bpause = Button(axnext, 'Play/Pause')
        axshowbesst = self.figret.pyplt.axes([0.86, 0.25 + 0.075, 0.1, 0.075])
        self.showbest = Button(axshowbesst, 'Show Best')
        self.slider_array = []
        self.figret.pyplt.subplots_adjust(left=0.25, bottom=0.5)
        self.buildSliders()
        #self.figret.fig.canvas.mpl_connect('button_press_event', self.playpause)
        self.bpause.on_clicked(self.playpause)
        self.showbest.on_clicked(self.showBest)
        self.figret.pyplt.show()

    def buildSliders(self):
        axcolor = 'lightgoldenrodyellow'

        for j in range(len(self.dataform)):
            df = self.dataform[j]
            ax = self.figret.pyplt.axes([0.15, 0.40 - (0.03*(j+1)), 0.65, 0.03], facecolor=axcolor)
            step=(df.max- df.min)/100
            slider = Slider(ax, df.name, df.min, df.max, valinit=df.data, valstep=step)
            slider.on_changed(self.updateSlider)
            self.slider_array.append(slider)
    def updateSlider(self,event):
        self.slider_changed=True

    def showBest(self,event):

        minarg = np.array(self.all_error).argmin()
        self.arg = self.oldargs[minarg]
        newds = self.func(*self.arg)
        self.figret.plots[0].set_ydata(newds.y)
        if (self.pause == False):
            self.playpause(event)

    def playpause(self,event):
        if(self.pause==False):
            self.ani.event_source.stop()
            self.pause=True
        else:
            self.ani.event_source.start()
            self.pause=False


    def update(self, i):
        f = self.func
        args = self.args
        nogo=False
        if(self.slider_changed):
            nogo=True
            self.slider_changed=False
            temp=[]
            for j in self.slider_array:
                temp.append(j.val)
            args=tuple(temp)

        for a in args:
            if(a==np.nan or a<=0 or a==None or math.isnan(a)):
                print("asfd")
        if(len(args)<7):
            print("asfd")
        for j in args:
            if(j<=0):
                print("fasfd")
        newds = f(*args)
        er = self.errorCalc(newds)
        if(math.isnan(er)):
            self.args = list(self.startNewPar())
            er = self.errorCalc(newds)
            print("asfd")
        if(len(self.all_error)>1 and nogo==False):
            if(er>self.all_error[-1]):
                tempargs = self.args
                try:
                    self.errors[self.cur_par].append(er)
                except Exception as e:
                    self.errors.append([er])
                try:
                    self.oldargs_byparameter[self.cur_par].append(self.args[self.cur_par])
                except Exception as e:
                    self.oldargs_byparameter.append([self.args[self.cur_par]])
                self.all_error.append(er)
                self.args = self.oldargs[-1]
                self.oldargs.append(tempargs)
                if(self.lcount<self.maxlcount):

                    self.lcount+=1


                    return
                else:
                    if(self.dataform[self.cur_par].lrate > 0.1):
                        self.dataform[self.cur_par].lrate =self.dataform[self.cur_par].lrate*0.8
                    self.cur_par += 1
                    if (self.cur_par > len(self.args) - 1):
                        self.cur_par = 0
                    self.lcount=0
                    return


        try:
            self.errors[self.cur_par].append(er)
        except Exception as e:
            self.errors.append([er])
        self.all_error.append(er)
        try:
            self.oldargs_byparameter[self.cur_par].append(self.args[self.cur_par])
        except Exception as e:
            self.oldargs_byparameter.append([self.args[self.cur_par]])

        self.oldargs.append(args)

        if(self.show_error and len(self.errors)== len(self.args)):
            self.plotError(i)
        newargs = []
        if (self.errors!=None and len(self.errors[self.cur_par])>=2):
            tw = np.matrix(self.oldargs)
            tw1 = tw[:, self.cur_par]
            tw2 = []
            for k in range(len(args)):
                if(k==self.cur_par):
                    for j in tw1:
                        tw2.append(float(j[0]))
                    grad = getGradient(y=self.errors[self.cur_par], x=self.oldargs_byparameter[self.cur_par])
                    if(grad<0):
                        print("negative")
                    #grad = grad/np.abs(grad)
                    # if(self.pkfound):
                    #     grad = grad*5e-2
                    #grad = grad/np.abs(grad)
                    gfactor = grad*(self.dataform[self.cur_par].lrate)*10
                    #gfactor = grad*(self.dataform[self.cur_par].max - self.dataform[self.cur_par].min)*(self.dataform[self.cur_par].lrate/100)
                    a = args[self.cur_par] - gfactor#*np.abs(args[self.cur_par])*1e-1 #self.learning_rate *
                    while np.abs(gfactor) >= args[self.cur_par]:
                        gfactor=gfactor*0.1
                        a = args[self.cur_par] - gfactor
                    while(a<=self.dataform[self.cur_par].min or a >= self.dataform[self.cur_par].max):
                        if(a<=self.dataform[self.cur_par].min and grad>0):
                            gfactor=gfactor*0.1
                        elif(a<=self.dataform[self.cur_par].min and grad<0):
                            gfactor = gfactor * 10
                        if (a >= self.dataform[self.cur_par].max and grad > 0):
                            gfactor = gfactor * 10
                        elif (a >= self.dataform[self.cur_par].max and grad < 0):
                            gfactor = gfactor * 0.1
                        a = args[self.cur_par] - gfactor
                    if(a<=0):
                        a= args[self.cur_par]*1e-1
                    self.cur_par_count += 1

                    if(math.isnan(a)):
                        print("asfd")
                    newargs.append(np.abs(a))
                else:
                    newargs.append(args[k])

        else:
            newargs = list(self.startNewPar())
        if (self.cur_par_count >= self.par_opt_len):
            self.cur_par += 1
            self.cur_par_count = 0
            self.learning_rate = self.org_learning_rate
            if (self.cur_par > (len(args) - 1)):
                self.cur_par = 0
        self.args = newargs
        self.figret.plots[0].set_ydata(newds.y)
        self.figret.ax.set_title("Iterataion: " + str(i) + " Current Parameter: " + str(self.cur_par) +" cur_par_count: "+str(self.cur_par_count)+ " Chi: " + str("{:.4f}".format(self.chi) ))
        for j in range(len(self.slider_array)):
            self.slider_array[j].set_val(self.args[j])
        self.slider_changed=False
        if(i>=self.maxinter-2):

            minarg = np.array(self.all_error).argmin()
            self.arg = self.oldargs[minarg]
            for j in range(len(self.slider_array)):
                self.slider_array[j].set_val(self.args[j])
            newds = self.func(*self.arg)
            self.figret.plots[0].set_ydata(newds.y)
            self.figret.pyplt.pause(1)
            self.figret.pyplt.close()
            self.complete=True


    def startNewPar(self):
        args = self.args
        rands = np.random.randint(100, size=len(args))
        newargs = []
        for i in range(len(args)):
            if i==self.cur_par:
                a = args[self.cur_par]
                newargs.append(np.abs(a * (1 + (1 / 100))))
            else:
                newargs.append(args[i])
        return tuple(newargs)


    def errorCalc(self, newds: dataset):
        y = newds.y
        x = newds.x
        cy = self.ds.y
        cx = self.ds.x
        idxs1 = []
        errs = []
        # for i in range(len(cy)):
        #     newx, newy = find_nearest_point(x,y,cx[i],cy[i])
        #     err = 0
        #     try:
        #         #err = ((cy[i]) - (newy)) ** 2 + ((cx[i]) - (newx)) ** 2
        #         err = (np.log10((cy[i]) / (newy))) ** 2 + (np.log10((cx[i]) / (newx))) ** 2
        #     except Exception as e:
        #         if(len(self.errors[self.cur_par])>=1):
        #             err = 4*self.errors[self.cur_par][-1]
        #         else:
        #             err = 1e2
        #     errs.append(err)
        my = np.nanmax(y[y != np.inf])
        mcy = np.nanmax(cy)
        if(math.isinf(my)):
            my=mcy+10
        val1, idx1 = find_nearest(y, my)
        idx1 = int(np.where(y==my)[0])
        idx2 = cy.index(mcy)
        pkerr = ((np.log(mcy) - np.log(my)) ** 2) + ((np.log(cx[idx2]) - np.log(x[idx1])) ** 2)
        #pkerr=pkerr**len(errs)
        # error = sum(errs) + pkerr
        # if error == None or pkerr == None or self.errors==None:
        #     print("the fuck")
        # if(len(self.errors)>self.cur_par):
        #     if(len(self.errors[self.cur_par])>=1):
        #         if(error>self.errors[self.cur_par][-1]):
        #             error=10*self.errors[self.cur_par][-1]
        #self.errors.append(error)
        # val3,idx3 = find_nearest(x,cx[0])
        # val4,idx4 = find_nearest(x,cx[-1])
        # yobs = y[idx3:idx4]
        # # group =math.ceil(len(yobs)/len(cy))
        # # yobs = yobs.reshape(-1, group).mean(axis=1)
        # difl = len(yobs) - len(cy)
        # chin=1
        # k=0
        # yobs= list(yobs)
        # yobs= []
        # for n in cy:
        #     vall,idxx = find_nearest(y,n)
        #     yobs.append(vall)

        # while k<(len(yobs)-chin):
        #     if(difl + chin <=0 or math.isnan(difl+chin)):
        #         print("adf")
        #     try:
        #         valcheck = (math.floor(len(yobs)/(difl + chin)))
        #         if valcheck!=0 and k%valcheck==0:
        #             tempy = (yobs[k] + yobs[k+1])/2
        #             #yobs = list(yobs)
        #             del yobs[k+1]
        #             chin+=1
        #             yobs[k]=tempy
        #            # yobs = np.array(yobs)
        #     except Exception as e:
        #         print(e)
        #     k+=1
        # while len(yobs)>len(cy):
        #     #yobs = list(yobs)
        #     del yobs[0]
        #     #yobs = np.array(yobs)
        #yobs = np.array(yobs)
        yobs=[]
        xobs = []
        for tt in range(len(cy)):
            # tx,ty =find_nearest_point(y,x,cx[tt],cy[tt])
            # xobs.append(tx)
            # yobs.append(ty)
            tval,tind = find_nearest(x,cx[tt])
            yobs.append(y[tind])
            xobs.append(tval)
        r=0
        for tt in range(len(cy)):
           r+=(np.log10(cy[tt])-np.log10(yobs[tt]))**2 # + (cx[tt]-xobs[tt])**2
        chi2 = np.exp(np.sqrt(r))#chisquare(yobs, f_exp=cy)[0]
        #chi2 = np.abs(chi2)
       # chi2 = np.log10(1 + chi2)
        val5,idx5 = find_nearest(x,cx[0])
        val6,idx6 = find_nearest(x,cx[-1])
        # int1 = np.trapz(np.log10(cy), x=np.log10(cx))
        # int2 = np.trapz(np.log10(y[idx5:idx6]), x=np.log10(x[idx5:idx6]))
        # error1 = np.abs(int2-int1)
        if pkerr<0.04:
            self.pkfound=True
        if pkerr>1:
            self.pkfound=False
        if(self.pkfound):
            #error = pkerr + error1 + chi2
            #error = error1 + chi2
            error = chi2 #+ pkerr
        else:
            #error=pkerr + error1 + chi2
            #error= error1 + chi2
            error= chi2 #+ pkerr
        #error = np.sqrt(error)
        self.chi = chi2
        #xobs=[]
        # for t in yobs:
        #     tval,tind=find_nearest(y,t)
        #     xobs.append(x[tind])
        if len(self.figret.plots)<2:
            plotty = self.figret.ax.scatter(xobs, yobs, c="C2")
            self.figret.plots.append(plotty)
        else:
            self.figret.plots[1].set_offsets(np.c_[xobs,yobs])
        self.figret.fig.canvas.draw()
        if(math.isnan(error)):
            print("asdf")
        return error

    def plotError(self,iter):
        if(self.errorplot==None):
            fig, ax = plt.subplots()
            plots=[]
            # for i in range(len(self.args)):
            #     plot = axs[i].plot(self.oldargs_byparameter[i],self.errors[i])
            #     axs[i].autoscale(True)
            #     plots.append(plot)
            # plot = axs[-1].scatter(range(iter),self.all_error)
            # plots.append(plot)
            plot, = ax.plot(self.oldargs_byparameter[0], self.errors[0],'--bo')
            plots.append(plot)
            fig.set_tight_layout(True)

            figr = figret(fig=fig,ax=ax,pyplt=plt,plots=plots)
            axframe = plt.axes([0.25, 0.1, 0.65, 0.03])
            self.errorSlider = Slider(axframe, 'Frame', 0, len(self.args), valinit=0,valfmt='%d')
            self.errorSlider.on_changed(self.updateErrorPlot)
            fig.show()
            self.errorplot=figr
        else:
            # for i in range(len(self.errorplot.plots)):
            plot = self.errorplot.plots[0]
            # plot.set_offsets(np.c_[self.oldargs_byparameter[i],self.errors[i]])
            xs = self.oldargs_byparameter[self.cur_err_par]
            ys = self.errors[self.cur_err_par]
            plot.set_xdata(xs)
            plot.set_ydata(ys)
            ax = self.errorplot.ax

            # for k in range(len(xs[0])):
            #     label = "{:.2f}".format(k)
            #
            #     ax.annotate(label,  # this is the text
            #                  (xs[k], ys[k]),  # this is the point to label
            #                  textcoords="offset points",  # how to position the text
            #                  xytext=(0, 10),  # distance from text to points (x,y)
            #                  ha='center')
            ax.relim()
            ax.autoscale_view()
            self.errorplot.pyplt.draw()
            # plot = self.errorplot.plots[-1]
            # plot.set_offsets(np.c_[range(iter),self.all_error])

    def updateErrorPlot(self,val):
        frame = int(np.floor(self.errorSlider.val))
        self.cur_err_par=frame
        ln = self.errorplot.plots[0]
        xs = self.oldargs_byparameter[frame]
        ys = self.errors[frame]
        ln.set_xdata(xs)
        ln.set_ydata(ys)
        ax = self.errorplot.ax
        for k in range(len(xs)):
            label = "{:.2f}".format(k)

            ax.annotate(label,  # this is the text
                        (xs[k], ys[k]),  # this is the point to label
                        textcoords="offset points",  # how to position the text
                        xytext=(0, 10),  # distance from text to points (x,y)
                        ha='center')

        ax.set_title(frame)
        ax.relim()
        ax.autoscale_view()
        self.errorplot.pyplt.draw()