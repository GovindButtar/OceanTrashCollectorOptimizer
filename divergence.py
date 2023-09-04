from sympy.physics.vector import ReferenceFrame, is_solenoidal
from sympy.plotting.plot import plot3d
R = ReferenceFrame('R')
print(R.x)
field = R[1]*R[2]*R.x + R[0]*R[2]*R.y + R[0]*R[1]*R.z
plot3d(field)