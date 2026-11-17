#version 120

attribute vec3 position;
attribute vec2 texCoord;
attribute vec3 aNormal;

varying vec2 vTexCoord;
varying vec3 fragPos;
varying vec3 lightPos;
varying vec3 normal;

uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;

void main() {
	float radius=5000.0;
	float lightAngle=1;
	lightPos=vec3(
		0.0,
		radius * sin(lightAngle),
		radius * cos(lightAngle * 3.14149265)
	);
	fragPos=vec3(model * vec4(position, 1.0));
	normal=aNormal;
    gl_Position = projection * view * model * vec4(position, 1.0);
    vTexCoord = texCoord;
}
