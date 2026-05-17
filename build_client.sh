rm -r build
rm -r dist
python -m PyInstaller --name 'Minecraft' --windowed --onefile --icon 'icon.icns' --add-data "assets:assets" --add-data "data:data" --collect-all net.minecraft --collect-all OpenGL net/minecraft/client/Main.py
cp -R icon.icns dist
cd dist
create-dmg --volname "Minecraft" --volicon "icon.icns" --window-pos 0 0 --window-size 1680 1050 --icon-size 256 --icon "Minecraft.app" 175 120 --hide-extension "Minecraft.app" --app-drop-link 425 120 "dist/Minecraft.dmg" "dist/dmg/"