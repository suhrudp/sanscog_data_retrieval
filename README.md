# sanscog_data_retrieval

Developed with Pradipto Mondal - https://github.com/pradipto111

A data retrieval application made using Python and Flask; with its interface written in html and styled using css.

While working at the Centre for Brain Research, Indian Institute of Science between June to August 2023, there was a dire need to develop a data retrieval app to efficiently access the huge corpus of data which is bound to exponentially grow in the next 10 years. Hundreds of man-hours were spent in sifting through 10+ excel sheets with 300-1500 columns per sheet, matching participant IDs, and getting 15-20 variables for the final statistical analysis. Big multinational companies such as Infosys were willing to make a customized app with a similar functionality for data retrival and collection at source. However, considering the time required to develop such an application along with a yearly subscription charge, we deciced to take matters into our own hands and build such an application.

PROBLEM STATEMENT:
As of May 2023, the Srinivasapura Aging, Neurosenescence, and Cognition (SANSCOG) study dataset comprises of different categories of data including Socio-Demographic, Clinical, Nursing, Cognitive, Blood Biochemistry, MRI and ApoE. Combined, they account for 4241 columns. This makes data extraction a tedious task for the researchers who want to leverage this huge corpus. Hence, there is a burning need for an extraction procedure which is easy to use, intuitive and saves hours of manual work.

METHODOLOGY:
We create a web based application based on Flask, which is an open source Python package for backend development. The frontend was created using HTML/CSS and Bootstrap. The web app loads the source dataset in a dataframe and dispenses the required columns as requested by the user.

USER INTERFACE:
(1) The landing page of the application is a login page(which ensures data security and only approved researchers to use the facility.
(2) Once logged in, the home page opens which contains the different categories of data to select from. It also consists of a dropped
down menu which consists of the currently selected columns for download ( empty by default).
(3) The user must click on the required category, which further opens a new page consisting of the column subcategories and names which can be selected using a slider button as required.
(4) Once the user confirms the selected columns, they can be downloaded in .xlsx format with the click of a single button after entering the filename.

FUTURE DIRECTIONS:
(1) We aim to further expand this to build an unified application encompassing data collection as well. This will be a seamless workflow application with user-friendliness and an elegant UI at the forefront.
(2) The data corpus must be hosted in an SQL based database for faster retrieval, maintenance and scalability, and synchronised function of Srinivaspura on-site data collection centres and CBR Researchers.

Please note - the data provided is fictional and NOT real patient data. Patient and sample IDs have been changed.
