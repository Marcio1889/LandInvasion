from code.Background import Background
from code.const import WIND_WIDTH


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'ImageFP':
                list_bg = []
                for i in range(11): # configurando a exibição do fundo da fase 1
                    list_bg.append(Background(f'ImageFP{i}',(0,0)))
                    list_bg.append(Background(f'ImageFP{i}', (WIND_WIDTH, 0)))

                return list_bg