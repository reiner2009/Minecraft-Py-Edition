#version 120

varying vec2 vTexCoord;
varying vec3 fragPos;
varying vec3 normal;
varying vec3 lightPos;

uniform sampler2D texture;
uniform bool cutout;

void main(){
	vec4 texColor = texture2D(texture, vTexCoord);
	if (cutout && texColor.a < 0.5){
		discard;
	}
	vec3 n = normalize(normal);
	vec3 lightDir=normalize(lightPos - fragPos);
	float ambient=0.2;
	float diff = max(dot(n, lightDir), 0.0);
	vec3 color=texColor.rgb * (ambient + diff * 0.8);
	gl_FragColor=vec4(color, texColor.a);
}
