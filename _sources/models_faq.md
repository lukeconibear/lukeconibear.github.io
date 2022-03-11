# Models FAQ

Here, I'm mainly referring to numerical atmospheric models that are used for simulating air quality, weather, and climate.

## What's inside climate models?

Paul Ullrich explains climate models [here](https://youtube.com/playlist?list=PL_cuIb7hx5lihu3Wq605u6kVGltXgEfDt). Guy Brasseur gives an overview of atmospheric chemistry modelling [here](https://youtu.be/t-6ntWF3B8c) and [here](https://youtu.be/tc7vGe1efrA). Tim Palmer explains how to deal with uncertainty [here](https://youtu.be/ed4p7JYMYKs).  

## Are any models (and their output) openly available?

Yes.

Some examples of models:

- [Weather Research and Forecasting (WRF) model](https://github.com/wrf-model/WRF)  
- [Goddard Earth Observing System (GEOS) Chem model](https://github.com/geoschem/geos-chem)  
- [Community Earth System Model (CESM)](https://github.com/ESCOMP/CESM)  
- [Energy Exascale Earth System model](https://github.com/E3SM-Project/E3SM)  

And some output data:

- [Model output](https://esgf-data.dkrz.de/search/cmip6-dkrz/) from all the Coupled Model Intercomparison Project (CMIP) 6 models used in the IPCC 6th Assessment Report  
- [NASA Earth Data](https://search.earthdata.nasa.gov/search)  

## What are the well-known models?

- [ECMWF, Integrated Forecasting System (IFS)](https://www.ecmwf.int/en/research/modelling-and-prediction)  
- [UK Met Office, Unified Model (UM)](https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model/index)  
- [NCAR, Community Earth System Model (CESM)](https://www.cesm.ucar.edu/models/)  
- [NASA, Goddard Institute for Space Studies (GISS) model](https://www.giss.nasa.gov/projects/gcm/)  

## Are the models accurate?  

It's helpful to separate the core model, scenario, and phenomena.  

The scenarios are possible future decisions and actions. As this future knowledge is unknowable in advance, their use is limited. Some phenomena are not well suited for long-term prediction. However, independent of these, the skill of different core models varies a lot.  

For the core model, the fundamentals are similar, in that to predict the weather they need to accurately simulate atmospheric dynamics, physics, chemistry, etc. These predictions are then constantly evaluated against reality (at least for short-term phenomena), so the model skill can be determined.  

Many of the best models from top institutions perform very well (e.g., ECMWF, UK Met Office, NCAR, NASA). For weather, the accuracy of <10 day forecasts has improved a lot over the last 40 years ([paper](https://www.nature.com/articles/nature14956)). For climate, the accuracy of broad general effects, such as global temperature anomalies, is not too bad (e.g., [paper](https://www.pnas.org/node/900558.full)). However, this same paper points out well that the models struggle with specifics (e.g., regional effects, extremes, etc.) and that there are many ways the models can substantially improve.  

*Overall, this continual error correction and stringent testing against reality has gone on for decades for weather models, and is why I think that in general they're pretty good scientific tools.*

## Can we find out how sensitive the climate is to emissions without using scenarios?

Yes.  

We can remove the dependency on future knowledge by looking at climate sensitivity. This is an emergent metric that estimates how much surface warming there would be from a doubling of CO2 emissions (i.e., how sensitive is the climate to emissions). This is then split into a transient climate response (TCR) showing short-term response and an equilibrium climate sensitivity (ECS) showing long-term response.  

The climate sensitivity turns out to be a skewed probability distribution with a thin tail at higher temperatures. Recent estimates ([IPCC AR6](https://www.carbonbrief.org/guest-post-why-low-end-climate-sensitivity-can-now-be-ruled-out)) find the TCR mean is 1.8 degrees and the ECS mean is 3 degrees. This is probably the best guide for decisions we currently have. Tim Palmer explains climate sensitivity and how to use it to make decisions [here](https://youtu.be/qXNaNXwWvmk).  
