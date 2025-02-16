
from room import Room

class Game_World():
    def __init__(self):
        self.world = {}
        self.current_location = None
        self.populate_world()

    def populate_world(self):
        docks_esrel = Room("[Esrel Docks]", "You notice the hustle and bustle of the Esrel docks. Glancing around you can see numerous boats moored, rocking to the waves of Lake Esrel. Fresh fish and nature raise to meet you. Along the waters edge you can see a stretching sand lake front and in the distance standing among trees you see stone walls.")
        lake_esrel = Room("[Lake Esrel]", "Water laps at your feet as you peer out across Lake Esrel. The sound of boats echo out aross the busy water with sights of fishing boats on the horizon. The occasional visitor comes and goes heading to and from Esrel and the docks.")
        path_esrel = Room("[Path to Esrel]", "A faint cobblestone path navigates from north and south, speckled with grass and moss and forest creeping to the edges of the pathway. The echos of a port are distant with village life intertwined to the North.")

        docks_esrel.set_exits({"north": path_esrel, "east": lake_esrel})
        path_esrel.set_exits({"south": docks_esrel, "southeast": lake_esrel})
        lake_esrel.set_exits({"west": docks_esrel, "northwest": path_esrel})
        self.current_location = docks_esrel
        self.world = {
            docks_esrel.name: docks_esrel,
            path_esrel.name: path_esrel,
            lake_esrel.name: lake_esrel,
        }
    
    def set_world_location(self, room, input):
        self.current_location = self.world[room.name].exits[input]

    def get_current_location(self):
        return self.current_location
    
    def get_description(self):
        return self.current_location.get_description()