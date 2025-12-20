// Set the geometry factory to OpenCASCADE (recommended for extrusion operations)
SetFactory("OpenCASCADE");

// Define parameters for the ellipse and extrusion
a = 1.0;  // Semi-major axis length
b = 0.5;  // Semi-minor axis length
H = 1.0;  // Extrusion height
lc = 0.05; // Characteristic length for meshing

center_x = 2.0;
center_y = 0.0;

// Create the center point
Point(1) = {center_x, center_y, 0, lc};

// Create points on the major and minor axes to define the ellipse
Point(2) = {center_x+a, 0+center_y, 0, lc}; // Point on major axis
Point(3) = {center_x+0, b+center_y, 0, lc}; // Point on minor axis
Point(4) = {-a+center_x, 0+center_y, 0, lc}; // Point on major axis
Point(5) = {0+center_x, -b+center_y, 0, lc}; // Point on minor axis

// Define the arcs that form the ellipse
// The syntax is Ellipse(tag) = {start_point_tag, center_point_tag, major_axis_point_tag, end_point_tag};
Ellipse(1) = {2, 1, 2, 3};
Ellipse(2) = {3, 1, 2, 4};
Ellipse(3) = {4, 1, 2, 5};
Ellipse(4) = {5, 1, 2, 2};

// Create a Line Loop from the ellipse arcs
Curve Loop(1) = {1, 2, 3, 4};

// Create a Surface from the Line Loop
Surface(1) = {1};

// Extrude the surface to create a volume
// Extrude {translation_vector} {Surface{surface_tag};}
Extrude {0, 0, H} {
  Surface{1};
  Layers{25}; // Optional: defines number of layers in the extrusion direction
  Recombine; // Optional: tries to generate quads/hexahedra
}

// Generate the 3D mesh
Mesh 3D;
