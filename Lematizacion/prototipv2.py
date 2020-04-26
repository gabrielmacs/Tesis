# https://medium.com/@yeralway1/primeros-pasos-en-nlp-con-spacy-un-vistazo-general-734686843a57

import spacy
from spacy import displacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")
texto = """



Abstract

Purpose ñ This purpose of this paper is to understand the environmental impacts of stakeholder-driven sustainable purchasing policies in institutional settings.

Design/methodology/approach ñ The research is framed using stakeholder and life cycle assessment (LCA) theories. The study uses a multi-method approach. Starting with interviews to understand the breadth of sustainability issues and significant food purchases facing institutional purchasing managers, the authors subsequently perform LCA of these various policies using the most popular food item in different categories. Findings ñ From the interview results, the authors found that food purchasers focus predominately on cost, thus, are committed to food and packaging reduction. They are driven to buy local foods based on their consumer stakeholders but share their commitment to buying local products if the cost is appropriate. In the LCA of popular food items in multiple scenarios, avoiding food waste of various forms had significantly higher carbon emissions savings than packaging reduction or transportation minimizing (buy local) strategies.

Research limitations/implications ñ The sample relied solely on the perceptions of institutional purchasing managers in university dining services. Future research should involve collecting data from other stakeholder groups such as the customers themselves, institutional leaders, and in other types of institutional settings such as hospitals and government agencies.

Practical implications ñ The research provides managers with insights concerning the trade-offs between different sustainability objectives. In particular, findings show that reducing waste related animal protein has a bigger impact on environmental performance than many other popular sustainability objectives such as buying local or reducing packaging waste.

Social implications ñ The paper focuses on the purchasing trade-offs of buying local vs national food products, different packaging solutions, and food waste generation. These decisions offer some social benefits (improve the economic situation for local farms vs consolidated food producers) as well as multiple environmental benefits.

Originality/value ñ The paper presents new findings on the sustainability purchasing priorities of stakeholders in institutional food settings and subsequent LCA of those policies to show which might have the most environmental impact.

Keywords Sustainability, LCA, Packaging, Purchasing, Supply chain management, Food waste Paper type Research paper

Like many involved with purchasing, institutional food purchasers face multiple stakeholders with competing agendas. Institutional purchasers often confront more stakeholder pressure than those in other industries as institutions are often a function of government or public service such as education, hospitals, military and jails thus garner political attention. Regardless of whether it is a public or private institution, the institutional

The authors wish to thank the Oregon Transportation Research and Education Consortium (OTREC) for grant support with this research.



food service area has highly committed stakeholders such as students, their parents, patients and their families, health care practitioners, staff, government, donors and various advocacy groups. Thus, it is no surprise that sustainability issues have increasing become an important area for institutional food purchasing. This trend is reflected in the multiple sustainability-related food purchasing rating and certification schemes for institutions such as: sustainability tracking, assessment and rating systems (STARS, 2015), LEED sustainable food purchasing (LEED, 2012), and Health Care Without Harm (2016). A structural issue that helps complicate matters is that many institutions outsource their food production and service activities to food service management (FSM) or catering companies. These companies are highly concentrated; the biggest players, Compass Group, Aramark, and Sodexo, garner more than 78 percent of sales of top 50 companies (Food Management, 2014). Compass Group í s division, Bon AppÈtit, uses sustainable purchasing as a competitive advantage to win international corporate accounts such as Google, Facebook, etc. And with increasing stakeholder pressures on purchasing sustainable food, more institutions must now grapple with adopting some kind of sustainable food purchasing policy. Sustainability criteria can emanate from institutional organizations such as STARS (2015) for universities or from various stakeholders within the institutional setting. Criteria run the gamut from explicit purchasing requirements such as local purchases from specific geographic locations and sustainably certified product to additional requirements related to food package recycling, food composting, and other food service waste issues. Purchasers must decide which areas to emphasize, where to commit resources and how to measure sustainability outcomes.

From the purchaser í s perspective, the agent juggles the pressure to meet financial performance criteria from their host institution or employer FSM, contractual obligations from major food suppliers and stakeholders í interests. Thus, this research has multiple objectives:

(1) understand institutional food purchasers í perspectives on sustainability, their

priorities, challenges and impact of various stakeholders;

(2) establish representative examples of most popular institutional food items and

sustainability decisions around those items;

(3) evaluate the alternative purchasing options for the most popular items and the

resulting environmental impacts; and

(4) suggest purchasing policies and strategies which better address the concerns of the

different stakeholder groups.

The purpose of this study is to understand the environmental impacts of stakeholder-driven sustainable purchasing policies in institutional settings. The research is framed using stakeholder theory and life cycle assessment (LCA) and uses a two-stage approach to provide empirical evidence. First, we perform in-depth field interviews with institutional purchasers to understand the role of stakeholders in sustainable food policy and decision making as well as the significant food purchase categories and their associated environmental issues. In the second state, we perform LCA analysis of these various policies using the most popular food item in each of three key institutional purchasing categories (protein, fresh produce and value-added produce). The paper goes beyond previous research by not only looking at these policies from the purchaser í s perspective and their evaluation of stakeholder priorities but actually measuring the environmental impact of key institutional food items purchased under different stakeholder-driven sustainability policies. From these results, we propose potential improvements that could address multiple stakeholders í concerns simultaneously. This research addresses a gap in operations and supply chain research about how behavioral and human factors influence sustainability particularly how

Institutional sustainable purchasing

priorities



firms respond to different stakeholders, their concerns, and the actual environmental impact of different policies (Klassen and Vereecke, 2012; Walker et al. , 2014).

In the next section, we will cover the related literature on stakeholders and sustainable purchasing practices followed by the research on environmental outcomes related to food, waste, and packaging decisions. This is followed by the description of our two-stage approach, analysis and results. We conclude with a discussion on the results and implications of the research for institutional purchasers and policy makers.

Literature review

In this section, we review several streams of research and propose hypotheses. We start by looking at the relevant research on stakeholder theory. We then consider the previous work in our context area, food service and sustainable purchasing policies. Next, we discuss the research connecting food purchasing policy and environmental performance measured by transportation metrics and LCA. Finally, we look at the previous work on the environmental impacts of food packaging and waste.

Stakeholder theory

Stakeholder theory suggests that a firm should go beyond shareholders í interests to include employees, suppliers, and local communities because all of these groups are important to the success of a business (Freeman, 1984). Stakeholders exert pressure on companies to diminish negative effects (Sarkis et al. , 2010, 2011) and firms respond by developing and reconfiguring capabilities to gain social legitimacy and performance improvement (Mitchell et al. , 1997; Parmigiani et al. , 2011; Zorzini et al. , 2015). Generally, stakeholders groups can be categorized as regulatory, internal primary, external primary, and external secondary (Wu et al. , 2014).

More specifically looking at different stakeholders í roles in influencing purchasing practices, Carter and Carter (1998) found that downstream members of the supply chain influence environmental purchasing practices. Several authors have looked at the role of management support on environmental purchasing practices (Carter et al. , 1998; Drumwright, 1994; Narasimhan and Carter, 1998). Others have examined the initiatives of individual employees and environmental purchasing practices (Drumwright, 1994; Kopicki et al. , 1993). Carter and Jennings (2004) created a purchasing social responsibility (PSR) metric including environment as well as social issues and found a positive relationship between PSR and three stakeholder areas: top management support, employee initiative and customer pressures.

As independent variables, the institution and its customer values may align or differ on various purchasing and waste reduction practices (Fawcett et al. , 2008; Lamming et al. , 2004; Bartlett et al. , 2007). Similarly, the third-party buyer and organization may have the same alignment issues (Lee et al. , 2007). These differing perspectives would affect both the development and implementation of policies along with the subsequent changes in local purchasing and waste reduction.

Food service and sustainable purchasing policies

Typically, in institutional environments, sustainable food purchasing policies are driven either by internal stakeholders and customers (administration, students and parents, staff, patients, their families, etc.) or by special interest groups. One of the most popular sustainability policies initiated by stakeholders of public institutions is the local food procurement policy. In US school, an example is the National Farm-to-School Network (FSN) program. Funded by government agencies, grants, and voter initiatives, FSN procurement policies ask for a certain minimum purchasing commitment from local producers



(National Farm-to-School Network, 2016). Student and parent stakeholders believe that these purchases will build a more sustainable local food system, support local agriculture by providing a large, stable market for producers, and reduce greenhouse gas emissions by transporting food from shorter distances. Researchers indicate that this type of procurement policy has gained momentum for public institutions not only in the USA but also in countries like Italy, Britain, and Canada and that it particularly resonates with end consumers (Brown, 2003; MacLeod and Scott, 2007).

Institutional food purchasing agents, on the other hand, face fiscal and structural challenges to implementing these policies. Purchasing agents are either given a fixed amount of money per person served or cost is a significant constraint in the food purchase decision (Devi et al. , 2010; Izumi et al. , 2010; MacLeod and Scott, 2007). Thus, any policy that potentially lowers costs would be more favorably perceived by the agent. For example, Izumi et al. (2010) found that school purchasing professionals were motivated to buy locally grown food not only because the students liked it, but also because the price was right. Bergstrˆm et al. (2005) showed that purchasers are dependent on corporate policy when it comes to environmental considerations related to food, thus, are mainly guided by business parameters with respect to price, quality and service. Other examples of sustainability- related institutional food policies that have been shown to reduce costs are those that encourage pre-consumer waste reduction (i.e. avoiding spoiled or excess product) and disposal cost reduction (i.e. post-consumer, preparation, and packaging waste). In their study of school food service operations, Hollingsworth et al. (1995) found several waste reduction food purchasing strategies that significantly reduced both food and packaging waste costs. In conclusion, the previous research about food policy and stakeholders would support the following hypotheses:

H1. Institutional purchasing agents prioritize sustainability policies that support

cost control.

H2. Institutional food consumers prioritize sustainability policies that support local

purchasing.

Food purchasing policy and environmental performance

Given the amount of stakeholder interest in sustainable food purchasing in institutions, how do these policies actually improve the institution í s environmental performance While certain policies enjoy enormous stakeholder support, do they actually perform better environmentally relative to the less attention grabbing policies such as packaging changes and waste reduction In this paper, we focus particularly on the environmental or LCA as an outcome measure.

LCA is widely used method to assess the environmental impacts and resources used throughout the life cycle of a product or process. The method covers raw material acquisition, production use, and end-of-life phases (Finnveden et al. , 2009). LCA was originally proposed in the 1990s and has since been used to analyze products and processes worldwide. Today, there are recognized standards for the technique from the Intergovernmental Panel on Climate Change (2009) and International Standards Organization (International Organization for Standardization (ISO), 2009). While LCA can apply to every resource used in the process, in this paper, we are concerned with measuring greenhouse gas emissions particularly carbon dioxide emissions, often referred to as the ì carbon footprint. î

Rising concern about the environmental impact of food transportation has led some FSM firms to implement policies and practices that reduce their transportation carbon footprint (Bauccio and Halwell, 2005). Tukker (2006) identifies food as one of the top-three

Institutional sustainable purchasing

priorities


contributors to the environmental impact in society with food transportation, as a major part of that impact. The centralization of buying, globalization, and consolidation of the food industry and increased usage of regional distribution centers have all contributed to the escalation of food transportation over the past 30 years (Finney, 2006). The concept of ì food miles î is used to contrast local and global food supply systems (Pirog, 2004). Food miles can provide a relative indicator of the amount of energy or fuel used to transport from farm to consumer, with less ì food miles î signaling lower transportation fuel usage, cost, and greenhouse gas emissions. Others argue that the low food miles focus in many cases may not correlate with lower emissions overall. For some product í s LCA, emissions from production and manufacturing are more significant than transportation emissions; non-local industrial scaled farms could grow crops better suited to their region using less energy per item and growing more food on less land (Desrochers and Shimizu, 2012; McWilliams, 2009). The institutional sector requires frequent and lengthy trips by food growers and producers to hubs in a complex food distribution network that contribute significantly to global carbon dioxide emissions (Horrigan et al. , 2002). Increasingly, these businesses are assessing the impact of their purchasing decisions on their carbon footprints (Min and Galle, 2001). Purchasing decisions have complex implications for the environment based on the mode of transportation employed, the corresponding packaging used to transport the goods, and the resulting waste and disposal transportation. Thus, we propose the following hypothesis:

H3. Policies that encourage local procurement for high-demand institutional foods will

generate lower transportation emissions than the mainstream alternative.

Food packaging

Various researchers have examined the relationship between purchasing decisions around packaging and the potential impact on waste generation, environment, and resource recycling and recovery (Carter et al. , 2000; Min and Galle, 2001). Institutional food comes in multiple forms and packages: plastic, glass, metal and paper containers and protective coverings. The vast majority of the items will also come in a cardboard box. These items have different environmental impacts. Sonesson et al. (2009) found on the one hand, packaging waste makes up a large part of landfills with plastics and paper; on the other hand, packaging reduces food waste, which has been shown to greatly contribute to greenhouse gas emissions and can be used to improve transportation efficiency by improving weight to volume ratios of products. Packaging waste makes up one-third to half of the US landfills (Environmental Protection Agency, 2016). In the EU, 3.3 percent of all GHG emissions come from waste (Eurostat, 2015). Given the above research, we propose the following hypothesis:

H4. Policies that encourage reduced packaging for high-demand institutional foods will

generate lower emissions than the mainstream alternatives.

Food waste

Food waste contributes to environmental performance via two paths, disposal and embedded emissions. If an institution throws food in the dumpster, the wasted food degrades in the landfill and generates CH 4 (methane). More significantly, wasted

food contains the embedded emissions associated with production, processing, transportation, storage and cooking. Since between 30 and 50 percent of all food is wasted in the journey from field to fork, this waste is a major source of environmental concern (Bloom, 2010; Institute of Mechanical Engineers, 2013; McWilliams, 2009). According to recent studies, the energy embedded in wasted food represents approximately



2 percent of annual energy consumption in the USA (CuÈllar and Webber, 2010). In an institutional setting, food can be wasted before getting to the final consumer either before preparation (over-buying and lack of attention to inventory), during preparation (trimming excess and mistakes), and after preparation (over-supply or inability to recycle prepared product for another meal). The consumer contributes to waste by different behaviors, ì eyes are bigger than stomach î syndrome and other reasons for not finishing the food on their plate or tray. Very little data exist on the amount of food wasted in institutions. A study of food losses in four food service institutions in Sweden showed that about one-fifth of the food was lost: 4 percent during storage and preparation, 6 percent during serving including discarded leftovers, and 10 percent from plate waste (Engstrˆm and Carlsson-Kanyama, 2004). In another study at a US college cafeteria, 0.41 pounds of food was wasted for every meal served, equally split between plate waste and cafeteria preparation/serving (Bolak et al. , 2008). Venkat (2011) found that production and processing emissions accounted for 68.6 percent of all wasted food emissions with packaging, distribution and retail accounting for 10 percent or less. Animal products had a disproportionate climate change impact because of their relatively high emission footprints from production. They make up about 30 percent of all wasted food by weight, but account for nearly 57 percent of the emissions. On the other hand, grains, vegetables and fruits make up 56 percent of the waste, but contribute just 31 percent of the emissions due to their relatively low emission footprints:

H5. Policies that discourage food waste overall will generate more emissions savings

than transportation and packaging reduction policies.

H6. Policies that discourage animal product waste will generate more emissions savings

than other food waste and packaging reduction policies.

In summary, while previous research has looked at certain aspects of sustainable purchasing from a stakeholder perspective, there is limited research examining the demands of different food purchasing stakeholders, potential policies to address those demands, and their resulting environmental impacts.

Methodology

In this section, we cover both phases of the data collection and analysis. The first phase involved in-depth institutional interviews and secondary data collection to assess institutional practices and perceptions of various stakeholder priorities around these practices. Based on these results, a selected group of the popular practices and food products were then analyzed with LCA in second phase.

Phase 1: interviews

The goal of this phase was to gather information from institutional purchasing agents and their supply chain partners about key concerns, policies, and important food categories. We began by conducting 20 semi-structured interviews with institutional FSM purchasing managers, supply chain partners, and stakeholder representative groups from the Northwestern USA (see the Appendix). The purchasing managers were selected based on size, institution, public/private, and management type. The resulting seven purchasing managers came from three hospitals and four universities. The interviews were supplemented by information gathering and clarification interviews from sustainability directors from the two largest US broad-line food distributors, five local produce distributors, two regional FSM companies, and four NGO food service stakeholder groups. These interviews started with general demographic questions about the respondent í s role and employer. The questions then turned to general purchasing issues and policies related to sustainability, documented policies and reports, supplier selection process and the

Institutional sustainable purchasing

priorities



impact of supplier and other drivers on local purchasing and waste reduction practices. The final portion of the interview addressed specific purchasing issues such as highest volume food products, waste streams, and problems with packaging and transportation reduction. Most interviews lasted about one hour. Purchasing individuals had worked in the waste reduction and sustainable purchasing area for three to four years and their institutions served between 2,600 and 8,600 meals per day.

Interview analysis

Our analytical approach is best described as a grounded theory approach. Although it is impossible to approach data without prior expectations or assumptions, we aimed to allow themes to emerge from the data rather than attempting to fit preconceived categories (Lindlof and Taylor, 1995). The authors read all transcripts, field notes, and artifacts in their entirety before rereading the data and identifying themes. Based on our observations, we tentatively identified themes. Through a constant comparison method (Strauss and Corbin, 1998), we grouped the data into categories and developed labels for the categories or themes. The coding process was iterative, and categories were added, combined, and revised in an emergent manner until the coding categories did not require further modification. For a reliability check, both researchers worked independently and checked coding to ensure the accuracy and consistency of the categories (Creswell, 1998).

Interview results

"""


doc = nlp(texto)




print("\n\n*****Entidades que pueden ser stakeholders (partes interesadas) AUTORES*****\n")

autoresTotales=Counter(palabra.text+" "+palabra.label_ for palabra in doc.ents if palabra.label_!='MISC'and palabra.label_!='DATE' and palabra.label_!='CARDINAL' and palabra.label_!='ORDINAL' and palabra.label_!='PERCENT' and palabra.label_!='QUANTITY.¿'  )
for nombre in autoresTotales:
  if(autoresTotales[nombre] > 2): 
    print (nombre,autoresTotales[nombre])

print("\n\n*****Temas que pueden ser representativos TEMAS*****")

temasTotales=Counter(palabra.text for palabra in doc.ents if palabra.label_=='MISC')
for nombre in temasTotales:
  if(temasTotales[nombre] > 1): 
    print (nombre,temasTotales[nombre])



print("\n\n***** REPETICIONES *****")
nombres = [w.lemma_.lower() for w in nlp(texto)
           if w.is_stop != True and w.is_punct != True and w.pos_ != 'CONJ' and w.pos_ != 'SPACE' and w.pos_ != 'NUM' and w.pos_ != 'ADP' and len(w) > 2]

frasesDosPalabras=[]
frasesTresPalabras=[]
i=0
#se construye arreglo de dos y tres palabras seguidas, aunque para el caso
#de dos palabras, se busca palabras repetidas que esten a la izq o der
while i < len(nombres):
    if(i==len(nombres)-1):
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i-1])
        i+=1  
    elif(i==len(nombres)-2):
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i+1])
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i-1])
        i+=1  
    elif(i==0):
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i+1])  
        i+=1   
    else:
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i+1])
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i-1])
        frasesTresPalabras.append(nombres[i] +" "+ nombres[i+1]+" "+ nombres[i+2])
        i+=1  
    

frasesFrecuenteRepetidas=Counter(frasesDosPalabras).most_common(40)
frasesFrecuente=[]
for i in range(0, len(frasesFrecuenteRepetidas), 2):
    frasesFrecuente.append(frasesFrecuenteRepetidas[i])

print("\n30 palabras más repetidas:")
print (Counter(nombres).most_common(30))
print("\n20 juegos de dos palabras más repetidas:")
print (frasesFrecuente)
print("\n10 juegos de tres palabras más repetidas:")
print(Counter(frasesTresPalabras).most_common(10))
