class Mobile:
    button = "on"
    call_list=[]
    def __init__(self,company,ROM,camera,RAM):
        self.company = company
        self.RAM = RAM
        self.ROM = ROM
        self.camera = camera
        
    def about (self):
        if self.button=="on":
            print("about Mobile")
            print("company :",self.company)
            print("RAM :",self.RAM)
            print("ROM :",self.ROM)
            print("camera :",self.camera)
        else:
            print("mobile locked")

    def call(self):
        from datetime.datetime import now
        import time
        if self.button=="on":
            number = input("dial number ...")
            t=T.strftime("%d/%m/%y %H:%M%:S%")
            print("calling......".center(20," "))
            print(f"{number}".center(20," "))
            
            if input("is recieved? (y/n)")=="y":
                self.call_list.append(f"+{number} {t}")
               
            else:
                self.call_list.append(f"-{number} {t}")
                
        else:
            print("MobIle Locked")
        
    def unlock(self):
        if input("enter ur pin")== self.pin:
            print("unlocked")
            self.button = "on"
        else:
            print("WRONG PIN")
        
    def lock(self):
        print("locked")
        self.button = "off"
        
    def set_pin(self):
        self.pin = input("set your pin")
        print("pin registered")
    
    def call_details(self):
        for j,i in enumerate(self.call_list):
            print(j+1,":",i)
        
