import geoip2.database #pip install geoip
import folium #pip install folium
import random
import nmap #pip install python-nmap


def scan(ip):
    
    #scan ip
    nm = nmap.PortScanner()
    nm.scan(hosts=ip,arguments='-n -F -T5')
    string=""
    #if exist open ports return them else return nothing
    try:
        result=nm[ip]['tcp'].keys()
        for i in result:
            
            if nm[ip]['tcp'][i]['state']=="open":
                string=string+str(i)+' '
    except:
        string=""
    return string

def main():
    #storage the location of seted markers
    used_locations=[]
    used_locations.append(0)
    # read from db
    try:
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    except:
        #because github accept small files, I split the data base and now I will recreate the database
        with open("GeoLite2-City.mmdb",'wb') as file:
            for i in range(4):
                with open("db"+str(i),'rb') as merge:
                    for line in merge:
                        file.write(line)
                    merge.close()
            file.close()
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')

    #create map
    map = folium.Map()
    #check if user want random ip or to read from file
    state=input("read random / read from file(r/f):")
    if state=='f':
        file=input("name of file:")
        f= open(file,'r')
    #number of elements to put on map
    if state == 'r':
        number=int(input("how many?:"))
    else:
        with open(file,'r') as fp:
            number = len(fp.readlines())
    #check if user want to show only open ports ip
    nmap_state=input("show only with open ports(y/n):")
    for i in range(number):
        #check if generated ip has port open and it is in database
        not_found=1
        
        while not_found==1:
            #we assume that generated ip is valid
            not_found=0
            
           
            #generate ip or read ip from file
            if state=='r':
                ip = str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))
            else:
                
                ip = f.readline()
                if not ip:
                    break
                ip=ip.replace('\n',"")

                    
            #scan ip and get output
            if nmap_state=="y":
                string=scan(ip)
            
                #check if port is open
                if string=="" and state=='r':
                    not_found=1
                    continue
            else:
                string=""    
            
            #check if ip is in database
            try:
                response = reader.city(ip)
            except:
                not_found=1
                continue
            
            ip=ip+'\n'+string
            #search if the location is used before
            for j in used_locations:
                if j==response.location.latitude:
                    response.location.latitude=response.location.latitude+0.0002
        
                    
                
            used_locations.append(response.location.latitude)
                
            #get ip location and add to map
            
            location = [response.location.latitude, response.location.longitude]
            folium.Marker(location=location,popup=ip).add_to(map)
            
   
    # save map in html format
    map.save('test.html')


if __name__ == "__main__":
    main()    
