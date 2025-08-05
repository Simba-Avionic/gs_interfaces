# TankingControl message
# ---
std_msgs/Header header 

int8 valve_feed
int8 valve_vent

bool decouple

int8 VALVE_OPEN = 100
int8 VALVE_CLOSE = 100

bool DECOUPLE_OPEN = true
bool DECOUPLE_CLOSE = false