import itertools
import re

NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"

TAKE = "take"
DROP = "drop"

INV = "inv"

SAND = "sand"
COIN = "coin"
JAM = "jam"
ASTROLABE = "astrolabe"
ORNAMENT = "ornament"
WEATHER_MACHINE = "weather machine"
FOOD_RATION = "food ration"
CAKE = "cake"

USEFUL_ITEMS = (SAND, COIN, JAM, ASTROLABE, ORNAMENT, WEATHER_MACHINE, FOOD_RATION, CAKE)
LIGHT_ITEMS = (JAM, ASTROLABE, ORNAMENT, WEATHER_MACHINE, FOOD_RATION)


class Droid:

    def __init__(self, program):
        self.program = program

    def get_password(self):

        # Consume initial "Hull Breach" output
        self.program.get_ascii()

        self.take_everything_to_security_checkpoint()
        self.check_individual_items()
        return self.check_combinations_of_light_items()

    def take_everything_to_security_checkpoint(self):

        # Hull Breach → Passages
        self.south()
        self.west()
        self.north()
        self.north()
        self.east()

        self.take(ASTROLABE)

        # Passages → Warp Drive Maintenance
        self.west()
        self.south()
        self.south()

        self.take(SAND)

        # Warp Drive Maintenance → Arcade
        self.east()

        self.take(FOOD_RATION)

        # Arcade → Navigation
        self.north()
        self.north()
        self.east()

        self.take(COIN)

        # Navigation → Crew Quarters
        self.west()
        self.south()
        self.east()
        self.south()
        self.west()
        self.west()

        self.take(JAM)

        # Crew Quarters → Science Lab
        self.east()

        self.take(ORNAMENT)

        # Science Lab → Hallway
        self.east()

        self.take(WEATHER_MACHINE)

        # Hallway → Corridor
        self.north()

        self.take(CAKE)

        # Corridor → Security Checkpoint
        self.east()
        self.east()
        self.east()

        print(self.inv())

        # Drop everything
        for item in USEFUL_ITEMS:
            self.drop(item)

        print(self.inv())

    def check_individual_items(self):

        for item in USEFUL_ITEMS:

            self.take(item)

            # Go to pressure-sensitive floor
            response = self.south()

            # Check response
            if "are heavier" in response:
                print("%s: too light" % item)
            elif "are lighter" in response:
                print("%s: too heavy" % item)

            self.drop(item)

    def check_combinations_of_light_items(self):

        for num_items in range(2, len(LIGHT_ITEMS) + 1):

            for items in itertools.combinations(LIGHT_ITEMS, num_items):

                # Take items
                for item in items:
                    self.take(item)

                # Go to pressure-sensitive floor
                response = self.south()

                # Check response
                if "You may proceed" in response:
                    match = re.search("typing (\\d+) on", response)
                    return match.group(1)

                # Drop items
                for item in items:
                    self.drop(item)

    def north(self):
        return self._send_command(NORTH)

    def south(self):
        return self._send_command(SOUTH)

    def east(self):
        return self._send_command(EAST)

    def west(self):
        return self._send_command(WEST)

    def take(self, item):
        return self._send_command(TAKE + " " + item)

    def drop(self, item):
        return self._send_command(DROP + " " + item)

    def inv(self):
        return self._send_command(INV)

    def _send_command(self, command):
        return self.program.send_ascii_and_get_reply(command)
