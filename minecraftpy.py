import mcpi.minecraft as minecraft
from mcpi.entity import PRIMED_TNT
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z=pos.z
import main.py


entityVar = mc.spawnEntity(x, y, z, PRIMED_TNT.id)
entityVar = mc.spawnEntity(x, y, z, PRIMED_TNT.id)
entityVar = mc.spawnEntity(x, y, z, PRIMED_TNT.id)
entityVar = mc.spawnEntity(x, y, z, PRIMED_TNT.id)
entityVar = mc.spawnEntity(x, y, z, PRIMED_TNT.id)