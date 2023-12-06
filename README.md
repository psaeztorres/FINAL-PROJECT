# FINAL-PROJECT
## 100 % ELECTRICITY FROM RENOWABLE SOURCES IN SPAIN: A PIPE DREAM OR A REAL POSSIBILITY

![placa solar](images\image1.jpeg)
---
# [LINK TO PRESENTATION](https://public.tableau.com/app/profile/patricia.saez/viz/ELECTRICITYDEMANDGENERATIONINSPAIN/PROJECT?publish=yes)
---
# *Study Objective:*

As we delve into Spain's role as a potential powerhouse for electricity from renewable or non-renewable sources, several critical questions emerge:

Is Spain genuinely on the right trajectory?

Is there a practical tipping point between the increasing demand for electricity and the generation of green or conventional energy?

In this  study, an exploration into the current electricity landscape is conducted, examining each autonomous community's role and the status of renewable and non-renewable projects both in Spain and globally. Join this exploration to assess whether Spain is moving towards a sustainable future or encountering hurdles on the path to achieving 100% electricity from renewable sources.

---
# *Data:*

Queries were conducted on the Red Electrica Española (REE) API to retrieve generation and demand data for the past 10 years. The requests were made for monthly data, categorized by autonomous community (aacc).

For global projects, data was sourced from Global Energy Monitor using the appropriate web page authorization. Given that global projects do not inherently have autonomous communities, a function was developed to establish their respective aacc based on latitude and longitude information obtained from a geojason file.

Upon gathering all the information, Exploratory Data Analysis (EDA) was performed, followed by cleaning and transformation processes. The goal was to standardize all data to common autonomous community names, energy source types, and units.

In accordance with the project's criteria and following REE standards, only the following electricity sources were considered renewable: solar, wind, geothermal, and biomass. Interestingly, hydropower was not classified as renewable, despite potential varying opinions.

Concerning REE data, units were explicitly specified as MWh. However, for project data, units were often undeclared. In cases where unit information was available, it was in MW. To maintain consistency, all project capacity values were assumed to be in MW and then converted to MWh (using 720h/month).

It is crucial to note that, throughout this study, projects have a declared named plate capacity, which has been considered 100 as the real capacity, although this all project's capacity  accurate in every case.

---
# *Analysis:*

### SPAIN CURRENT STATUS

When choosing only renewable sources, it is evident that the demand exceeds the generation. However, as the circular graph illustrates, this is not the case for all autonomous communities (aacc). Some aacc can generate more electricity from renewable sources than their demand.

On the other hand, it is apparent that the demand has not increased in recent years. This information leads us to believe that transitioning to 100% electricity from renewable sources is a real possibility.

The percentage of electricity from renewable sources in 2022 was 44,6% of the demand.

Only 4 autonomous communities (aacc) were able to generate all their electrical demand from renewable sources.

![Autonomous communities situation](images\aacc_situation.png)

### PROJECTS IN SPAIN

The highest number of projects is planned in Castilla-Leon and Aragon, both of which already generate more renewable electricity than their demand. The third autonomous community with the most projects is Catalonia, which also has the highest electricity demand.
 
EXPECTED RENEWABLE ELECTRICITY IN SPAIN

"Active" projects are considered those under construction, in pre-construction, or announced. The total amount of electricity from renewable sources, if all these "active" projects are completed and based on the 2022 demand, unfortunately, is only sufficient for one autonomous community to be "100% renewable," which would be Extremadura. Although renewable electricity would increase, it would not be enough to cover the entire demand.

In the following graphic, each autonomous community (aacc) is represented by three columns. The left columns depict the total demand for the year 2022, the right columns illustrate the total renewable electricity generated in 2022, and the middle column represents the combined result of:

(total renewable electricity generated in 2022) + (electricity generated if all projects were already running).

![Autonomous communities projects](images\aacc_projects.png)

### PROJECTS AROUND THE WORLD

It is evident that most of the "active" projects worldwide are for wind and solar electricity generation, which is really good news. Nevertheless, oil, gas, and coal projects are also considered "active.


<img src="images/world_map.gif" width="800" height="450" />

---
# *CONCLUSIONS:*

1- Electricity demand has not only failed to increase in recent years but has remained steady. The most probable cause is the improvement in energy consumption of equipment, coupled with increased public awareness.

2- Currently, several autonomous communities have the capacity to generate electricity from renewable sources in sufficient quantities to meet their demand.

3- Despite the presence of "active" projects, they are not adequate to meet 100% of Spain's electricity demand.

4- Globally, similar to Spain, the majority of "active" projects focus on solar and wind electricity generation.

5- "Active" projects for electricity generation from sources emitting CO2 persist, especially in Asia.

---
# *NEXT CHALLENGES:*

Find how to store electricity efficiently

![placa solar](images\image2.jpeg)