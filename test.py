import mesh
import os
from mesh import *
from subdivision import *

input_mesh = input("Enter the mesh you want to subdivide: ")
data_path = 'tests/data/{}.off'.format(input_mesh)

# HalfedgeMesh
mesh = mesh.HalfedgeMesh(data_path)

# Returns a list of Vertex type (in order of file)--similarly for halfedges,
# and facets
mesh.vertices

# The number of facets in the mesh
print(len(mesh.facets))

# Get the 10th halfedge
mesh.halfedges[10]

# Get the halfedge that starts at vertex 25 and ends at vertex 50
# mesh.get_halfedge(0, 1)

print(mesh.vertices)
# for vertex in mesh.vertices:
#     print(vertex.get_vertex())

print(mesh.facets)
print('--------------------')
for face in mesh.facets:
    print(face.a, face.b, face.c)

# to save the halfedge mesh you will need to following function.
def save_halfmesh_as_obj(mesh, file_name):
    if not os.path.exists("output"):
        os.makedirs("output")

    # Construct full file path with folder and file name
    file_path = os.path.join("output", file_name)
    with open(file_path, 'w') as open_file:
        for vertex in mesh.vertices:
            lv = vertex.get_vertex()
            open_file.write("v {} {} {} \n".format(lv[0], lv[1], lv[2]))

        for face in mesh.facets:
            open_file.write("f {} {} {}\n".format(face.a+1, face.b+1, face.c+1))

n_it = int(input("Enter number of iterations for loop subdivision: "))

for i in range(n_it):
    mesh = binary_loop_subdivision(mesh)

save_halfmesh_as_obj(mesh, '{}_iterations_{}.obj'.format(input_mesh,n_it))
