# gs_interfaces
Paczka zawiera definicje wiadomości ROS2 dla ground segmentu 

## Creating messages for this project - the easy way
1. You can generate message definitions files by editing config.json (assuming that gs_interfaces is a submodule of gs_web_app)
and running `python3 generate_ros2_messages.py` in console
2. And then adding the message file name in `CMakeLists.txt` file in the `rosidl_generate_interfaces` section

## knowdlege base about working with msgs instruction

### 1. Creating message
This one is simple, create a text file with .msg or .srv (in case of server message) extension and define custom messages following the format:

`type` `variable_name` `# comment`

Note that `variable_name` has to start with alphabetic symbol and can't consist of upper_case letters.

### 2. Update package.xml
If you message is of non standard class/type add dependencies to package.xml e.g. `<depend>geometry_msgs</depend>`

### 3. Update CMakeLists.txt
Modify your CMakeLists.txt to include the custom message files for the ROS2 build system to process them.
Add your message files under the rosidl_generate_interfaces function call.

```
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/YourMessage.msg"
  # Add more message files here
  DEPENDENCIES std_msgs geometry_msgs
)
```

Note that as for 16/03/2024 we are not following typical directory pattern yet (TODO) - 
For instance, `msg/tanking_msgs/LoadCell.msg` tanking_msgs should actually be a separate package i.e. repo should be as such `gs_interfaces/tanking_msgs/msg/LoadCell.msg'

### 4. Build Your Package
Navigate back to the root of your workspace and build your package.
Typically your workspace is a directory consisting of packages, e.g. gs_interfaces package could be in such directory: `simba_ws/src/gs_interfaces`

```
cd <>/simba_ws
colcon build --packages-select gs_interfaces
```

### 5. Source the Workspace
After building, don't forget to source the setup files to make your new messages available to ROS2.

`. install/setup.bash`

### 6. Verify Message Creation
To verify that your message has been created successfully, you can list message types and look for your custom message.
`ros2 interface list | grep gs_interfaces`