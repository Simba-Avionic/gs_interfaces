cmake_minimum_required(VERSION 3.8)
project(gs_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/tanking_msgs/LoadCell.msg"
  "msg/tanking_msgs/TankingCmds.msg"
  "msg/tanking_msgs/TankingControl.msg"
  "msg/tanking_msgs/Tensobelki.msg"
  "msg/tanking_msgs/ValveSensors.msg"
  "msg/tanking_msgs/ValveServos.msg"
  "msg/rocket_msgs/RocketStatus.msg"
  "msg/rocket_msgs/RocketTelemetry.msg"
  "msg/radio_msgs/Telemetry433.msg
  "msg/radio_msgs/RadioTelemetry.msg"
  "msg/control_panel_msgs/ControlPanelSwitches.msg"

  "srv/FixGPSPosition.srv"
  DEPENDENCIES builtin_interfaces std_msgs geometry_msgs
)

ament_package()
