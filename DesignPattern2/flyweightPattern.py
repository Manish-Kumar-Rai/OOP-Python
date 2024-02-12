#------------------ The flywieght Pattern --------------------
import weakref
import gc

class CarModel:
    _models = weakref.WeakValueDictionary()

    def __new__(cls,model_name,*args,**kwargs):
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model
        return model
    
    def __init__(self,model_name,air=False,tilt=False,power_lock=False,usb_charger=False,cruise_control=False,alloy_wheels=False):
        if not hasattr(self,"initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.usb_charger = usb_charger
            self.power_lock = power_lock
            self.alloy_wheels = alloy_wheels
            self.initted = True

    def check_serial(self,serial_number):
        print(
            "Sorry, we are unable to check"
            "the serial number {0} on the {1}"
            "at this time.".format(serial_number,self.model_name)
        )
        

class Car:
    def __init__(self,model,color,serial):
        self.model = model
        self.color = color
        self.serial = serial

    def check_serial(self):
        return self.model.check_serial(self.serial)
    
dx = CarModel("FIT DX")
lx = CarModel("FIT LX",air=True,alloy_wheels=True,cruise_control=True,power_lock=True,tilt=True,usb_charger=True)

car1 = Car(dx,"blue","12345")
car2 = Car(dx,"black","12346")
car3 = Car(lx,"red","12347")

print(id(lx))
del lx
del car3
gc.collect()
lx = CarModel("FIT LX",air=True,alloy_wheels=True,cruise_control=True,power_lock=True,tilt=True,usb_charger=True)
print(id(lx))
lx = CarModel("FIT LX")
print(lx.air)
print(id(lx))
