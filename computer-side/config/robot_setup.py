robot_sens = 1.2
servos = [
#	name		pin	pulse_range,	start	angle_rnge	speed, sens
    ('waist',	12,	(900, 1100),	90,		(0, 30),	0.1,	1.0),
    ('shoulder',11,	(600, 2400),	60,		(30, 150),	0.1,	1.0),
    ('elbow',	10,	(600, 2400),	50,		(50, 180),	0.1,	1.0),
    ('wrist',	9,	(600, 2400),	0,		(0, 180),	0.1,	1.0),
    ('claw',	8,	(600, 2400), 	0,		(0, 180),	0.1,	1.0),
]
#TODO: servo control sensitivity
#port_name = 'F'
#port_name = 'R:/dev/ttyUSB*'
port_name = 'R:/dev/tty.usb*'
baud_rate = 57600
object_name = 'Robot over Serial'
