
SUPPORTED_SOLVERS = ["flipsolver", "pyrosolver_sparse"]

PYRO_PARM_SIMULATION = ["divsize",
    "calcspeed",
    "timescale",
    "viscosity",
    "tempdiffusion",
    "tempcooling",
    "temperature0",
    "temperature1",
    "buoyancylift",
    "gravaccel",
    "gravdir"]

PYRO_PARM_FLAMES = [
    "flames_lifespan",
    "soot_doemit",
    "soot_amount",
    "soot_mergemethod",
    "soot_controlrange",
    "soot_controlramp",
    "temperature_doadd",
    "temperature_amount",
    "temperature_mergemethod",
    "temperature_pullstrength",
    "temperature_controlrange",
    "temperature_controlramp",
    "div_doadd",
    "div_amount",
    "div_controlrange",
    "div_controlramp"]

PYRO_PARM_SHAPE = [
    "dissipation",
    "dissipation_controlfield",
    "dissipation_controlrange",
    "dissipation_controlramp",
    "disturbance",
    "disturbance_thresholdfield",
    "disturbance_threshold",
    "disturbance_mode",
    "disturbance_refscale",
    "disturbance_blocksize",
    "disturbance_pulselength",
    "disturbance_controlfield",
    "disturbance_controlrange",
    "disturbance_controlramp",
    "shredding",
    "shredding_field",
    "shredding_range",
    "shredding_blocksize",
    "shredding_controlfield",
    "shredding_controlrange",
    "shredding_controlramp",
    "turbulence",
    "turbulence_noisetype",
    "turbulence_swirlsize",
    "turbulence_grain",
    "turbulence_pulselength",
    "turbulence_influencefield",
    "turbulence_infthreshold",
    "turbulence_controlfield",
    "turbulence_controlrange",
    "turbulence_controlramp"
    "wind_strength",
    "wind_direction"]    

PYRO_PARM_COLOR = [
    "color_dissipation",
    "color_diss_onlydecayalpha",
    "color_diss_controlfield",
    "color_diss_controlrange",
    "color_diss_controlramp",
    "color_blur",
    "color_blur_radius",
    "color_blur_filter",
    "color_sharpening",
    "color_sharpen_radius",
    "color_sharpen_threshold"]


PYRO_PARM_ADVANCED = [
    "minimalsolve",
    "opencl",
    "minimumsubsteps",
    "substeps",
    "cflcond",
    "quantize",
    "framesbeforesolve",
    "singlevcycle",
    "adv_scheme",
    "adv_clampvalues"]    


FLIP_PARM_SIMULATION = [
    "particlesep",
    "radiusscale",
    "gridscale",
    "collisionsep",
    "timescale",
    "minimumsubsteps",
    "substeps",
    "cflcond",
    "partcflcond",
    "quantize"]


FLIP_PARM_MOTION = [
    "doforces",
    "volumeoverrideattrib",
    "underresolved",
    "collision",
    "tankcollision",
    "killoutside",
    "usephysparms",
    "doid",
    "doage",
    "doreapparticles"]    
