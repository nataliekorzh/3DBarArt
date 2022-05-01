# 3D Bar Art

Create your own 3D art by producing projections of rectangular solids across a canvas! These appear to be 3D by changing their size and orientation based on their
distance from the origin. 

`3Dbar_random.py h w num` will produce `num` rectangular solids randomly across the `h` x `w` canvas 

`3Dbar_photo.py image.pgm` Given grayscale target image `image.pgm`, will produce a 3D version by placing filled in rectangular solids
at the locations of the darkest pixels.
