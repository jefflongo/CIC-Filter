class CICDecimatorFilter:
    """Create a CIC decimator filter

    R: decimation factor
    N: number of integrator/comb stages
    """

    class Integrator:
        def __init__(self) -> None:
            self.y_prev: int = 0

        def update(self, x: int) -> int:
            y: int = x + self.y_prev
            self.y_prev = y
            return y

    class Comb:
        def __init__(self) -> None:
            self.x_prev: int = 0

        def update(self, x: int) -> int:
            y: int = x - self.x_prev
            self.x_prev = x
            return y

    def __init__(self, R: int = 2, N: int = 1) -> None:
        self.R = R
        self.N = N
        self.integrators: list = [self.Integrator() for _ in range(N)]
        self.combs: list = [self.Comb() for _ in range(N)]

    def update(self, samples: list) -> list:
        out: list = []
        normalization: int = self.R**self.N

        for i in range(len(samples)):
            # pass input through integrators
            z: int = samples[i]
            for stage in range(self.N):
                z = self.integrators[stage].update(z)

            # decimate
            if i % self.R == 0:
                # pass decimated input through combs
                for stage in range(self.N):
                    z = self.combs[stage].update(z)

                out.append(z / normalization)

        return out
