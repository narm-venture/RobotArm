robot_sens = 1.2
robot_sens_exp = 1

#servos = [
#	#name		pin	pulse_range,	start	angle_rnge	speed, sens
#    ('waist', 12, (900, 1100), 90, (0,30), .1, 2.0),
#    ('shoulder', 11, (600, 2400), 60, (0, 180),	.1, 1.5),
#    ('elbow', 10, (600, 2400), 50, (50, 180), .1, 1.0),
#    ('wrist', 9, (600, 2400), 0, (0, 180), .1,	1.0),
#    ('claw', 8, (600, 2400),  0, (0, 180), .1, 1.0),
#]

servos = [
	#name		pin	pulse_range,	start	angle_rnge	speed, sens, sens_exp
    ('waist',	12,	(900, 1100),	162,	(5,30),		1,		0.6,	2.5),
    ('shoulder',11,	(600, 2400),	43.52,	(75, 140),	1,		1.3,	2.0),
    ('elbow',	10,	(600, 2400),	20.125,	(20, 175),	1,		0.6,	1.5),
    ('wrist',	9,	(600, 2400),	97.55,	(2, 150),	1,		1.2,	1.2),
    ('claw',	8,	(600, 2400),	0,		(0, 180),	1,		2.5,	1.0),
]

# Good defaults with original angle range
#servos = [
#	#name		pin	pulse_range,	start	angle_rnge	speed, sens
#    ('waist',    12, (900, 1100), 162,  (0,30),    .1, 2.0),
#    ('shoulder', 11, (600, 2400), 24.5, (81, 132), .1, 1.5),
#    ('elbow',    10, (600, 2400), 3,    (44, 152), .1, 1.0),
#    ('wrist',    9,  (600, 2400), 41,   (0, 180),  .1, 1.0),
#    ('claw',     8,  (600, 2400), 0,    (0, 180),  .1, 1.0),
#]


#waist is at 162
#shoulder is at 84
#elbow is at 3
#wrist is at 41
#claw is at 0

#TODO: servo control sensitivity
#port_name = 'F'
port_name = 'R:/dev/tty.usb*'
port_name = 'R:/dev/ttyUSB*'
baud_rate = 57600
log_file = '/home/sam/Dropbox/dev/eclipse_workspace/Robo/dev/log.txt'
object_name = 'Robot over Serial'
