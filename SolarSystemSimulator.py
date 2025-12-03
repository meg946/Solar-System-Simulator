from vpython import *

scene = canvas(title='Solar System Simulator', width=1450, height=750, center=vector(0,0,0), background=color.black)
 



# constants/variables


solarRadiusScaler = 1
solarMassScaler = 1
G = 6.67430e-11 # universal gravitational constant (in N*m^2/kg^2)
KMM = 1000.0 #kilometer to meter conversion
t = 0 #initial time
dt = 60*10 #time elapsed every calculation
trailLength = 200
year = 25 #int(input("Please enter the amount of years you want the simulation to run for: "))
year *= 1*365*24*60*60
trailTF = True #turns the trails on or off (True/False)



#planets

Center = sphere(pos=vector(0,0,0), radius = 6e7, color = color.white) #used to see the movement of the sun


Sun = sphere(pos=vector(-1.193445727790451E6,-4.326513370492446E5,3.147489527927423E4), radius = (6.96e8)*solarRadiusScaler, color=color.yellow, make_trail=trailTF, trail_color=color.yellow, retain=trailLength)
Sun.pos = Sun.pos*KMM #KM to M Conversions, Nasa JPL uses KM.
Mercury = sphere(pos=vector(-3.500920388740070E7,3.550587183193444E7,6.070128350746274E6), radius = 2.44e6, color=color.white, make_trail=trailTF, trail_color=color.white, retain=trailLength)
Mercury.pos = Mercury.pos*KMM
Venus = sphere(pos=vector(-1.086296486549258E8,-5.829314234717066E6,6.156516747455408E6), radius = 6.0518e6, color=color.orange, make_trail=trailTF, trail_color=color.orange, retain=trailLength)
Venus.pos = Venus.pos*KMM
Earth = sphere(pos=vector(-2.083706942527980E7,1.453614687357149E8,2.349029577782005E4), radius = 6.371e6, color=color.blue, make_trail=trailTF, trail_color=color.blue, retain=trailLength)
Earth.pos = Earth.pos*KMM
Mars = sphere(pos=vector(-4.933255427146677E7,-2.170077090234142E8,-3.326516764358014E6), radius = 3.4e6, color=color.red, make_trail=trailTF, trail_color=color.red, retain=trailLength)
Mars.pos = Mars.pos*KMM
Jupiter = sphere(pos=vector(5.230130607547573E+08,5.297012196913854E8,-1.389882261915931E+07), radius = 7.1492e7, color=color.orange, make_trail=trailTF, trail_color=color.orange, retain=trailLength)
Jupiter.pos = Jupiter.pos*KMM
Saturn = sphere(pos=vector(1.344055618845829E9,-5.579027459892032E8,-4.381277790545800E7), radius = 5.8232e7, color=color.yellow, make_trail=trailTF, trail_color=color.yellow, retain=trailLength)
Saturn.pos = Saturn.pos*KMM
Uranus = sphere(pos=vector(1.835448961570092E9,2.287775275446396E9,-1.528174038176084E7), radius = 2.5362e7, color=color.cyan, make_trail=trailTF, trail_color=color.cyan, retain=trailLength)
Uranus.pos = Uranus.pos*KMM
Neptune = sphere(pos=vector(4.463204230864025E9,-2.692934972916258E8,-9.731348599939896E7), radius = 2.4622e7, color=color.blue, make_trail=trailTF, trail_color=color.blue, retain=trailLength)
Neptune.pos = Neptune.pos*KMM


#Celestial Body Mass

Sun.mass = 1.989e30
Mercury.mass = 3.3e23
Venus.mass = 4.867e24
Earth.mass = 5.97219e24
Mars.mass = 6.39e23
Jupiter.mass = 1.89819e27
Saturn.mass = 5.683e26
Uranus.mass = 8.681e25
Neptune.mass = 1.024e26



#Celestial Body Velocity

Sun.vel = vector(8.416834414290640E-3,-1.224970637260944E-2,-7.880965476347694E-5)*KMM
Mercury.vel = vector(-4.534322093250886E01,-3.144353941271197E01, 1.591160809990642e00)*KMM
Venus.vel = vector(1.556527166368694,-3.514424492207917E1,-5.718886156716394E-1)*KMM
Earth.vel = vector(-2.999819163289379E1,-4.101674617595416,3.286874800350059E-4)*KMM
Mars.vel = vector(2.457349624092830E1,-3.190776149448077,-6.692497105645787E-1)*KMM
Jupiter.vel = vector(-9.441911327951376E+00,9.800919435568662E+00,1.706764389597479E-01)*KMM
Saturn.vel = vector(3.163919674177270,8.902550134242253,-2.807710008186199E-1)*KMM
Uranus.vel = vector(-5.361799100695984,3.944245269740309,8.411028905930662E-2)*KMM
Neptune.vel = vector(2.914198846879136E-1,5.457644137467666,-1.191059003480193E-1)*KMM


# in order to add objects, follow HalleyComet and Ganymede. The vectors are found here https://ssd.jpl.nasa.gov/horizons/app.html#/, just hit edit on the target body, type in what body you want, and then hit generate ephemeris
#Non planetary bodies

#HalleyComet = box(pos=vector(-2.968971283460145E9,4.075816678506456E9,-1.488768318255022E9)*KMM,size=vector(14420,7400,7400),color=color.purple, make_trail=trailTF, trail_color=color.white, retain=trailLength)
#HalleyComet.vel = vector(7.248055206614089E-1,5.382164590573272E-1,1.093898188740034E-01)*KMM
#HalleyComet.mass = 2.2e14

#Ganymede = sphere(pos=vector(5.219406283438694E+08,5.297323622302089E+08,-1.391271976216149E+07)*KMM,radius = 2631*KMM, color=color.gray(.4), make_trail=trailTF, trail_color=color.white, retain=trailLength)
#Ganymede.vel = vector(-9.749079485645257,-1.042257835648576,-2.470680016537412)*KMM
#Ganymede.mass = 1.4819e23

#General Gravity Force equation
#       (Mm*-G)/mag(M.pos-m.pos)**2*norm(M.pos-m.pos)

#General Acceleration Equation
#       A = F/M

#General Velocity Equation
#       V = V+A*dT

#General Position Update Equation
#       Pos = Pos+V*dT

bodies = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune] #list of objects in the system

while t <= (year): #goes for however many years you input.
    rate(1) 
    days = (t/(24*60*60))
    years = (days/365)
    for i in bodies:
        force = vector(0,0,0) #to reset the force after finishing a planet
        body = i
        for j in [p for p in bodies if p != i]:
            next_body = j
            body.ForceCalc = (-G*body.mass*next_body.mass)/(mag(body.pos-next_body.pos))**2*norm(body.pos-next_body.pos)
            force += body.ForceCalc #adds the forces from each planet together.
        body.a = force/body.mass
        body.vel = body.vel + body.a*dt
        body.pos = body.pos + body.vel*dt

    scene.center = Sun.pos #used to center the screen on any body, instead of <0,0,0>

    t = t+dt