rm -r build
rm -r dist
python -m PyInstaller --name 'DataFixer' --onefile --collect-all net.minecraft.world.block --collect-all net.minecraft.resources net/minecraft/resources/DataFixer.py