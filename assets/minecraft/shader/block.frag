#version 120

varying vec2 vTexCoord;

uniform sampler2D texture;
uniform bool cutout;

void main(){
	vec4 texColor = texture2D(texture, vTexCoord);
	if (cutout && texColor.a < 0.5){
		discard;
	}
	gl_FragColor=vec4(texColor.rgb, texColor.a);
}
