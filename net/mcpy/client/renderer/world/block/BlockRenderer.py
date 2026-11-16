import json
from net.mcpy.client.renderer.world.block.Models import models, uv, width, height
from net.mcpy.resources.ResourceLocation import ResourceLocation
import net.mcpy.resources.FileLoader as FileLoader

render_data=json.load(open(FileLoader.getFromModOrFrozen("assets/minecraft/render/render_data.json")))

def getNY(u0, u1, v0, v1, x0=0,y0=0,z0=0,x1=1,y1=1,z1=1, x_offset=0, y_offset=0, z_offset=0):
	return [
			x1+x_offset,y0+y_offset,z1+z_offset,u0,v0,
			x0+x_offset,y0+y_offset,z1+z_offset,u0,v1,
			x0+x_offset,y0+y_offset,z0+z_offset,u1,v1,
			x1+x_offset,y0+y_offset,z1+z_offset,u0,v0,
			x0+x_offset,y0+y_offset,z0+z_offset,u1,v1,
			x1+x_offset,y0+y_offset,z0+z_offset,u1,v0
		]
	
def getPY(u0, u1, v0, v1, x0=0,y0=0,z0=0,x1=1,y1=1,z1=1, x_offset=0, y_offset=0, z_offset=0):
	return [
			x0+x_offset,y1+y_offset,z1+z_offset,u0,v0,
			x1+x_offset,y1+y_offset,z1+z_offset,u0,v1,
			x1+x_offset,y1+y_offset,z0+z_offset,u1,v1,
			x0+x_offset,y1+y_offset,z1+z_offset,u0,v0,
			x1+x_offset,y1+y_offset,z0+z_offset,u1,v1,
			x0+x_offset,y1+y_offset,z0+z_offset,u1,v0
		]
	
def getNX(u0, u1, v0, v1, x0=0,y0=0,z0=0,x1=1,y1=1,z1=1, x_offset=0, y_offset=0, z_offset=0):
	return [
			x0+x_offset,y1+y_offset,z0+z_offset,u0,v0,
			x0+x_offset,y0+y_offset,z0+z_offset,u0,v1,
			x0+x_offset,y0+y_offset,z1+z_offset,u1,v1,
			x0+x_offset,y1+y_offset,z0+z_offset,u0,v0,
			x0+x_offset,y0+y_offset,z1+z_offset,u1,v1,
			x0+x_offset,y1+y_offset,z1+z_offset,u1,v0
		]
	
def getPX(u0, u1, v0, v1, x0=0,y0=0,z0=0,x1=1,y1=1,z1=1, x_offset=0, y_offset=0, z_offset=0):
	return [
			x1+x_offset,y1+y_offset,z1+z_offset,u0,v0,
			x1+x_offset,y0+y_offset,z1+z_offset,u0,v1,
			x1+x_offset,y0+y_offset,z0+z_offset,u1,v1,
			x1+x_offset,y1+y_offset,z1+z_offset,u0,v0,
			x1+x_offset,y0+y_offset,z0+z_offset,u1,v1,
			x1+x_offset,y1+y_offset,z0+z_offset,u1,v0
		]

def getNZ(u0, u1, v0, v1, x0=0,y0=0,z0=0,x1=1,y1=1,z1=1, x_offset=0, y_offset=0, z_offset=0):
	return [
			x1+x_offset,y1+y_offset,z0+z_offset,u0,v0,
			x1+x_offset,y0+y_offset,z0+z_offset,u0,v1,
			x0+x_offset,y0+y_offset,z0+z_offset,u1,v1,
			x1+x_offset,y1+y_offset,z0+z_offset,u0,v0,
			x0+x_offset,y0+y_offset,z0+z_offset,u1,v1,
			x0+x_offset,y1+y_offset,z0+z_offset,u1,v0
		]

def getPZ(u0, u1, v0, v1, x0=0,y0=0,z0=0,x1=1,y1=1,z1=1, x_offset=0, y_offset=0, z_offset=0):
	return [
			x0+x_offset,y1+y_offset,z1+z_offset,u0,v0,
			x0+x_offset,y0+y_offset,z1+z_offset,u0,v1,
			x1+x_offset,y0+y_offset,z1+z_offset,u1,v1,
			x0+x_offset,y1+y_offset,z1+z_offset,u0,v0,
			x1+x_offset,y0+y_offset,z1+z_offset,u1,v1,
			x1+x_offset,y1+y_offset,z1+z_offset,u1,v0
		]

vertices=[]

def getVertices(x,y,z, resource_location, level):
	global vertices
	vertices=[]
	model=models[resource_location.getAsString()]
	face_arrays=[getNY, getPY, getNX, getPX, getNZ, getPZ]
	neighbors=[(x,y-1,z),(x,y+1,z),(x-1,y,z),(x+1,y,z),(x,y,z-1),(x,y,z+1)]
	if model["type"]=="full_cube":
		for face in range(6):
			if level.getBlock(*neighbors[face]).getAsString() in render_data["cutout"] or level.getBlock(*neighbors[face]).getAsString() in render_data["translucent"]:
				texture=model["textures"][face]
				u0=uv[texture][0]/width
				u1=(uv[texture][0]+1)/width
				v0=uv[texture][1]/height
				v1=(uv[texture][1]+1)/height
				for num in face_arrays[face](u0,u1,v0,v1, x_offset=x, y_offset=y, z_offset=z):
					vertices.append(num)
	else:
		for element in model["elements"].values():
			model_custom_uv=element["custom_uv"]
			model_texture_names=element["textures"]
			model_vertices=element["vertices"]
			for face in range(6):
				if level.getBlock(*neighbors[face]).getAsString() in render_data["cutout"] or level.getBlock(*neighbors[face]).getAsString() in render_data["translucent"]:
					texture=model_texture_names[face]
					if model_custom_uv[face]==False:
						u0=uv[texture][0]/width
						u1=(uv[texture][0]+1)/width
						v0=uv[texture][1]/height
						v1=(uv[texture][1]+1)/height
					else:
						u0=model_custom_uv[face][0][0]/width
						v0=model_custom_uv[face][0][1]/height
						u1=model_custom_uv[face][1][0]/width
						v1=model_custom_uv[face][1][1]/height
					x0,y0,z0,x1,y1,z1=model_vertices
					for num in face_arrays[face](u0,u1,v0,v1, x0,y0,z0,x1,y1,z1, x, y, z):
						vertices.append(num)
	return vertices
