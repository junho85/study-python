import base64

decoded = base64.b64decode(b'MSB4IDEgPSAxCjEgeCAyID0gMgoxIHggMyA9IDMKMSB4IDQgPSA0CjEgeCA1ID0gNQoxIHggNiA9IDYKMSB4IDcgPSA3CjEgeCA4ID0gOAoxIHggOSA9IDkKMiB4IDEgPSAyCjIgeCAyID0gNAoyIHggMyA9IDYKMiB4IDQgPSA4CjIgeCA1ID0gMTAKMiB4IDYgPSAxMgoyIHggNyA9IDE0CjIgeCA4ID0gMTYKMiB4IDkgPSAxOAozIHggMSA9IDMKMyB4IDIgPSA2CjMgeCAzID0gOQozIHggNCA9IDEyCjMgeCA1ID0gMTUKMyB4IDYgPSAxOAozIHggNyA9IDIxCjMgeCA4ID0gMjQKMyB4IDkgPSAyNwo0IHggMSA9IDQKNCB4IDIgPSA4CjQgeCAzID0gMTIKNCB4IDQgPSAxNgo0IHggNSA9IDIwCjQgeCA2ID0gMjQKNCB4IDcgPSAyOAo0IHggOCA9IDMyCjQgeCA5ID0gMzYKNSB4IDEgPSA1CjUgeCAyID0gMTAKNSB4IDMgPSAxNQo1IHggNCA9IDIwCjUgeCA1ID0gMjUKNSB4IDYgPSAzMAo1IHggNyA9IDM1CjUgeCA4ID0gNDAKNSB4IDkgPSA0NQo2IHggMSA9IDYKNiB4IDIgPSAxMgo2IHggMyA9IDE4CjYgeCA0ID0gMjQKNiB4IDUgPSAzMAo2IHggNiA9IDM2CjYgeCA3ID0gNDIKNiB4IDggPSA0OAo2IHggOSA9IDU0CjcgeCAxID0gNwo3IHggMiA9IDE0CjcgeCAzID0gMjEKNyB4IDQgPSAyOAo3IHggNSA9IDM1CjcgeCA2ID0gNDIKNyB4IDcgPSA0OQo3IHggOCA9IDU2CjcgeCA5ID0gNjMKOCB4IDEgPSA4CjggeCAyID0gMTYKOCB4IDMgPSAyNAo4IHggNCA9IDMyCjggeCA1ID0gNDAKOCB4IDYgPSA0OAo4IHggNyA9IDU2CjggeCA4ID0gNjQKOCB4IDkgPSA3Mgo5IHggMSA9IDkKOSB4IDIgPSAxOAo5IHggMyA9IDI3CjkgeCA0ID0gMzYKOSB4IDUgPSA0NQo5IHggNiA9IDU0CjkgeCA3ID0gNjMKOSB4IDggPSA3Mgo5IHggOSA9IDgx').decode('utf-8')
print(decoded)
