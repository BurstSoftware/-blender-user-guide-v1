import streamlit as st

# Set the title and description
st.title("Blender Beginner Guide 🎨")
st.markdown("A quick reference guide for getting started with Blender!")

# Section for Key Concepts
st.header("Core Blender Concepts")
st.write("- **3D Objects**: Create and manipulate 3D models.")
st.write("- **Animating**: Add motion to your models.")
st.write("- **Rigging**: Add a skeleton to models for animation.")
st.write("- **Compositing**: Combine visual elements into a final render.")

# Section for Changing Primitive Objects
st.header("Adding Primitive Objects")
st.write("To add basic shapes (e.g., cubes, spheres):")
st.write("- Press **Shift + A** to open the Add menu and select a primitive object.")

# Section for Scaling Along One Axis
st.header("Scaling Along One Axis")
st.write("To scale an object along a single axis:")
st.write("- Select the object.")
st.write("- Press **S** (Scale), then **X**, **Y**, or **Z** to choose the axis.")
st.write("- Move the mouse or type a value, then press **Enter**.")

# Section for Blender Modes
st.header("Blender Modes")
st.write("Blender offers several modes for editing:")
st.write("- **Object Mode**: Manipulate objects as a whole.")
st.write("- **Edit Mode**: Edit the mesh (vertices, edges, faces).")
st.write("- **Sculpt Mode**: Sculpt models like digital clay.")
st.write("- **Vertex Mode**: Edit individual vertices (part of Edit Mode).")
st.write("- **Weight Paint**: Paint weights for rigging.")
st.write("- **Texture Paint**: Paint textures directly on your model.")

# Section for Switching Modes
st.header("Switching Between Modes")
st.write("- Press **Tab** to toggle between Object Mode and Edit Mode.")
st.write("- Use **Ctrl + Tab** to open a pie menu and select other modes.")

# Footer
st.markdown("---")
st.write("💡 **Pro Tip**: Memorize these shortcuts to speed up your Blender workflow!")
