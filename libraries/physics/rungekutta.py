from vectors import vadd, vscale

def runge_kutta(f, state, dt = 0.01):
    '''
    Apply the Runge-Kutta approximation technique
    to a state vector for a single time step.

    f -- a function that takes a state vector
        and returns the instantaneous time derivative
        of each component
    state -- the existing state vector. Simply a list
        of floats with every variable needed in the system.
    dt -- the time delta

    returns the next state vector after
    one time step
    '''
    a = f(state)
    b = f(vadd(state, vscale(dt / 2.0, a)))
    c = f(vadd(state, vscale(dt / 2.0, b)))
    d = f(vadd(state, vscale(dt, b)))

    #Apply the weights dt/6 * (a + 2b + 2c + d)
    a = vscale(dt / 6.0, a)
    b = vscale(dt / 3.0, b)
    c = vscale(dt / 3.0, c)
    d = vscale(dt / 6.0, d)
    return vadd(state, a, b, c, d)
