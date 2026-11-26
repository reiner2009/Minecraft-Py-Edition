#version 120

varying vec2 texCoord;

uniform sampler2D texture;

void main() {
	if (texture2D(texture, texCoord).a == 0.0){
		discard;
	}
    gl_FragColor = texture2D(texture, texCoord);
}
