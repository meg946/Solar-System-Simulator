from vpython import *

#constants
KMM = 1000
solarRadiusScaler = 1
trailTF = True
trailLength = 200

#Initials
Sun = sphere(pos=vector(-1.193445727790451E6,-4.326513370492446E5,3.147489527927423E4), radius = (6.96e8)*solarRadiusScaler, color=color.yellow, make_trail=trailTF, trail_color=color.yellow, retain=trailLength)
Mercury = sphere(pos=vector(-3.500920388740070E7,3.550587183193444E7,6.070128350746274E6), radius = 2.44e6, color=color.white, make_trail=trailTF, trail_color=color.white, retain=trailLength)
Venus = sphere(pos=vector(-1.086296486549258E8,-5.829314234717066E6,6.156516747455408E6), radius = 6.0518e6, color=color.orange, make_trail=trailTF, trail_color=color.orange, retain=trailLength)
Earth = sphere(pos=vector(-2.083706942527980E7,1.453614687357149E8,2.349029577782005E4), radius = 6.371e6, color=color.blue, make_trail=trailTF, trail_color=color.blue, retain=trailLength)
Mars = sphere(pos=vector(-4.933255427146677E7,-2.170077090234142E8,-3.326516764358014E6), radius = 3.4e6, color=color.red, make_trail=trailTF, trail_color=color.red, retain=trailLength)
Jupiter = sphere(pos=vector(5.230130607547573E+08,5.297012196913854E8,-1.389882261915931E+07), radius = 7.1492e7, color=color.orange, make_trail=trailTF, trail_color=color.orange, retain=trailLength)
Saturn = sphere(pos=vector(1.344055618845829E9,-5.579027459892032E8,-4.381277790545800E7), radius = 5.8232e7, color=color.yellow, make_trail=trailTF, trail_color=color.yellow, retain=trailLength)
Uranus = sphere(pos=vector(1.835448961570092E9,2.287775275446396E9,-1.528174038176084E7), radius = 2.5362e7, color=color.cyan, make_trail=trailTF, trail_color=color.cyan, retain=trailLength)
Neptune = sphere(pos=vector(4.463204230864025E9,-2.692934972916258E8,-9.731348599939896E7), radius = 2.4622e7, color=color.blue, make_trail=trailTF, trail_color=color.blue, retain=trailLength)

#Initial Position Unit Corrections
Sun.pos = Sun.pos*KMM #KM to M Conversions, Nasa JPL uses KM.
Mercury.pos = Mercury.pos*KMM
Venus.pos = Venus.pos*KMM
Earth.pos = Earth.pos*KMM
Mars.pos = Mars.pos*KMM
Jupiter.pos = Jupiter.pos*KMM
Saturn.pos = Saturn.pos*KMM
Uranus.pos = Uranus.pos*KMM
Neptune.pos = Neptune.pos*KMM

#Mass
Sun.mass = 1.989e30
Mercury.mass = 3.3e23
Venus.mass = 4.867e24
Earth.mass = 5.97219e24
Mars.mass = 6.39e23
Jupiter.mass = 1.89819e27
Saturn.mass = 5.683e26
Uranus.mass = 8.681e25
Neptune.mass = 1.024e26



#Velocity
Sun.vel = vector(8.416834414290640E-3,-1.224970637260944E-2,-7.880965476347694E-5)*KMM
Mercury.vel = vector(-4.534322093250886E01,-3.144353941271197E01, 1.591160809990642e00)*KMM
Venus.vel = vector(1.556527166368694,-3.514424492207917E1,-5.718886156716394E-1)*KMM
Earth.vel = vector(-2.999819163289379E1,-4.101674617595416,3.286874800350059E-4)*KMM
Mars.vel = vector(2.457349624092830E1,-3.190776149448077,-6.692497105645787E-1)*KMM
Jupiter.vel = vector(-9.441911327951376E+00,9.800919435568662E+00,1.706764389597479E-01)*KMM
Saturn.vel = vector(3.163919674177270,8.902550134242253,-2.807710008186199E-1)*KMM
Uranus.vel = vector(-5.361799100695984,3.944245269740309,8.411028905930662E-2)*KMM
Neptune.vel = vector(2.914198846879136E-1,5.457644137467666,-1.191059003480193E-1)*KMM

