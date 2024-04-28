"""
Kindly visit the below URL and convert the UML diagram into Python Class and its
methods.https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md
"""



"""TV class
.TVClass - Base class
.LedTV class
.PlasmaTV class

Part - A

1.Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. 
Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.
2.Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
3.Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 
60 the TV will stay at the current channel.
4.Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from 
the constructor).
5.It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, 
volume 75".

Part - B : LED , Plasma

1.Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh 
rate , functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed 
features of the TV"""

# Define a base class TV
class TV:
    
    # Initialising the TV with a brand
    def __init__(self,brand):
        self.brand=brand
        self.channel=1 #Default channel is 
        self.volume=50 # Default volume is 50
        self.on_off=False # TV is initially off
    
    
    
    # Method to increase the volume
    def increase_volume(self):
        if self.volume<100:
            self.volume +=1


    # Method to decrease the volume
    def decrease_volume(self):
        if self.volume>0:
            self.volume-=1

    # Method to set channel, channels are between 1 and 50
    def set_channel(self,channel):
        if channel>=1 and channel<=50:
            self.channel=channel
   
   # Method to reset tv to default channel and volume 
    def reset_tv(self):
        self.channel=1
        self.volume=50

    # Method to return the status of the tv
    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


# Defining a subclass LedTV inheriting from TV class
class LedTV(TV):
    
    
    # Initialising the LedTV with additional attributes
    def __init__ (self,brand,screen_thickness,energy_usage,lifespan, refresh_rate,viewingangle,backlight):
        
        # Calling the constructor of the base class
        super().__init__(brand)
        self.screen_thickness= screen_thickness
        self.energy_usage=energy_usage
        self.lifespan=lifespan
        self.refresh_rate=refresh_rate
        self.viewingangle=viewingangle
        self.backlight=backlight

    # Method to display details specific to LedTV
    def Display_details(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Eneergy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate},Viewing Angle: {self.viewingangle}, Backlight: {self.backlight}"


# Defining  another subclass PlasmaTV inheriting from TV
class PlasmaTV(TV):

    # Initialising the PlasmaTV with additional attributes
    def __init__ (self,brand,screen_thickness,energy_usage,lifespan, refresh_rate,viewingangle,backlight):
        
        # Calling the constructor of the base class
        super().__init__(brand)
        self.screen_thickness= screen_thickness
        self.energy_usage=energy_usage
        self.lifespan=lifespan
        self.refresh_rate=refresh_rate
        self.viewingangle=viewingangle
        self.backlight=backlight

    # Method to display details specific to PlasmaTV
    def Display_details(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Eneergy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate},Viewing Angle: {self.viewingangle}, Backlight: {self.backlight}"

# Printing LED TV operations
print("LED TV")
led_tv=LedTV("Samsung","10mm","Low","10 years","120Hz","178 degrees","Edge_light")
print("Initial status",led_tv.status())
led_tv.increase_volume()
print("Volume increases. Current status:",led_tv.status())
led_tv.decrease_volume()
print("Volume decreased. Current status:",led_tv.status())
led_tv.set_channel(8)
print("Channel set to 8. Current status:",led_tv.status())
led_tv.reset_tv()
print("Tv reset. Current status:",led_tv.status())
print("Tv details:",led_tv.Display_details())


# Printing Plasma TV operations
print("Plasma TV" )
plasma_tv=PlasmaTV("Sony","11mm","Medium","5 years","60Hz","160 degrees","Full Array")
print("Initial status",plasma_tv.status())
plasma_tv.increase_volume()
print("Volume increases. Current status:",plasma_tv.status())
plasma_tv.decrease_volume()
print("Volume decreased. Current status:",plasma_tv.status())
plasma_tv.set_channel(5)
print("Channel set to 5. Current status:",plasma_tv.status())
plasma_tv.reset_tv()
print("Tv reset. Current status:",plasma_tv.status())
print("Tv details:",plasma_tv.Display_details())