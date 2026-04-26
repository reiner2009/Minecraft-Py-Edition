from net.minecraft.client.Client import*
import net.minecraft.util.logger.Logger as logger

def load_texture(path, isSkin=False):
    logger.set_environment("Client")
    try:
        surface = pygame.image.load(path).convert_alpha()
        surface = pygame.transform.flip(surface, False, True)
        data = pygame.image.tostring(surface, "RGBA", 1)
        width, height = surface.get_size()
        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGBA,
            width,
            height,
            0,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            data
        )
        logger.info("Loaded texture " + path)
        if isSkin:
            return tex_id, width, height
        else:
            return tex_id
    except:
        logger.error("Falied to load texture " + path)
        surface = pygame.image.load("assets/minecraft/textures/error.png").convert_alpha()
        surface = pygame.transform.flip(surface, False, True)
        data = pygame.image.tostring(surface, "RGBA", 1)
        width, height = surface.get_size()
        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGBA,
            width,
            height,
            0,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            data
        )
        return tex_id
