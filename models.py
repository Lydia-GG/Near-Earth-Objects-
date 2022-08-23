from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:

    def __init__(self, designation, name=None,
                 diameter=float('nan'), hazardous=""):

        self.designation = designation
        self.name = None if name == "" else name
        self.diameter = float('nan') if diameter == "" else float(diameter)
        self.hazardous = True if hazardous == 'Y' else False

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""

        return f'{self.designation} {self.name}'

    def __str__(self):
        """Return `str(self)`."""

        self.hazardous = f"is" if self.hazardous else "is not"
        return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km \
          and {self.hazardous} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of \
          this object."""
        return (f"NearEarthObject(designation={self.designation!r}, \
          name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:

    def __init__(self, designation, time, distance, velocity):

        self._designation = designation
        self.time = cd_to_datetime(time)  
        self.distance = float(distance)
        try:
            self.velocity = float(velocity)
        except ValueError:
            self.velocity = float("nan")

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):

        # build a formatted representation of the approach time.
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""

        return f"On {self.time}, {self._designation} approaches Earth at a \
          distance of {self.distance:.2f} au and a velocity of \
            {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of \
          this object."""
        return (f"CloseApproach(time={self.time_str!r}, \
          distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
