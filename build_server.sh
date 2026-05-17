rm -r build
rm -r dist
python -m PyInstaller --name 'MinecraftServer' --onefile --collect-all net.minecraft.util.logger net/minecraft/server/Main.py