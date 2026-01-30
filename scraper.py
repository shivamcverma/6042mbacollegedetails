from requests import options
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
import re
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

# ---------------- URLS ----------------
BASE_URL = [
    "https://www.shiksha.com/college/iim-ahmedabad-indian-institute-of-management-vastrapur-307",
    "https://www.shiksha.com/college/iim-bangalore-indian-institute-of-management-bannerghatta-road-318",
    "https://www.shiksha.com/college/iim-kozhikode-indian-institute-of-management-20188",
    "https://www.shiksha.com/college/department-of-management-studies-iit-delhi-hauz-khas-35998",
    "https://www.shiksha.com/college/iim-lucknow-indian-institute-of-management-333",
    "https://www.shiksha.com/college/symbiosis-institute-of-business-management-symbiosis-international-pune-lavale-village-3959",
    "https://www.shiksha.com/college/indian-institute-of-management-mumbai-20735",
    "https://www.shiksha.com/college/xlri-xavier-school-of-management-jamshedpur-28564",
    "https://www.shiksha.com/university/andhra-university-visakhapatnam-2948",
    "https://www.shiksha.com/college/s-p-jain-institute-of-management-and-research-mumbai-andheri-west-3489",
    "https://www.shiksha.com/university/indian-institute-of-foreign-trade-delhi-28559",
    "https://www.shiksha.com/university/alagappa-university-karaikudi-23417",
    "https://www.shiksha.com/college/iim-raipur-indian-institute-of-management-32740",
    "https://www.shiksha.com/college/iim-trichy-indian-institute-of-management-tiruchirappalli-36076",
    "https://www.shiksha.com/university/bharathidasan-university-tiruchirappalli-22026",
    "https://www.shiksha.com/university/university-of-madras-chennai-23679",
    "https://www.shiksha.com/university/mgu-kerala-mahatma-gandhi-university-kottayam-24666",
    "https://www.shiksha.com/college/iim-ranchi-indian-institute-of-management-32728",
    "https://www.shiksha.com/university/bangalore-university-3701",
    "https://www.shiksha.com/college/iit-kanpur-department-of-industrial-and-management-engineering-53988",
    "https://www.shiksha.com/college/imt-ghaziabad-institute-of-management-technology-255",
    "https://www.shiksha.com/university/pau-punjab-agricultural-university-ludhiana-986",
    "https://www.shiksha.com/college/iim-visakhapatnam-indian-institute-of-management-47712",
    "https://www.shiksha.com/university/dibrugarh-university-31514",
    "https://www.shiksha.com/college/iim-bodh-gaya-indian-institute-of-management-49314",
    "https://www.shiksha.com/university/madurai-kamaraj-university-mku-24865",
    "https://www.shiksha.com/university/lpu-lovely-professional-university-jalandhar-28499",
    "https://www.shiksha.com/university/university-of-calicut-51534",
    "https://www.shiksha.com/college/jaipuria-noida-jaipuria-institute-of-management-29088",
    "https://www.shiksha.com/college/goa-institute-of-management-goa-other-22600",
    "https://www.shiksha.com/university/periyar-university-salem-19392",
    "https://www.shiksha.com/college/imi-kolkata-alipore-35997",
    "https://www.shiksha.com/university/ccsu-chaudhary-charan-singh-university-meerut-19694",
    "https://www.shiksha.com/university/tamil-nadu-agricultural-university-coimbatore-23625",
    "https://www.shiksha.com/college/college-of-engineering-pune-28324",
    "https://www.shiksha.com/university/amity-university-noida-41334",
    "https://www.shiksha.com/university/acharya-narendra-deva-university-of-agriculture-and-technology-faizabad-65247",
    "https://www.shiksha.com/college/institute-of-management-nirma-university-s-g-highway-ahmedabad-3029",
    "https://www.shiksha.com/university/berhampur-university-orissa-other-26281",
    "https://www.shiksha.com/university/bundelkhand-university-jhansi-uttar-pradesh-other-25207",
    "https://www.shiksha.com/university/tribhuvan-sahkari-university-anand-28620",
    "https://www.shiksha.com/university/chaudhary-charan-singh-haryana-agricultural-university-haryana-other-23876",
    "https://www.shiksha.com/college/loyola-institute-of-business-administration-nungambakkam-chennai-33857",
    "https://www.shiksha.com/university/srm-institute-of-science-and-technology-kattankulathur-chennai-24749",
    "https://www.shiksha.com/university/nit-trichy-national-institute-of-technology-tiruchirappalli-2996",
    "https://www.shiksha.com/university/saveetha-institute-of-medical-and-technical-sciences-poonamallee-chennai-34281",
    "https://www.shiksha.com/university/gujarat-technological-university-ahmedabad-57789",
    "https://www.shiksha.com/college/iim-amritsar-indian-institute-of-management-47709",
    "https://www.shiksha.com/university/soa-university-siksha-o-anusandhan-bhubaneswar-38037",
    "https://www.shiksha.com/university/harcourt-butler-technical-university-kanpur-5040",
    "https://www.shiksha.com/university/jain-deemed-to-be-university-bangalore-424",
    "https://www.shiksha.com/college/kiit-school-of-management-kalinga-institute-of-industrial-technology-bhubaneswar-32416",
    "https://www.shiksha.com/university/indira-gandhi-krishi-vishwavidyalaya-raipur-63929",
    "https://www.shiksha.com/college/jaipuria-lucknow-jaipuria-institute-of-management-29084",
    "https://www.shiksha.com/college/jaipuria-jaipur-jaipuria-institute-of-management-29091",
    "https://www.shiksha.com/university/guru-gobind-singh-indraprastha-university-delhi-24725",
    "https://www.shiksha.com/university/kuvempu-university-shimoga-1610",
    "https://www.shiksha.com/college/rajasthan-college-of-agriculture-maharana-pratap-university-of-agriculture-and-technology-udaipur-106187",
    "https://www.shiksha.com/college/school-of-management-bml-munjal-university-gurgaon-38132",
    "https://www.shiksha.com/university/mahatma-jyotiba-phule-rohilkhand-university-bareilly-20593",
    "https://www.shiksha.com/university/babasaheb-bhimrao-ambedkar-university-bbau-lucknow-26165",
    "https://www.shiksha.com/university/chitkara-university-chandigarh-25096",
    "https://www.shiksha.com/college/college-of-agriculture-mahatma-phule-krishi-vidyapeeth-shivaji-nagar-pune-52774",
    "https://www.shiksha.com/university/odisha-university-of-agriculture-and-technology-bhubaneswar-57101",
    "https://www.shiksha.com/university/jamia-hamdard-delhi-3082",
    "https://www.shiksha.com/university/prsu-pandit-ravishankar-shukla-university-raipur-1626",
    "https://www.shiksha.com/college/college-of-engineering-anna-university-guindy-chennai-51546",
    "https://www.shiksha.com/university/punjabi-university-patiala-24117",
    "https://www.shiksha.com/college/jagan-institute-of-management-studies-rohini-rohini-delhi-28468",
    "https://www.shiksha.com/college/som-pandit-deendayal-energy-university-pdeu-gandhinagar-30990",
    "https://www.shiksha.com/university/ravenshaw-university-cuttack-52514",
    "https://www.shiksha.com/university/sambalpur-university-25285",
    "https://www.shiksha.com/university/birla-institute-of-technology-mesra-ranchi-24087",
    "https://www.shiksha.com/university/amity-university-gurugram-gurgaon-38084",
    "https://www.shiksha.com/college/pune-institute-of-business-management-mulshi-37019",
    "https://www.shiksha.com/college/iit-jodhpur-indian-institute-of-technology-32712",
    "https://www.shiksha.com/university/uoh-university-of-hyderabad-23069",
    "https://www.shiksha.com/college/imt-nagpur-institute-of-management-technology-2942",
    "https://www.shiksha.com/university/university-of-lucknow-21456",
    "https://www.shiksha.com/university/vidyasagar-university-midnapore-4217",
    "https://www.shiksha.com/college/sharda-school-of-business-studies-greater-noida-28552",
    "https://www.shiksha.com/college/jaipuria-indore-jaipuria-institute-of-management-32476",
    "https://www.shiksha.com/university/opju-op-jindal-university-raigarh-chhattisgarh-other-47013",
    "https://www.shiksha.com/university/vignan-s-foundation-for-science-technology-and-research-guntur-21507",
    "https://www.shiksha.com/university/gjust-guru-jambheshwar-university-of-science-and-technology-hisar-3273",
    "https://www.shiksha.com/college/national-academy-of-agricultural-research-management-rajendra-nagar-hyderabad-37509",
    "https://www.shiksha.com/college/chandigarh-business-school-of-administration-sahibzada-ajit-singh-nagar-116853",
    "https://www.shiksha.com/college/cms-business-school-jain-deemed-to-be-university-bangalore-gandhi-nagar-38233",
    "https://www.shiksha.com/college/gibs-business-school-bangalore-46745",
    "https://www.shiksha.com/college/nmims-school-of-business-management-mumbai-vile-parle-west-46487",
    "https://www.shiksha.com/college/dayananda-sagar-business-school-banashankari-bangalore-28376",
    "https://www.shiksha.com/college/symbiosis-institute-of-operations-management-symbiosis-international-nashik-33796",
    "https://www.shiksha.com/college/itm-business-school-navi-mumbai-35619",
    "https://www.shiksha.com/college/soil-institute-of-management-gurgaon-26672",
    "https://www.shiksha.com/college/sies-college-of-management-studies-navi-mumbai-mumbai-28278",
    "https://www.shiksha.com/college/rajagiri-centre-for-business-studies-kochi-30865",
    "https://www.shiksha.com/college/prin-l-n-welingkar-institute-of-management-development-and-research-hosur-road-bangalore-32444",
    "https://www.shiksha.com/college/indian-institute-of-social-welfare-and-business-management-college-square-kolkata-166",
    "https://www.shiksha.com/college/chitkara-business-school-chitkara-university-chandigarh-28446",
    "https://www.shiksha.com/university/shoolini-university-solan-31257",
    "https://www.shiksha.com/college/fortune-institute-of-international-business-vasant-vihar-delhi-24286",
    "https://www.shiksha.com/college/xavier-institute-of-management-and-entrepreneurship-kochi-36454",
    "https://www.shiksha.com/college/aims-institutes-peenya-bangalore-3698",
    "https://www.shiksha.com/college/ramaiah-institute-of-management-m-s-ramaiah-bangalore-30829",
    "https://www.shiksha.com/college/rv-institute-of-management-jayanagar-bangalore-28525",
    "https://www.shiksha.com/university/sri-sri-university-bhubaneswar-34208",
    "https://www.shiksha.com/college/balaji-institute-of-management-and-human-resource-development-sri-balaji-university-tathawade-pune-30144",
    "https://www.shiksha.com/college/its-institute-of-technology-and-science-ghaziabad-25218",
    "https://www.shiksha.com/college/calcutta-business-school-24-parganas-south-kolkata-30699",
    "https://www.shiksha.com/university/amity-university-gwalior-38082",
    "https://www.shiksha.com/university/dsu-dayananda-sagar-university-bangalore-48042",
    "https://www.shiksha.com/university/bharath-institute-of-higher-education-and-research-biher-chennai-24072",
    "https://www.shiksha.com/college/amity-global-business-school-mumbai-malad-west-36842",
    "https://www.shiksha.com/college/kec-kongu-engineering-college-erode-3598",
    "https://www.shiksha.com/college/aurora-s-business-school-aurora-group-of-institutions-panjagutta-hyderabad-24827",
    "https://www.shiksha.com/college/institute-of-management-studies-noida-1144",
    "https://www.shiksha.com/university/amity-university-raipur-46902",
    "https://www.shiksha.com/college/saintgits-institute-of-management-kottayam-30931",
    "https://www.shiksha.com/university/quantum-university-roorkee-54618",
    "https://www.shiksha.com/university/reva-university-bangalore-40416",
    "https://www.shiksha.com/university/poornima-university-jaipur-36071",
    "https://www.shiksha.com/university/amity-university-lucknow-38047",
    "https://www.shiksha.com/college/siva-sivani-institute-of-management-kompalli-hyderabad-29602",
    "https://www.shiksha.com/college/chandragupt-institute-of-management-patna-23763",
    "https://www.shiksha.com/college/school-of-business-indira-university-tathawade-pune-32570",
    "https://www.shiksha.com/college/i-business-institute-greater-noida-56463",
    "https://www.shiksha.com/college/sree-saraswathi-thyagaraja-college-coimbatore-9872",
    "https://www.shiksha.com/college/the-business-school-university-of-jammu-53587",
    "https://www.shiksha.com/college/srm-easwari-engineering-college-ramapuram-chennai-1517",
    "https://www.shiksha.com/college/trident-academy-of-creative-technology-bhubaneswar-23154",
    "https://www.shiksha.com/university/bahra-university-solan-35924",
    "https://www.shiksha.com/college/cmr-institute-of-technology-bangalore-i-t-park-road-3055",
    "https://www.shiksha.com/college/bms-college-of-engineering-bangalore-397",
    "https://www.shiksha.com/college/cmr-college-of-engineering-and-technology-medchal-hyderabad-24274",
    "https://www.shiksha.com/college/nimt-global-institute-of-management-technology-nimt-global-jaipur-35265",
    "https://www.shiksha.com/college/bannari-amman-institute-of-technology-erode-9761",
    "https://www.shiksha.com/college/velalar-college-of-engineering-and-technology-erode-42544",
    "https://www.shiksha.com/college/bharatiya-vidya-bhavan-institute-of-management-science-bimskol-salt-lake-city-kolkata-28097",
    "https://www.shiksha.com/college/hindusthan-college-of-arts-and-science-coimbatore-5228",
    "https://www.shiksha.com/college/faculty-of-management-studies-university-of-delhi-malka-ganj-28361",
    "https://www.shiksha.com/college/tilak-raj-chadha-institute-of-management-and-technology-yamuna-nagar-2852",
    "https://www.shiksha.com/college/ies-s-management-college-and-research-centre-bandra-west-mumbai-28220",
    "https://www.shiksha.com/college/rathinam-college-of-arts-and-science-coimbatore-25364",
    "https://www.shiksha.com/college/presidency-college-hebbal-bangalore-19396",
    "https://www.shiksha.com/university/integral-university-iul-lucknow-21870",
    "https://www.shiksha.com/university/lingaya-s-vidyapeeth-faridabad-24621",
    "https://www.shiksha.com/college/nehru-college-of-engineering-and-research-centre-ncerc-thrissur-25023",
    "https://www.shiksha.com/college/the-oxford-college-of-business-management-h-s-r-layout-bangalore-21403",
    "https://www.shiksha.com/college/jnnce-jawaharlal-nehru-national-college-of-engineering-shimoga-22357",
    "https://www.shiksha.com/college/poddar-group-of-institution-jaipur-48877",
    "https://www.shiksha.com/college/nehru-memorial-college-tiruchirappalli-20769",
    "https://www.shiksha.com/college/jaipuria-school-of-business-ghaziabad-48786",
    "https://www.shiksha.com/college/sardar-vallabhbhai-patel-international-school-of-textiles-and-management-coimbatore-25334",
    "https://www.shiksha.com/college/the-oxford-college-of-engineering-hosur-road-bangalore-449",
    "https://www.shiksha.com/college/coimbatore-institute-of-management-and-technology-cimat-11891",
    "https://www.shiksha.com/college/p-k-r-arts-college-for-women-erode-22870",
    "https://www.shiksha.com/college/harlal-institute-of-management-and-technology-greater-noida-48928",
    "https://www.shiksha.com/college/global-business-school-hubli-28515",
    "https://www.shiksha.com/college/christ-academy-institute-for-advanced-studies-electronic-city-phase-1-bangalore-56171",
    "https://www.shiksha.com/college/t-john-group-of-institutions-bannerghatta-road-bangalore-28395",
    "https://www.shiksha.com/college/sahrdaya-institute-of-management-studies-thrissur-53441",
    "https://www.shiksha.com/college/university-business-school-chandigarh-21440",
    "https://www.shiksha.com/university/the-icfai-university-sikkim-gangtok-52524",
    "https://www.shiksha.com/college/acropolis-faculty-of-management-and-research-indore-65043",
    "https://www.shiksha.com/college/srbs-sheila-raheja-school-of-business-management-research-bandra-east-mumbai-43351",
    "https://www.shiksha.com/college/datta-meghe-institute-of-management-studies-nagpur-43309",
    "https://www.shiksha.com/college/sbs-sinhgad-business-school-erandwana-pune-42811",
    "https://www.shiksha.com/college/myra-school-of-business-mysore-33987",
    "https://www.shiksha.com/college/prasad-v-potluri-siddhartha-institute-of-technology-vijayawada-24531",
    "https://www.shiksha.com/college/ims-business-school-imsbs-kolkata-sonarpur-37942",
    "https://www.shiksha.com/university/bits-pilani-birla-institute-of-technology-and-science-467",
    "https://www.shiksha.com/university/kiet-university-ghaziabad-962",
    "https://www.shiksha.com/college/indian-school-of-business-hyderabad-gachibowli-28444",
    "https://www.shiksha.com/college/school-of-business-upes-dehradun-38604",
    "https://www.shiksha.com/university/adamas-university-kolkata-46715",
    "https://www.shiksha.com/college/iilm-university-greater-noida-3227",
    "https://www.shiksha.com/college/international-institute-of-business-studies-airport-new-airport-bangalore-49833",
    "https://www.shiksha.com/college/vishwa-vishwani-institute-of-systems-and-management-hyderabad-51902",
    "https://www.shiksha.com/college/lloyd-business-school-greater-noida-37957",
    "https://www.shiksha.com/college/b-k-school-of-professional-and-management-studies-navrangpura-ahmedabad-24660",
    "https://www.shiksha.com/college/symbiosis-institute-of-business-management-symbiosis-international-bangalore-hosur-road-36082",
    "https://www.shiksha.com/university/assam-down-town-university-adtu-guwahati-38050",
    "https://www.shiksha.com/college/greater-noida-institute-of-technology-32439",
    "https://www.shiksha.com/college/centurion-university-of-technology-and-management-bhubaneswar-campus-53057",
    "https://www.shiksha.com/college/riim-arihant-group-of-institutes-bavdhan-pune-46556",
    "https://www.shiksha.com/university/jis-university-kolkata-47791",
    "https://www.shiksha.com/college/dev-bhoomi-uttarakhand-university-dehradun-47413",
    "https://www.shiksha.com/college/university-college-of-commerce-and-business-management-osmania-university-tarnaka-hyderabad-53677",
    "https://www.shiksha.com/college/rajalakshmi-engineering-college-thandalam-chennai-24039",
    "https://www.shiksha.com/college/vit-business-school-vellore-institute-of-technology-vellore-31040",
    "https://www.shiksha.com/college/jindal-global-business-school-o-p-jindal-global-university-sonepat-34723",
    "https://www.shiksha.com/college/international-institute-of-management-studies-iims-pune-hinjewadi-31240",
    "https://www.shiksha.com/college/cmr-technical-campus-autonomous-engineering-college-medchal-hyderabad-42690",
    "https://www.shiksha.com/college/dy-patil-akurdi-mba-akurdi-pune-35064",
    "https://www.shiksha.com/college/haldia-institute-of-technology-harish-mukherjee-road-kolkata-1116",
    "https://www.shiksha.com/college/ramdeobaba-university-nagpur-21172",
    "https://www.shiksha.com/college/kcc-institute-of-technology-and-management-greater-noida-32427",
    "https://www.shiksha.com/college/gems-b-school-bangalore-vasanth-nagar-26986",
    "https://www.shiksha.com/college/ips-academy-indore-49406",
    "https://www.shiksha.com/college/asm-s-institute-of-business-management-and-research-chinchwad-pune-30065",
    "https://www.shiksha.com/college/lakshmi-narain-college-of-technology-bhopal-42559",
    "https://www.shiksha.com/college/loyola-institute-of-technology-palanchur-chennai-42584",
    "https://www.shiksha.com/college/nmims-hyderabad-mahboobnagar-35399",
    "https://www.shiksha.com/college/icfai-business-school-ibs-bangalore-mysore-road-36231",
    "https://www.shiksha.com/college/bengal-institute-of-business-studies-lake-view-road-kolkata-30386",
    "https://www.shiksha.com/college/k-k-wagh-institute-of-engineering-education-and-research-nashik-20406",
    "https://www.shiksha.com/university/m-s-ramaiah-university-of-applied-sciences-msruas-bangalore-47146",
    "https://www.shiksha.com/college/dr-d-y-patil-b-school-tathawade-pune-54766",
    "https://www.shiksha.com/college/nicmar-university-pune-balewadi-27442",
    "https://www.shiksha.com/university/gls-university-ahmedabad-58429",
    "https://www.shiksha.com/college/international-institute-of-health-management-research-iihmr-new-delhi-dwarka-34295",
    "https://www.shiksha.com/university/mangalayatan-university-aligarh-22191",
    "https://www.shiksha.com/college/st-joseph-s-college-of-engineering-old-mahabalipuram-road-chennai-24564",
    "https://www.shiksha.com/college/nhce-bangalore-new-horizon-college-of-engineering-marathahalli-46973",
    "https://www.shiksha.com/college/icfai-business-school-mumbai-powai-26449",
    "https://www.shiksha.com/college/symbiosis-institute-of-business-management-noida-213435",
    "https://www.shiksha.com/college/atria-institute-of-technology-hebbal-bangalore-28151",
    "https://www.shiksha.com/college/zeal-college-of-engineering-and-research-narhe-pune-36894",
    "https://www.shiksha.com/college/chitkara-college-of-sales-and-marketing-chitkara-university-chandigarh-52072",
    "https://www.shiksha.com/college/empi-business-school-chattarpur-delhi-25938",
    "https://www.shiksha.com/college/malla-reddy-university-powered-by-sunstone-malkajgiri-hyderabad-202651",
    "https://www.shiksha.com/university/patna-university-25175",
    "https://www.shiksha.com/college/malla-reddy-college-of-engineering-and-technology-medchal-hyderabad-42615",
    "https://www.shiksha.com/college/jd-college-of-engineering-and-management-nagpur-42674",
    "https://www.shiksha.com/college/krupanidhi-college-of-management-krupanidhi-group-of-institutions-sarjapur-road-bangalore-36613",
    "https://www.shiksha.com/college/altera-institute-gurgaon-212387",
    "https://www.shiksha.com/university/babu-banarasi-das-university-lucknow-33058",
    "https://www.shiksha.com/college/maharaja-agrasen-institute-of-technology-rohini-delhi-24875",
    "https://www.shiksha.com/college/pratap-college-of-management-uttar-pradesh-other-37675",
    "https://www.shiksha.com/college/uttaranchal-institute-of-management-uttaranchal-university-dehradun-30675",
    "https://www.shiksha.com/university/centurion-university-of-technology-and-management-paralakhemundi-orissa-other-53023",
    "https://www.shiksha.com/college/siom-sinhgad-institute-of-management-vadgaon-budruk-pune-52003",
    "https://www.shiksha.com/university/dr-m-g-r-educational-and-research-institute-chennai-33330",
    "https://www.shiksha.com/college/rajalakshmi-school-of-business-chembarambakkam-chennai-49108",
    "https://www.shiksha.com/college/jims-kalkaji-jagannath-international-management-school-kalkaji-delhi-28470",
    "https://www.shiksha.com/college/nims-institute-of-business-studies-nims-university-jaipur-52977",
    "https://www.shiksha.com/university/gautam-buddha-university-greater-noida-38229",
    "https://www.shiksha.com/university/srm-institute-of-science-and-technology-chennai-ramapuram-campus-51992",
    "https://www.shiksha.com/college/gitarattan-international-business-school-rohini-delhi-37867",
    "https://www.shiksha.com/college/eastern-institute-for-integrated-learning-in-management-eiilm-esplanade-kolkata-28435",
    "https://www.shiksha.com/college/icfai-business-school-ibs-gurgaon-35452",
    "https://www.shiksha.com/university/p-p-savani-university-surat-53279",
    "https://www.shiksha.com/college/indsearch-institute-of-management-studies-and-research-bavdhan-campus-bavdhan-pune-21643",
    "https://www.shiksha.com/college/keshav-memorial-institute-of-technology-narayanguda-hyderabad-44845",
    "https://www.shiksha.com/university/rv-university-bangalore-151359",
    "https://www.shiksha.com/university/gd-goenka-university-gurgaon-36294",
    "https://www.shiksha.com/university/shri-guru-ram-rai-university-dehradun-101361",
    "https://www.shiksha.com/college/abes-engineering-college-ghaziabad-24068",
    "https://www.shiksha.com/college/christ-delhi-ncr-campus-ghaziabad-39326",
    "https://www.shiksha.com/university/techno-india-university-kolkata-38061",
    "https://www.shiksha.com/university/shri-ramswaroop-memorial-university-lucknow-24759",
    "https://www.shiksha.com/college/i-t-s-school-of-management-ghaziabad-149101",
    "https://www.shiksha.com/college/gitam-school-of-business-hyderabad-patancheru-32970",
    "https://www.shiksha.com/college/city-group-of-college-lucknow-41011",
    "https://www.shiksha.com/college/school-of-management-cmr-university-kalyan-nagar-bangalore-52032",
    "https://www.shiksha.com/college/kiit-school-of-rural-management-ksrm-bhubaneswar-43022",
    "https://www.shiksha.com/college/alliance-ascent-college-alliance-university-btm-2nd-stage-bangalore-49202",
    "https://www.shiksha.com/college/sri-krishna-college-of-technology-coimbatore-3868",
    "https://www.shiksha.com/college/som-lalit-institute-of-management-studies-slims-slibm-navrangpura-ahmedabad-211969",
    "https://www.shiksha.com/college/amrita-school-of-business-amrita-vishwa-vidyapeetham-kochi-campus-244900",
    "https://www.shiksha.com/college/karpagam-college-of-engineering-coimbatore-23772",
    "https://www.shiksha.com/college/finx-institute-fort-mumbai-28834",
    "https://www.shiksha.com/university/veer-narmad-south-gujarat-university-surat-29852",
    "https://www.shiksha.com/college/vidyavardhaka-college-of-engineering-mysore-21504",
    "https://www.shiksha.com/college/sms-school-of-management-sciences-varanasi-29170",
    "https://www.shiksha.com/college/all-india-shri-shivaji-memorial-society-s-institute-of-management-kennedy-road-pune-57085",
    "https://www.shiksha.com/college/raj-kumar-goel-institute-of-technology-rkgit-ghaziabad-25012",
    "https://www.shiksha.com/college/jhulelal-institute-of-technology-nagpur-42808",
    "https://www.shiksha.com/college/city-college-jayanagar-bangalore-25170",
    "https://www.shiksha.com/college/school-of-management-sciences-lucknow-29104",
    "https://www.shiksha.com/university/d-y-patil-university-pune-113753",
    "https://www.shiksha.com/college/surana-college-post-graduate-departments-kengeri-bangalore-3742",
    "https://www.shiksha.com/university/pimpri-chinchwad-university-pcu-pune-211493",
    "https://www.shiksha.com/college/nit-warangal-national-institute-of-technology-25425",
    "https://www.shiksha.com/university/sgt-university-gurgaon-38726",
    "https://www.shiksha.com/college/s-b-patil-institute-of-management-pimpri-chinchwad-educations-trust-s-nigdi-pune-36376",
    "https://www.shiksha.com/college/dr-ambedkar-institute-of-management-studies-and-research-nagpur-63997",
    "https://www.shiksha.com/college/global-institute-of-technology-and-management-gurgaon-36326",
    "https://www.shiksha.com/university/saveetha-university-saveetha-institute-of-medical-and-technical-sciences-chennai-48312",
    "https://www.shiksha.com/college/chandigarh-group-of-colleges-landran-45524",
    "https://www.shiksha.com/university/cuhp-central-university-of-himachal-pradesh-dharamsala-32735",
    "https://www.shiksha.com/college/kv-institute-of-management-and-information-studies-kvimis-coimbatore-36863",
    "https://www.shiksha.com/college/kashi-institute-of-technology-varanasi-37250",
    "https://www.shiksha.com/college/institute-of-engineering-and-technology-iet-dr-a-p-j-abdul-kalam-technical-university-lucknow-24137",
    "https://www.shiksha.com/college/regional-college-of-management-bangalore-devanhalli-48874",
    "https://www.shiksha.com/college/east-west-college-of-management-vishwaneedam-bangalore-239416",
    "https://www.shiksha.com/college/school-of-management-ajeenkya-dy-patil-university-lohegaon-pune-48026",
    "https://www.shiksha.com/college/shri-ram-institute-of-technology-jabalpur-42593",
    "https://www.shiksha.com/university/banasthali-vidyapith-jaipur-3155",
    "https://www.shiksha.com/college/amity-global-business-school-hyderabad-panjagutta-36841",
    "https://www.shiksha.com/college/amrapali-university-haldwani-24855",
    "https://www.shiksha.com/college/symbiosis-institute-of-management-studies-symbiosis-international-pune-khadki-21359",
    "https://www.shiksha.com/college/christ-lavasa-pune-campus-mulshi-38868",
    "https://www.shiksha.com/college/cmr-institute-of-technology-medchal-hyderabad-46220",
    "https://www.shiksha.com/college/st-ann-s-college-for-women-mehdipatnam-hyderabad-19426",
    "https://www.shiksha.com/university/aditya-university-kakinada-229163",
    "https://www.shiksha.com/college/lucknow-institute-of-technology-26453",
    "https://www.shiksha.com/college/sjb-institute-of-technology-kengeri-bangalore-25122",
    "https://www.shiksha.com/college/a-v-college-of-arts-science-and-commerce-gagan-mahal-hyderabad-19502",
    "https://www.shiksha.com/university/guru-nanak-dev-university-amritsar-24108",
    "https://www.shiksha.com/college/smit-sikkim-manipal-institute-of-technology-sikkim-manipal-university-rangpo-34437",
    "https://www.shiksha.com/college/dav-college-chandigarh-1623",
    "https://www.shiksha.com/university/maharishi-markandeshwar-university-mullana-ambala-4279",
    "https://www.shiksha.com/college/bangalore-institute-of-technology-chamrajpet-25445",
    "https://www.shiksha.com/university/marwadi-university-rajkot-53683",
    "https://www.shiksha.com/college/kommuri-pratap-reddy-institute-of-technology-ghatkesar-hyderabad-43037",
    "https://www.shiksha.com/college/ims-engineering-college-ghaziabad-24985",
    "https://www.shiksha.com/college/maharaja-agrasen-institute-of-management-and-technology-yamuna-nagar-279",
    "https://www.shiksha.com/college/symbiosis-institute-of-digital-and-telecom-management-symbiosis-international-pune-lavale-village-4524",
    "https://www.shiksha.com/college/aimsr-aditya-institute-of-management-studies-and-research-borivali-west-mumbai-34262",
    "https://www.shiksha.com/college/asma-institute-of-management-shivane-pune-30875",
    "https://www.shiksha.com/college/yeshwantrao-chavan-college-of-engineering-nagar-yuwak-shikshan-sanstha-nagpur-11259",
    "https://www.shiksha.com/college/sinhgad-college-of-engineering-vadgaon-budruk-pune-52071",
    "https://www.shiksha.com/college/swami-vivekananda-institute-of-science-and-technology-sonarpur-kolkata-40228",
    "https://www.shiksha.com/college/isbr-college-electronic-city-phase-1-bangalore-48827",
    "https://www.shiksha.com/university/jayoti-vidyapeeth-women-s-university-jaipur-24508",
    "https://www.shiksha.com/college/eastern-institute-for-integrated-learning-in-management-salt-lake-salt-lake-city-kolkata-213973",
    "https://www.shiksha.com/university/indira-gandhi-delhi-technical-university-for-women-igdtuw-47485",
    "https://www.shiksha.com/college/cmr-center-for-business-studies-banasavadi-bangalore-48187",
    "https://www.shiksha.com/college/atlas-skilltech-university-school-of-management-and-entrepreneurship-kurla-west-mumbai-48931",
    "https://www.shiksha.com/college/symbiosis-institute-of-health-sciences-symbiosis-international-pune-lavale-4517",
    "https://www.shiksha.com/college/iiit-lucknow-indian-institute-of-information-technology-53802",
    "https://www.shiksha.com/college/bhavan-s-royal-institute-of-management-kochi-51889",
    "https://www.shiksha.com/college/dr-d-y-patil-school-of-management-pune-lohegaon-40757",
    "https://www.shiksha.com/college/nalla-malla-reddy-engineering-college-ghatkesar-hyderabad-21980",
    "https://www.shiksha.com/college/sri-muthukumaran-institute-of-technology-chikkarayapuram-chennai-61607",
    "https://www.shiksha.com/college/gitam-school-of-business-visakhapatnam-36584",
    "https://www.shiksha.com/college/amity-global-business-school-indore-36849",
    "https://www.shiksha.com/university/dr-ram-manohar-lohia-avadh-university-uttar-pradesh-other-19953",
    "https://www.shiksha.com/college/nagarjuna-college-of-engineering-and-technology-devanhalli-bangalore-24585",
    "https://www.shiksha.com/college/mite-mangalore-institute-of-technology-and-engineering-42688",
    "https://www.shiksha.com/college/wainganga-college-of-engineering-and-management-nagpur-42701",
    "https://www.shiksha.com/university/mahindra-university-hyderabad-152023",
    "https://www.shiksha.com/college/suryadatta-institute-of-management-and-mass-communication-bavdhan-pune-27937",
    "https://www.shiksha.com/college/regional-college-of-management-bhubaneswar-24881",
    "https://www.shiksha.com/college/guru-nanak-college-velachery-chennai-48064",
    "https://www.shiksha.com/university/dr-c-v-raman-university-bilaspur-31270",
    "https://www.shiksha.com/college/met-institute-of-post-graduate-diploma-in-management-bandra-west-mumbai-152029",
    "https://www.shiksha.com/college/lal-bahadur-shastri-institute-of-management-and-development-studies-lucknow-30543",
    "https://www.shiksha.com/college/aims-atharva-institute-of-management-studies-malad-west-mumbai-35681",
    "https://www.shiksha.com/university/renaissance-university-indore-62691",
    "https://www.shiksha.com/college/symbiosis-national-aptitude-test-bangalore-hosur-road-32008",
    "https://www.shiksha.com/college/amity-school-of-engineering-and-technology-amity-university-noida-36761",
    "https://www.shiksha.com/college/indian-academy-school-of-management-studies-kalyan-nagar-bangalore-26733",
    "https://www.shiksha.com/college/bbit-budge-budge-institute-of-technology-budge-budge-kolkata-34790",
    "https://www.shiksha.com/college/stanley-college-of-engineering-and-technology-for-women-abids-hyderabad-42601",
    "https://www.shiksha.com/college/devi-ahilya-vishwavidyalaya-takshashila-campus-indore-146099",
    "https://www.shiksha.com/college/national-institute-of-science-and-technology-brahmapur-20745",
    "https://www.shiksha.com/college/k-s-group-of-institutions-kanakapura-road-bangalore-36173",
    "https://www.shiksha.com/college/karunya-school-of-management-karunya-institute-of-technology-and-sciences-coimbatore-47742",
    "https://www.shiksha.com/college/sankara-college-of-science-and-commerce-coimbatore-8626",
    "https://www.shiksha.com/university/jaypee-institute-of-information-technology-noida-20383",
    "https://www.shiksha.com/university/tmv-tilak-maharashtra-vidyapeeth-pune-25660",
    "https://www.shiksha.com/college/st-aloysius-institute-of-management-and-information-technology-aimit-mangalore-461",
    "https://www.shiksha.com/college/national-institute-of-securities-markets-raigad-46925",
    "https://www.shiksha.com/college/amity-global-business-school-chennai-nungambakkam-36839",
    "https://www.shiksha.com/university/royal-global-university-guwahati-52094",
    "https://www.shiksha.com/university/jharkhand-rai-university-ranchi-42948",
    "https://www.shiksha.com/college/itm-sls-baroda-university-vadodara-36486",
    "https://www.shiksha.com/college/manson-center-of-excellence-school-of-business-management-begumpet-hyderabad-154027",
    "https://www.shiksha.com/college/symbiosis-institute-of-business-management-symbiosis-international-hyderabad-rangareddy-47829",
    "https://www.shiksha.com/university/jss-science-and-technology-university-mysore-64589",
    "https://www.shiksha.com/college/amrita-school-of-business-amrita-vishwa-vidyapeetham-amritapuri-campus-kollam-38131",
    "https://www.shiksha.com/university/ganpat-university-guni-mehsana-42967",
    "https://www.shiksha.com/college/international-institute-of-sports-management-andheri-east-mumbai-48939",
    "https://www.shiksha.com/university/uka-tarsadia-university-surat-41376",
    "https://www.shiksha.com/university/gkv-gurukula-kangri-vishwavidyalaya-haridwar-25246",
    "https://www.shiksha.com/college/icfai-business-school-ibs-ahmedabad-25275",
    "https://www.shiksha.com/college/jaypee-business-school-noida-22073",
    "https://www.shiksha.com/college/vardhaman-college-of-engineering-shamshabad-hyderabad-25491",
    "https://www.shiksha.com/college/dayananda-sagar-college-of-arts-science-and-commerce-banashankari-bangalore-19810",
    "https://www.shiksha.com/college/management-education-and-research-institute-janakpuri-delhi-37434",
    "https://www.shiksha.com/college/amity-global-business-school-ahmedabad-bodakdev-36820",
    "https://www.shiksha.com/college/iim-lucknow-indian-institute-of-management-noida-campus-53008",
    "https://www.shiksha.com/college/srm-institute-of-science-and-technology-tiruchirappalli-153369",
    "https://www.shiksha.com/college/thakur-global-business-school-tgbs-kandivali-east-mumbai-146145",
    "https://www.shiksha.com/college/sns-college-of-engineering-sns-group-of-institutions-coimbatore-42576",
    "https://www.shiksha.com/college/administrative-management-college-bannerghatta-road-bangalore-35171",
    "https://www.shiksha.com/university/svsu-swami-vivekanand-subharti-university-meerut-37210",
    "https://www.shiksha.com/college/national-institute-of-pharmaceutical-education-and-research-s-a-s-nagar-punjab-other-23374",
    "https://www.shiksha.com/university/assam-university-silchar-25147",
    "https://www.shiksha.com/college/dr-b-r-ambedkar-institute-of-management-and-technology-baghlingampally-hyderabad-37298",
    "https://www.shiksha.com/college/sr-group-of-institutions-lucknow-33294",
    "https://www.shiksha.com/university/tripura-university-agartala-31157",
    "https://www.shiksha.com/college/united-group-of-institutions-ugi-allahabad-27910",
    "https://www.shiksha.com/college/marwari-college-ranchi-63675",
    "https://www.shiksha.com/college/bv-raju-institute-of-technology-hyderabad-20841",
    "https://www.shiksha.com/college/mce-meenakshi-college-of-engineering-k-k-nagar-chennai-37494",
    "https://www.shiksha.com/college/methodist-college-of-engineering-technology-abids-hyderabad-43034",
    "https://www.shiksha.com/college/p-r-pote-patil-college-of-engineering-and-management-amravati-59809",
    "https://www.shiksha.com/college/national-power-training-institute-faridabad-4285",
    "https://www.shiksha.com/college/s-b-jain-institute-of-technology-management-and-research-nagpur-57543",
    "https://www.shiksha.com/college/iilm-academy-of-higher-learning-lucknow-29375",
    "https://www.shiksha.com/college/indus-business-academy-iba-kanakapura-road-bangalore-150557",
    "https://www.shiksha.com/college/amity-global-business-school-pune-shivaji-nagar-36860",
    "https://www.shiksha.com/college/sage-university-powered-by-sunstone-indore-151301",
    "https://www.shiksha.com/college/bms-institute-of-technology-and-management-yelahanaka-bangalore-21616",
    "https://www.shiksha.com/university/graphic-era-hill-university-dehradun-37848",
    "https://www.shiksha.com/college/vidya-jyothi-institute-of-technology-c-b-post-hyderabad-25306",
    "https://www.shiksha.com/college/army-institute-of-management-and-technology-greater-noida-54700",
    "https://www.shiksha.com/college/school-of-business-management-noida-international-university-greater-noida-35845",
    "https://www.shiksha.com/college/kle-dr-m-s-sheshgiri-college-of-engineering-and-technology-belgaum-36765",
    "https://www.shiksha.com/college/xavier-institute-of-management-and-entrepreneurship-chennai-kanchipuram-52580",
    "https://www.shiksha.com/college/isb-mohali-indian-school-of-business-51886",
    "https://www.shiksha.com/university/swami-vivekananda-university-barrackpore-kolkata-150037",
    "https://www.shiksha.com/college/lotus-business-school-punawale-pune-26632",
    "https://www.shiksha.com/university/rayat-bahra-university-mohali-47305",
    "https://www.shiksha.com/college/xavier-school-of-human-resource-management-xavier-university-bhubaneswar-54278",
    "https://www.shiksha.com/college/school-of-management-studies-university-of-hyderabad-sms-hyderabad-c-r-rao-road-21107",
    "https://www.shiksha.com/college/tula-s-institute-dehradun-33002",
    "https://www.shiksha.com/college/jankidevi-bajaj-institute-of-management-studies-jdbims-santacruz-west-mumbai-13614",
    "https://www.shiksha.com/college/lead-college-of-management-palakkad-43312",
    "https://www.shiksha.com/college/christ-college-of-engineering-and-technology-pondicherry-43302",
    "https://www.shiksha.com/college/galgotias-business-school-greater-noida-24415",
    "https://www.shiksha.com/college/invertis-institute-of-management-studies-bareilly-4322",
    "https://www.shiksha.com/college/rajarshi-shahu-college-of-engineering-pune-tathawade-25081",
    "https://www.shiksha.com/college/institute-of-marketing-and-management-delhi-57759",
    "https://www.shiksha.com/college/ami-pune-arham-adhyan-management-institute-211425",
    "https://www.shiksha.com/college/wesley-p-g-college-secunderabad-62317",
    "https://www.shiksha.com/college/valia-school-of-management-andheri-west-mumbai-156195",
    "https://www.shiksha.com/college/dr-n-g-p-institute-of-technology-coimbatore-43115",
    "https://www.shiksha.com/college/pigm-indore-211629",
    "https://www.shiksha.com/college/sri-sairam-engineering-college-tambaram-sanatorium-chennai-36828",
    "https://www.shiksha.com/college/akemi-business-school-tathawade-pune-36300",
    "https://www.shiksha.com/college/rit-roorkee-school-of-management-216059",
    "https://www.shiksha.com/college/mesa-school-of-business-adugodi-bangalore-214001",
    "https://www.shiksha.com/college/kanpur-institute-of-technology-29740",
    "https://www.shiksha.com/college/bnmit-school-of-management-banashankari-bangalore-236896",
    "https://www.shiksha.com/college/gyan-ganga-college-of-technology-ggct-jabalpur-43346",
    "https://www.shiksha.com/college/dr-d-y-patil-institute-of-management-studies-nigdi-pune-270",
    "https://www.shiksha.com/college/institute-for-future-education-entrepreneurship-and-leadership-karla-pune-45420",
    "https://www.shiksha.com/college/g-h-raisoni-institute-of-management-and-research-pune-wagholi-53254",
    "https://www.shiksha.com/college/gl-bajaj-group-of-institutions-glbgi-mathura-48815",
    "https://www.shiksha.com/university/hemvati-nandan-bahuguna-garhwal-university-uttarakhand-other-49879",
    "https://www.shiksha.com/college/international-institute-of-management-and-human-resource-development-sai-balaji-education-society-hinjewadi-pune-30165",
    "https://www.shiksha.com/university/svu-shri-venkateshwara-university-uttar-pradesh-other-42914",
    "https://www.shiksha.com/college/prin-n-g-naralkar-institute-of-career-development-and-research-shaniwar-peth-pune-23919",
    "https://www.shiksha.com/college/dr-ambedkar-institute-of-technology-ait-bangalore-mallathalli-19927",
    "https://www.shiksha.com/college/shri-shankaracharya-institute-of-professional-management-and-technology-raipur-37147",
    "https://www.shiksha.com/college/mohamed-sathak-college-of-arts-and-science-mscas-sholinganallur-chennai-23701",
    "https://www.shiksha.com/college/shri-ramswaroop-memorial-college-of-engineering-and-management-lucknow-26458",
    "https://www.shiksha.com/college/dhaanish-ahmed-college-of-engineering-padappai-chennai-38299",
    "https://www.shiksha.com/college/b-n-bahadur-institute-of-management-sciences-mysore-60431",
    "https://www.shiksha.com/college/maharanis-commerce-and-management-college-for-women-mysore-69027",
    "https://www.shiksha.com/college/progressive-education-society-rsquo-s-modern-institute-of-business-management-mibm-pune-shivaji-nagar-38209",
    "https://www.shiksha.com/college/soim-school-of-innovation-and-management-hyderabad-208817",
    "https://www.shiksha.com/university/srm-institute-of-science-and-technology-chennai-vadapalani-campus-51999",
    "https://www.shiksha.com/college/pravin-dalal-school-of-entrepreneurship-and-family-business-management-nmims-mumbai-vile-parle-west-150053",
    "https://www.shiksha.com/college/universal-ai-university-karjat-mumbai-33323",
    "https://www.shiksha.com/university/srm-institute-of-science-and-technology-delhi-ncr-campus-ghaziabad-47486",
    "https://www.shiksha.com/college/apollo-institute-of-hospital-administration-jubilee-hills-hyderabad-24457",
    "https://www.shiksha.com/college/delhi-technological-university-east-delhi-vivek-vihar-65089",
    "https://www.shiksha.com/college/school-of-management-d-g-vaishnav-college-dgvc-arumbakkam-chennai-31492",
    "https://www.shiksha.com/college/isab-greater-noida-24390",
    "https://www.shiksha.com/university/siddhartha-academy-of-higher-education-deemed-to-be-university-formerly-vr-siddhartha-engineering-college-vijayawada-21486",
    "https://www.shiksha.com/college/gmit-gm-institute-of-technology-davangere-43269",
    "https://www.shiksha.com/college/asm-apeejay-school-of-management-dwarka-delhi-28136",
    "https://www.shiksha.com/college/st-claret-college-jalahalli-bangalore-51588",
    "https://www.shiksha.com/college/institute-of-information-technology-management-janakpuri-delhi-22302",
    "https://www.shiksha.com/college/ajay-kumar-garg-institute-of-management-ghaziabad-29797",
    "https://www.shiksha.com/college/rics-school-of-built-environment-amity-university-noida-36312",
    "https://www.shiksha.com/college/poona-institute-of-management-sciences-and-entrepreneurship-camp-pune-22295",
    "https://www.shiksha.com/college/rukmini-devi-institute-of-advanced-studies-rohini-delhi-28296",
    "https://www.shiksha.com/college/hpu-business-school-himachal-pradesh-university-shimla-37245",
    "https://www.shiksha.com/university/kaziranga-university-jorhat-42910",
    "https://www.shiksha.com/college/swami-vivekananda-institute-of-management-and-computer-science-sonarpur-kolkata-33277",
    "https://www.shiksha.com/college/national-institute-of-technology-jalandhar-24247",
    "https://www.shiksha.com/college/international-institute-of-professional-studies-devi-ahilya-vishwavidhyalaya-indore-37152",
    "https://www.shiksha.com/college/chetana-s-ramprasad-khandelwal-institute-of-management-and-research-bandra-east-mumbai-19255",
    "https://www.shiksha.com/college/dr-d-y-patil-institute-of-management-talegaon-dabhade-pune-36824",
    "https://www.shiksha.com/university/sharnbasva-university-gulbarga-60720",
    "https://www.shiksha.com/university/d-y-patil-international-university-pune-56973",
    "https://www.shiksha.com/university/cmr-university-bangalore-47389",
    "https://www.shiksha.com/university/auro-university-surat-32951",
    "https://www.shiksha.com/college/ips-business-school-jaipur-28553",
    "https://www.shiksha.com/university/tmbu-tilka-manjhi-bhagalpur-university-48203",
    "https://www.shiksha.com/college/panimalar-engineering-college-poonamallee-chennai-20849",
    "https://www.shiksha.com/college/ahmedabad-institute-of-business-management-usmanpura-214965",
    "https://www.shiksha.com/college/sri-venkateswara-college-of-engineering-and-technology-chittoor-37770",
    "https://www.shiksha.com/university/dcrust-deenbandhu-chhotu-ram-university-of-science-and-technology-sonepat-25196",
    "https://www.shiksha.com/college/skn-sinhgad-school-of-business-management-ambegaon-bk-pune-52012",
    "https://www.shiksha.com/college/integral-institute-of-advanced-management-vizag-business-school-iiam-vizag-visakhapatnam-37679",
    "https://www.shiksha.com/university/isbm-university-chhattisgarh-other-50417",
    "https://www.shiksha.com/university/jai-narain-vyas-university-jodhpur-22685",
    "https://www.shiksha.com/university/tumkur-university-23227",
    "https://www.shiksha.com/college/apollo-hospitals-educational-and-research-foundation-jubilee-hills-hyderabad-32900",
    "https://www.shiksha.com/college/issm-business-school-venkateswara-colony-chennai-23760",
    "https://www.shiksha.com/college/centre-for-advanced-studies-in-social-science-and-management-chandigarh-213265",
    "https://www.shiksha.com/college/iiest-shibpur-indian-institute-of-engineering-science-and-technology-howrah-24176",
    "https://www.shiksha.com/college/ramaiah-institute-of-management-studies-rims-mathikere-bangalore-26974",
    "https://www.shiksha.com/university/kakatiya-university-warangal-25211",
    "https://www.shiksha.com/college/atharva-school-of-business-malad-west-mumbai-182401",
    "https://www.shiksha.com/university/g-h-raisoni-university-amravati-151995",
    "https://www.shiksha.com/college/tirpude-institute-of-management-education-nagpur-38021",
    "https://www.shiksha.com/college/tamilnadu-college-of-engineering-coimbatore-25099",
    "https://www.shiksha.com/college/badruka-school-of-management-medchal-hyderabad-215023",
    "https://www.shiksha.com/university/apex-university-jaipur-63261",
    "https://www.shiksha.com/college/driems-university-cuttack-22221",
    "https://www.shiksha.com/college/villa-marie-college-for-women-somajiguda-hyderabad-21511",
    "https://www.shiksha.com/college/dr-b-c-roy-engineering-college-durgapur-25496",
    "https://www.shiksha.com/college/mvsr-engineering-college-hyderabad-20628",
    "https://www.shiksha.com/college/sinhgad-institute-of-management-mba-pune-off-karve-road-1543",
    "https://www.shiksha.com/college/acharya-institute-of-management-and-science-bangalore-105627",
    "https://www.shiksha.com/university/the-apollo-university-chittoor-202871",
    "https://www.shiksha.com/university/gangadhar-meher-university-sambalpur-52803",
    "https://www.shiksha.com/college/alva-s-institute-of-engineering-and-technology-mangalore-60049",
    "https://www.shiksha.com/college/mima-institute-of-management-balewadi-pune-32576",
    "https://www.shiksha.com/university/navrachana-university-vadodara-41387",
    "https://www.shiksha.com/college/gsss-institute-of-engineering-and-technology-for-women-mysore-59461",
    "https://www.shiksha.com/university/atmiya-university-rajkot-58511",
    "https://www.shiksha.com/college/st-joseph-s-college-tiruchirappalli-57473",
    "https://www.shiksha.com/college/department-of-management-studies-dms-bhopal-229858",
    "https://www.shiksha.com/college/simca-sinhgad-institute-of-management-and-computer-application-narhe-pune-48208",
    "https://www.shiksha.com/university/tantia-university-sriganaganagar-42663",
    "https://www.shiksha.com/college/omega-pg-college-ghatkesar-hyderabad-62167",
    "https://www.shiksha.com/college/dunes-college-gandhidham-241190",
    "https://www.shiksha.com/college/sri-guru-gobind-singh-college-of-commerce-university-of-delhi-pitampura-23921",
    "https://www.shiksha.com/college/guru-nanak-institute-of-technology-telangana-ibrahimpatnam-hyderabad-44722",
    "https://www.shiksha.com/college/psgr-krishnammal-college-for-women-coimbatore-22882",
    "https://www.shiksha.com/college/malla-reddy-institute-of-management-mrim-secunderabad-43364",
    "https://www.shiksha.com/college/st-andrews-institute-of-technology-and-management-gurgaon-48608",
    "https://www.shiksha.com/college/shekhawati-group-of-institutions-sikar-30862",
    "https://www.shiksha.com/college/symbiosis-school-of-sports-sciences-symbiosis-international-pune-lavale-53937",
    "https://www.shiksha.com/college/dhole-patil-college-of-engineering-wagholi-pune-27093",
    "https://www.shiksha.com/college/shri-ram-murti-smarak-college-of-engineering-and-technology-bareilly-24942",
    "https://www.shiksha.com/college/cis-foundation-saket-delhi-48657",
    "https://www.shiksha.com/college/vyasa-business-school-swami-vivekananda-yoga-anusandhana-samsthana-university-mysore-road-bangalore-54847",
    "https://www.shiksha.com/college/hrit-group-of-institutions-ghaziabad-24751",
    "https://www.shiksha.com/university/north-eastern-regional-institute-of-science-and-technology-itanagar-54382",
    "https://www.shiksha.com/university/punyashlok-ahilyadevi-holkar-solapur-university-57013",
    "https://www.shiksha.com/college/rungta-college-bhilai-21014",
    "https://www.shiksha.com/college/aurora-s-post-graduate-college-moosarambagh-hyderabad-24825",
    "https://www.shiksha.com/college/g-pullaiah-college-of-engineering-and-technology-kurnool-43188",
    "https://www.shiksha.com/university/ddu-dharmsinh-desai-university-gujarat-other-37125",
    "https://www.shiksha.com/college/rajarambapu-institute-of-technology-kolhapur-24862",
    "https://www.shiksha.com/college/c-v-raman-global-university-bhubaneswar-21724",
    "https://www.shiksha.com/university/shri-vaishnav-vidyapeeth-vishwavidyalaya-indore-48873",
    "https://www.shiksha.com/college/govt-p-g-college-una-43250",
    "https://www.shiksha.com/university/makaut-maulana-abul-kalam-azad-university-of-technology-kolkata-51181",
    "https://www.shiksha.com/college/dr-bhimrao-ambedkar-university-agra-khandari-campus-68375",
    "https://www.shiksha.com/university/rdvv-rani-durgavati-vishwavidyalaya-jabalpur-20980",
    "https://www.shiksha.com/college/nit-agartala-national-institute-of-technology-35298",
    "https://www.shiksha.com/college/amity-global-business-school-kochi-36851",
    "https://www.shiksha.com/college/ganga-institute-of-technology-and-management-punjabi-bagh-delhi-29191",
    "https://www.shiksha.com/university/jodhpur-national-university-38089",
    "https://www.shiksha.com/college/don-bosco-institute-of-management-studies-and-computer-applications-mysore-road-mysore-road-bangalore-53678",
    "https://www.shiksha.com/college/engineering-staff-college-of-india-gachibowli-hyderabad-26282",
    "https://www.shiksha.com/college/rohini-college-of-engineering-and-technology-kanyakumari-53925",
    "https://www.shiksha.com/college/ism-international-school-of-management-patna-34324",
    "https://www.shiksha.com/university/sanskriti-university-mathura-31624",
    "https://www.shiksha.com/college/vidya-vikas-institute-of-engineering-and-technology-vviet-mysore-21500",
    "https://www.shiksha.com/university/rabindranath-tagore-university-bhopal-52700",
    "https://www.shiksha.com/college/abasaheb-garware-institute-of-management-studies-sangli-54507",
    "https://www.shiksha.com/college/greater-noida-institute-of-management-226941",
    "https://www.shiksha.com/college/s-r-luthra-institute-of-management-surat-8375",
    "https://www.shiksha.com/university/gsfc-university-vadodara-54258",
    "https://www.shiksha.com/university/lnmu-lalit-narayan-mithila-university-bihar-other-20508",
    "https://www.shiksha.com/college/rathinam-institute-of-management-coimbatore-47932",
    "https://www.shiksha.com/college/karnataka-college-of-management-yelahanaka-bangalore-48254",
    "https://www.shiksha.com/college/upes-admission-office-nehru-place-delhi-38134",
    "https://www.shiksha.com/university/uniraj-university-of-rajasthan-jaipur-23071",
    "https://www.shiksha.com/university/kalasalingam-academy-of-research-and-education-virudhunagar-37820",
    "https://www.shiksha.com/college/ravenshaw-university-mahanadi-cuttack-204919",
    "https://www.shiksha.com/university/central-university-of-karnataka-karnataka-other-32702",
    "https://www.shiksha.com/college/sibar-sinhgad-institute-of-business-administration-and-research-kondhwa-pune-48200",
    "https://www.shiksha.com/college/st-francis-college-koramangala-bangalore-91839",
    "https://www.shiksha.com/college/balaji-institute-of-technology-management-sri-balaji-university-tathawade-pune-26217",
    "https://www.shiksha.com/university/central-university-of-kerala-kasargode-32704",
    "https://www.shiksha.com/college/s-e-a-college-of-engineering-technology-k-r-puram-bangalore-42857",
    "https://www.shiksha.com/college/college-of-agribusiness-management-uttarakhand-other-19725",
    "https://www.shiksha.com/college/indian-institute-of-digital-education-andheri-west-mumbai-53462",
    "https://www.shiksha.com/college/bsss-institute-of-advanced-studies-bhopal-157051",
    "https://www.shiksha.com/college/pragati-mahavidyalaya-pmv-hyderabad-koti-32374",
    "https://www.shiksha.com/college/nagpur-institute-of-technology-42631",
    "https://www.shiksha.com/college/dpg-degree-college-dpgdc-gurgaon-47298",
    "https://www.shiksha.com/college/st-xavier-s-college-tirunelveli-140793",
    "https://www.shiksha.com/college/alard-university-hinjewadi-pune-32549",
    "https://www.shiksha.com/college/maharaja-institute-of-technology-mysore-59149",
    "https://www.shiksha.com/college/r-a-podar-institute-of-management-jaipur-56915",
    "https://www.shiksha.com/college/b-n-m-institute-of-technology-banashankari-bangalore-21997",
    "https://www.shiksha.com/college/arihant-institute-of-management-and-technology-indore-30043",
    "https://www.shiksha.com/university/central-university-of-odisha-orissa-other-32709",
    "https://www.shiksha.com/college/xavier-school-of-sustainability-xavier-university-bhubaneswar-54281",
    "https://www.shiksha.com/college/school-of-business-public-policy-and-social-entrepreneurship-dr-b-r-ambedkar-university-delhi-kashmere-gate-campus-kashmere-gate-58809",
    "https://www.shiksha.com/university/sarala-birla-university-ranchi-61731",
    "https://www.shiksha.com/college/cmr-university-ombr-campus-bangalore-210947",
    "https://www.shiksha.com/university/arunachal-university-of-studies-arunachal-pradesh-other-42884",
    "https://www.shiksha.com/college/r-c-patel-institute-of-pharmaceutical-education-and-research-shirpur-65097",
    "https://www.shiksha.com/university/dhanalakshmi-srinivasan-university-tiruchirappalli-153053",
    "https://www.shiksha.com/college/ganga-institute-of-technology-and-management-jhajjar-36540",
    "https://www.shiksha.com/university/rama-university-kanpur-47222",
    "https://www.shiksha.com/college/rathinam-group-of-institution-powered-by-sunstone-coimbatore-153473",
    "https://www.shiksha.com/college/vivekanandha-college-of-arts-and-science-for-women-vivekanandha-educational-institutions-for-women-namakkal-42662",
    "https://www.shiksha.com/college/faculty-of-engineering-d-y-patil-technical-campus-talsande-kolhapur-56123",
    "https://www.shiksha.com/college/techno-main-salt-lake-salt-lake-city-kolkata-48911",
    "https://www.shiksha.com/university/central-university-of-tamil-nadu-thanjavur-50562",
    "https://www.shiksha.com/college/nalla-narasimha-reddy-education-society-s-group-of-institutions-ghatkesar-87757",
    "https://www.shiksha.com/college/aam-business-school-nungambakkam-chennai-32660",
    "https://www.shiksha.com/college/p-k-technical-campus-khed-pune-47555",
    "https://www.shiksha.com/university/imu-kochi-51899",
    "https://www.shiksha.com/university/bau-birsa-agricultural-university-ranchi-22263",
    "https://www.shiksha.com/college/r-g-kedia-college-of-commerce-koti-hyderabad-31635",
    "https://www.shiksha.com/college/delhi-institute-of-advanced-studies-rohini-48191",
    "https://www.shiksha.com/college/rajiv-gandhi-institute-of-petroleum-technology-amethi-46857",
    "https://www.shiksha.com/college/durgadevi-saraf-global-business-school-malad-west-mumbai-208971",
    "https://www.shiksha.com/college/bhagwan-mahavir-college-of-management-bhagwan-mahavir-university-surat-68695",
    "https://www.shiksha.com/college/psna-college-of-engineering-and-technology-tamil-nadu-other-20917",
    "https://www.shiksha.com/college/dr-g-r-damodaran-college-of-science-coimbatore-52763",
    "https://www.shiksha.com/university/j-c-bose-university-of-science-and-technology-ymca-faridabad-21570",
    "https://www.shiksha.com/university/sikkim-university-gangtok-50664",
    "https://www.shiksha.com/university/rkdf-university-bhopal-42496",
    "https://www.shiksha.com/university/birla-institute-of-technology-mesra-noida-extension-center-51601",
    "https://www.shiksha.com/university/maharishi-university-of-information-technology-noida-campus-48906",
    "https://www.shiksha.com/college/iit-mandi-indian-institute-of-technology-33322",
    "https://www.shiksha.com/college/nehru-institute-of-technology-nit-coimbatore-42725",
    "https://www.shiksha.com/college/gita-gandhi-institute-for-technological-advancement-bhubaneswar-23303",
    "https://www.shiksha.com/university/sri-ramachandra-institute-of-higher-education-and-research-chennai-24265",
    "https://www.shiksha.com/college/naemd-national-academy-of-event-management-and-development-mumbai-goregaon-west-27228",
    "https://www.shiksha.com/university/dr-rajendra-prasad-central-agricultural-university-bihar-other-25125",
    "https://www.shiksha.com/college/sri-sathya-sai-institute-of-higher-learning-anantapur-21288",
    "https://www.shiksha.com/college/indore-management-institute-and-research-centre-64101",
    "https://www.shiksha.com/college/vns-group-of-institutions-bhopal-21542",
    "https://www.shiksha.com/college/karpagam-academy-of-higher-education-kahe-coimbatore-28632",
    "https://www.shiksha.com/college/indian-institute-of-hotel-management-kolkata-salt-lake-city-28741",
    "https://www.shiksha.com/college/rajadhani-business-school-thiruvananthapuram-37025",
    "https://www.shiksha.com/college/st-marys-centenary-degree-college-secunderabad-59279",
    "https://www.shiksha.com/college/university-college-for-women-osmania-university-hyderabad-103815",
    "https://www.shiksha.com/college/maharana-pratap-engineering-college-kanpur-53972",
    "https://www.shiksha.com/college/geeta-university-panipat-53165",
    "https://www.shiksha.com/college/deccan-school-of-management-nampalli-hyderabad-42678",
    "https://www.shiksha.com/college/mp-birla-institute-of-management-race-course-road-bangalore-30827",
    "https://www.shiksha.com/college/malla-reddy-engineering-college-secunderabad-44794",
    "https://www.shiksha.com/college/guru-nanak-institute-of-hotel-management-sodepur-kolkata-34146",
    "https://www.shiksha.com/college/united-institute-of-management-united-group-of-institutions-greater-noida-56173",
    "https://www.shiksha.com/college/vignan-s-nirula-institute-of-technology-and-science-for-women-guntur-62379",
    "https://www.shiksha.com/college/future-institute-of-engineering-and-technology-bareilly-53168",
    "https://www.shiksha.com/college/isc-indian-school-of-commerce-bangalore-vasanth-nagar-63219",
    "https://www.shiksha.com/university/lakshmibai-national-institute-of-physical-education-gwalior-64911",
    "https://www.shiksha.com/college/world-college-of-technology-and-management-gurgaon-26201",
    "https://www.shiksha.com/university/kumaun-university-nainital-52573",
    "https://www.shiksha.com/university/gla-university-greater-noida-campus-228269",
    "https://www.shiksha.com/college/sri-siddhartha-institute-of-management-studies-ssims-tumkur-28265",
    "https://www.shiksha.com/college/k-l-e-society-s-institute-of-management-studies-and-research-klesimsr-hubli-28512",
    "https://www.shiksha.com/college/immanuel-business-school-hyderabad-47701",
    "https://www.shiksha.com/college/canara-bank-school-of-management-studies-jnanabharathi-campus-jnana-bharathi-bangalore-150345",
    "https://www.shiksha.com/university/the-neotia-university-kolkata-48575",
    "https://www.shiksha.com/university/iis-deemed-to-be-university-jaipur-64381",
    "https://www.shiksha.com/college/dhanalakshmi-srinivasan-engineering-college-dsec-tamil-nadu-other-24017",
    "https://www.shiksha.com/college/sahyadri-commerce-and-management-college-shimoga-115547",
    "https://www.shiksha.com/college/g-h-patel-postgraduate-institute-of-business-management-sardar-patel-university-gujarat-other-42999",
    "https://www.shiksha.com/college/aurora-s-pg-college-panjagutta-panjagutta-hyderabad-179997",
    "https://www.shiksha.com/college/community-institute-of-management-studies-jayanagar-bangalore-37018",
    "https://www.shiksha.com/college/st-martin-s-engineering-college-smec-secunderabad-42603",
    "https://www.shiksha.com/college/ajeenkya-dy-patil-university-powered-by-sunstone-lohegaon-pune-202621",
    "https://www.shiksha.com/university/i-k-gujral-punjab-technical-university-ptu-punjab-other-24093",
    "https://www.shiksha.com/college/moodlakatte-institute-of-technology-mit-kundapura-udupi-43174",
    "https://www.shiksha.com/college/mumbai-institute-of-management-and-research-mimr-wadala-43055",
    "https://www.shiksha.com/university/davangere-university-64547",
    "https://www.shiksha.com/college/padmashree-group-of-institutions-nagarbhavi-bangalore-4449",
    "https://www.shiksha.com/college/assam-institute-of-management-aim-assam-guwahati-2971",
    "https://www.shiksha.com/university/noorul-islam-centre-for-higher-education-kanyakumari-1350",
    "https://www.shiksha.com/college/nmam-institute-of-technology-nitte-university-mangalore-34649",
    "https://www.shiksha.com/college/e-g-s-pillay-engineering-college-nagapattinam-19973",
    "https://www.shiksha.com/university/itm-university-raipur-42934",
    "https://www.shiksha.com/college/haridwar-university-roorkee-47378",
    "https://www.shiksha.com/college/vignan-s-institute-of-engineering-for-women-view-visakhapatnam-43358",
    "https://www.shiksha.com/university/mats-university-raipur-37181",
    "https://www.shiksha.com/college/gandhinagar-university-38262",
    "https://www.shiksha.com/college/anna-university-madurai-regional-campus-62009",
    "https://www.shiksha.com/college/srinivas-institute-of-technology-srinivas-group-of-colleges-mangalore-52839",
    "https://www.shiksha.com/college/delhi-technical-campus-greater-noida-61517",
    "https://www.shiksha.com/college/school-of-business-management-csjm-university-kanpur-51673",
    "https://www.shiksha.com/college/mvit-manakula-vinayagar-institute-of-technology-pondicherry-22982",
    "https://www.shiksha.com/college/koshys-group-of-institutions-hennur-bagalur-road-bangalore-33183",
    "https://www.shiksha.com/college/jagdish-sheth-school-of-management-jagsom-karjat-mumbai-64923",
    "https://www.shiksha.com/college/abhijit-kadam-institute-of-management-and-social-sciences-bharati-vidyapeeth-solapur-42937",
    "https://www.shiksha.com/university/veer-kunwar-singh-university-arrah-65701",
    "https://www.shiksha.com/university/rama-devi-women-s-university-bhubaneswar-57037",
    "https://www.shiksha.com/college/school-of-business-sushant-university-gurgaon-38926",
    "https://www.shiksha.com/college/national-college-thane-thane-west-53644",
    "https://www.shiksha.com/college/pailan-college-of-management-and-technology-pcmt-joka-kolkata-24327",
    "https://www.shiksha.com/college/met-asian-management-development-centre-bandra-west-mumbai-47088",
    "https://www.shiksha.com/college/seshadripuram-academy-for-global-excellence-sage-yelahanaka-bangalore-8872",
    "https://www.shiksha.com/college/east-west-group-of-institutions-magadi-road-vishwaneedam-bangalore-26914",
    "https://www.shiksha.com/college/mba-esg-bangalore-btm-1st-stage-53933",
    "https://www.shiksha.com/college/g-h-raisoni-institute-of-engineering-and-technology-nagpur-43110",
    "https://www.shiksha.com/college/raja-bahadur-venkata-rama-reddy-institute-of-technology-hyderabad-62211",
    "https://www.shiksha.com/college/pillai-business-school-navi-mumbai-208737",
    "https://www.shiksha.com/college/acharya-institute-of-graduate-studies-chikkabanavara-lake-bangalore-51954",
    "https://www.shiksha.com/college/yashoda-technical-campus-satara-43224",
    "https://www.shiksha.com/college/sandip-institute-of-technology-and-research-centre-nashik-33253",
    "https://www.shiksha.com/college/kj-s-educational-institute-kondhwa-pune-36114",
    "https://www.shiksha.com/university/muhs-nashik-2878",
    "https://www.shiksha.com/college/kakatiya-institute-of-technology-and-science-warangal-20412",
    "https://www.shiksha.com/college/alliance-institute-of-hotel-management-visakhapatnam-25130",
    "https://www.shiksha.com/college/rics-school-of-built-environment-amity-university-mumbai-panvel-53013",
    "https://www.shiksha.com/college/bharat-institute-of-technology-meerut-19311",
    "https://www.shiksha.com/college/hindu-college-of-management-guntur-62483",
    "https://www.shiksha.com/university/niit-university-neemrana-34582",
    "https://www.shiksha.com/college/suryadatta-institute-of-business-management-and-technology-pune-77073",
    "https://www.shiksha.com/college/jnnie-chennai-61493",
    "https://www.shiksha.com/university/kashmir-university-srinagar-25276",
    "https://www.shiksha.com/college/david-memorial-business-school-tarnaka-hyderabad-26608",
    "https://www.shiksha.com/college/asb-asian-school-of-business-trivandrum-24514",
    "https://www.shiksha.com/university/telangana-university-nizamabad-23421",
    "https://www.shiksha.com/college/marian-institute-of-management-idukki-73463",
    "https://www.shiksha.com/college/hlm-group-of-institutions-ghaziabad-30509",
    "https://www.shiksha.com/university/jain-deemed-to-be-university-kochi-215723",
    "https://www.shiksha.com/college/excel-engineering-college-namakkal-60543",
    "https://www.shiksha.com/college/visakha-institute-of-engineering-and-technology-visakhapatnam-43043",
    "https://www.shiksha.com/college/j-s-kothari-business-school-dadar-west-mumbai-56937",
    "https://www.shiksha.com/university/imu-imu-kolkata-indian-maritime-university-51900",
    "https://www.shiksha.com/university/maharishi-university-of-information-technology-lucknow-67565",
    "https://www.shiksha.com/college/yuvarajas-college-university-of-mysore-24260",
    "https://www.shiksha.com/college/holy-grace-academy-of-management-studies-thrissur-30712",
    "https://www.shiksha.com/college/andhra-loyola-institute-of-engineering-and-technology-vijayawada-42700",
    "https://www.shiksha.com/college/parul-university-goa-south-goa-238430",
    "https://www.shiksha.com/college/geetanjali-institute-of-technical-studies-udaipur-42452",
    "https://www.shiksha.com/college/aristotle-pg-college-ranga-reddy-54524",
    "https://www.shiksha.com/university/academy-of-maritime-education-and-training-chennai-2973",
    "https://www.shiksha.com/college/institute-of-administrative-studies-iasindia-bihar-muzaffarpur-20216",
    "https://www.shiksha.com/college/jyoti-nivas-college-hosur-road-bangalore-33175",
    "https://www.shiksha.com/college/department-of-pg-studies-visvesvaraya-technological-university-mysuru-mysore-51747",
    "https://www.shiksha.com/university/sidho-kanho-birsha-university-purulia-58601",
    "https://www.shiksha.com/university/vikrama-simhapuri-university-nellore-62507",
    "https://www.shiksha.com/college/srk-institute-of-technology-vijayawada-42596",
    "https://www.shiksha.com/college/sri-venkateswara-agricultural-college-acharya-n-g-ranga-agricultural-university-tirupati-106313",
    "https://www.shiksha.com/college/shri-ram-group-of-colleges-muzaffarnagar-60101",
    "https://www.shiksha.com/college/vikas-college-of-engineering-and-technology-vijayawada-43234",
    "https://www.shiksha.com/college/sparsh-global-business-school-greater-noida-204731",
    "https://www.shiksha.com/college/parivarthana-business-school-mysore-215747",
    "https://www.shiksha.com/college/b-s-a-college-of-engineering-and-technology-mathura-24480",
    "https://www.shiksha.com/college/jiet-department-of-management-studies-jiet-group-of-institutions-jodhpur-52293",
    "https://www.shiksha.com/college/xavier-institute-of-management-and-informatics-ximi-jaipur-212617",
    "https://www.shiksha.com/university/shri-mata-vaishno-devi-university-jammu-4350",
    "https://www.shiksha.com/college/angadi-institute-of-technology-and-management-belgaum-42684",
    "https://www.shiksha.com/college/mahaveer-institute-of-science-and-technology-hyderabad-62139",
    "https://www.shiksha.com/college/hyderabad-presidency-college-68715",
    "https://www.shiksha.com/college/priyadarshini-lokmanya-tilak-institute-of-management-studies-and-research-pltimsr-nagpur-1221",
    "https://www.shiksha.com/college/university-business-school-ludhiana-47757",
    "https://www.shiksha.com/college/international-school-of-design-pune-jangali-maharaj-road-63297",
    "https://www.shiksha.com/college/the-vedica-scholars-programme-for-women-delhi-155875",
    "https://www.shiksha.com/college/buddha-institute-of-technology-bit-gorakhpur-48266",
    "https://www.shiksha.com/college/bhagwan-parshuram-institute-of-technology-rohini-delhi-49447",
    "https://www.shiksha.com/college/kamla-nehru-mahavidyalaya-nagpur-11042",
    "https://www.shiksha.com/college/aiems-amruta-institute-of-engineering-management-sciences-bidadi-bangalore-43235",
    "https://www.shiksha.com/college/sasmira-s-business-school-mumbai-147663",
    "https://www.shiksha.com/college/seacom-group-of-colleges-howrah-42580",
    "https://www.shiksha.com/college/samskruti-college-of-engineering-and-technology-ranga-reddy-42746",
    "https://www.shiksha.com/college/rmd-sinhgad-school-of-management-studies-warje-pune-52070",
    "https://www.shiksha.com/college/malla-reddy-engineering-college-and-management-sciences-medchal-hyderabad-62149",
    "https://www.shiksha.com/college/pondicherry-university-karaikal-campus-51053",
    "https://www.shiksha.com/college/ssvps-s-bapusaheb-shivajirao-deore-college-of-engineering-ssvps-s-bsd-coe-dhule-42756",
    "https://www.shiksha.com/university/avantika-university-ujjain-49129",
    "https://www.shiksha.com/college/silver-oak-college-of-aviation-technology-socat-gota-ahmedabad-215645",
    "https://www.shiksha.com/college/cii-school-of-logistics-amity-university-noida-48817",
    "https://www.shiksha.com/college/aradhana-school-of-business-management-hyderabad-62039",
    "https://www.shiksha.com/college/mmm-s-institute-of-management-education-research-and-training-deccan-pune-47122",
    "https://www.shiksha.com/college/abit-ajay-binay-institute-of-technology-cuttack-23310",
    "https://www.shiksha.com/university/khwaja-moinuddin-chishti-urdu-arabi-farsi-university-lucknow-59943",
    "https://www.shiksha.com/college/mata-gujri-college-punjab-other-42651",
    "https://www.shiksha.com/college/vit-business-school-bhopal-209123",
    "https://www.shiksha.com/college/saveetha-school-of-management-chennai-poonamallee-63411",
    "https://www.shiksha.com/college/maratha-mandir-s-babasaheb-gawde-institute-of-management-studies-mumbai-central-mumbai-21701",
    "https://www.shiksha.com/college/icri-institute-of-clinical-research-india-mumbai-andheri-east-32040",
    "https://www.shiksha.com/university/dr-shakuntala-misra-national-rehabilitation-university-lucknow-37240",
    "https://www.shiksha.com/college/lords-institute-of-engineering-and-technology-himayathsagar-hyderabad-23223",
    "https://www.shiksha.com/college/ashoka-business-school-nashik-60279",
    "https://www.shiksha.com/college/rims-rourkela-institute-of-management-studies-24883",
    "https://www.shiksha.com/college/imarticus-learning-andheri-east-mumbai-35242",
    "https://www.shiksha.com/college/ibmr-business-school-hubli-26835",
    "https://www.shiksha.com/university/sabarmati-university-ahmedabad-53851",
    "https://www.shiksha.com/college/sbm-sona-school-of-business-and-management-salem-28268",
    "https://www.shiksha.com/college/nishitha-degree-college-nizamabad-20783",
    "https://www.shiksha.com/college/tolani-motwane-institute-of-management-studies-adipur-30985",
    "https://www.shiksha.com/college/sveri-s-college-of-engineering-pandharpur-solapur-71281",
    "https://www.shiksha.com/college/dr-vithalrao-vikhe-patil-foundation-s-college-of-pharmacy-ahmednagar-147615",
    "https://www.shiksha.com/college/sbrr-mahajana-first-grade-college-mysore-3625",
    "https://www.shiksha.com/college/gitam-school-of-technology-hyderabad-patancheru-51852",
    "https://www.shiksha.com/college/odm-business-school-bhubaneswar-37455",
    "https://www.shiksha.com/college/srinivas-institute-of-management-studies-mangalore-43280",
    "https://www.shiksha.com/university/bodoland-university-assam-other-43347",
    "https://www.shiksha.com/college/grt-institute-of-engineering-and-technology-tiruvallur-chennai-38361",
    "https://www.shiksha.com/college/adhiyamaan-college-of-engineering-hosur-28120",
    "https://www.shiksha.com/college/jagran-institute-of-management-kanpur-23675",
    "https://www.shiksha.com/college/bhai-parmanand-dseu-shakarpur-campus-ii-shakarpur-delhi-64037",
    "https://www.shiksha.com/college/garware-institute-of-career-education-and-development-university-of-mumbai-santacruz-east-20038",
    "https://www.shiksha.com/college/sree-chaitanya-college-of-engineering-karimnagar-42741",
    "https://www.shiksha.com/college/impact-college-patna-145927",
    "https://www.shiksha.com/college/coimbatore-marine-college-21632",
    "https://www.shiksha.com/college/lovely-professional-university-admission-office-connaught-place-delhi-36321",
    "https://www.shiksha.com/college/iilm-academy-of-higher-learning-jaipur-52739",
    "https://www.shiksha.com/college/future-institute-of-engineering-and-management-sonarpur-kolkata-24088",
    "https://www.shiksha.com/college/lal-bahadur-shastri-institute-of-technology-and-management-indore-48822",
    "https://www.shiksha.com/college/aditya-group-of-institutions-yelahanaka-bangalore-40868",
    "https://www.shiksha.com/university/rajiv-gandhi-university-arunachal-pradesh-other-32725",
    "https://www.shiksha.com/college/rameshwaram-institute-of-technology-and-management-lucknow-37442",
    "https://www.shiksha.com/college/vedavyasa-institute-of-technology-kerala-other-42697",
    "https://www.shiksha.com/college/adi-shankara-institute-of-engineering-and-technology-ernakulum-30998",
    "https://www.shiksha.com/college/jntua-college-of-engineering-ananthapuramu-anantapur-46534",
    "https://www.shiksha.com/college/icri-jagannath-university-delhi-rohini-275",
    "https://www.shiksha.com/college/supreme-knowledge-foundation-chandannagar-kolkata-31155",
    "https://www.shiksha.com/college/jmit-seth-jai-parkash-mukand-lal-institute-of-engineering-and-technology-yamuna-nagar-43190",
    "https://www.shiksha.com/university/bhagwant-university-ajmer-bua-38044",
    "https://www.shiksha.com/college/kalam-institute-of-technology-berhampur-57999",
    "https://www.shiksha.com/college/institute-of-finance-banking-and-insurance-maninagar-ahmedabad-29507",
    "https://www.shiksha.com/college/the-yenepoya-institute-of-arts-science-commerce-and-management-yenepoya-deemed-to-be-university-mangalore-186677",
    "https://www.shiksha.com/college/uei-global-pune-shivaji-nagar-33591",
    "https://www.shiksha.com/university/swaminarayan-university-gandhinagar-214855",
    "https://www.shiksha.com/college/baba-institute-of-technology-and-sciences-visakhapatnam-42665",
    "https://www.shiksha.com/college/mit-group-of-institutions-moradabad-25393",
    "https://www.shiksha.com/college/gt-institute-of-management-studies-vishwaneedam-bangalore-67257",
    "https://www.shiksha.com/college/dy-patil-pgdm-institute-akurdi-pune-213013",
    "https://www.shiksha.com/college/inmantec-institutions-ghaziabad-4237",
    "https://www.shiksha.com/college/aditya-institute-of-management-narhe-pune-34290",
    "https://www.shiksha.com/college/r-p-sharma-institute-of-technology-patna-42728",
    "https://www.shiksha.com/university/national-rail-and-transportation-institute-vadodara-63441",
    "https://www.shiksha.com/college/gyan-ganga-institute-of-technology-and-science-jabalpur-57513",
    "https://www.shiksha.com/college/m-d-u-centre-for-professional-and-allied-studies-gurugram-gurgaon-5516",
    "https://www.shiksha.com/college/nehru-institute-of-engineering-and-technology-coimbatore-24916",
    "https://www.shiksha.com/college/sindhi-institute-of-management-sim-hebbal-bangalore-38815",
    "https://www.shiksha.com/college/poornaprajna-institute-of-management-udupi-51786",
    "https://www.shiksha.com/college/vivekananda-global-university-vgu-powered-by-sunstone-jaipur-211359",
    "https://www.shiksha.com/university/north-eastern-hill-university-tura-campus-meghalaya-other-51320",
    "https://www.shiksha.com/college/st-john-college-of-engineering-management-maharashtra-other-59653",
    "https://www.shiksha.com/college/symbiosis-national-aptitude-test-pune-lavale-village-29589",
    "https://www.shiksha.com/college/swami-vivekanand-institute-of-engineering-and-technology-patiala-116837",
    "https://www.shiksha.com/college/ldrp-institute-of-technology-and-research-gandhinagar-38284",
    "https://www.shiksha.com/college/fisat-federal-institute-of-science-and-technology-ernakulum-38607",
    "https://www.shiksha.com/college/echelon-institute-of-technology-faridabad-32493",
    "https://www.shiksha.com/college/sanketika-vidya-parishad-engineering-college-visakhapatnam-42781",
    "https://www.shiksha.com/college/dr-lankapalli-bullayya-college-visakhapatnam-22564",
    "https://www.shiksha.com/university/suresh-gyan-vihar-university-jaipur-24423",
    "https://www.shiksha.com/university/aku-dr-a-p-j-abdul-kalam-university-indore-58213",
    "https://www.shiksha.com/college/vidyalankar-institute-of-international-education-dadar-west-mumbai-34740",
    "https://www.shiksha.com/college/maharani-laxmi-bai-government-college-of-excellence-gwalior-44150",
    "https://www.shiksha.com/college/sjes-college-of-management-studies-old-madras-road-bangalore-47112",
    "https://www.shiksha.com/university/indira-gandhi-university-rewari-64609",
    "https://www.shiksha.com/university/ptsns-university-shahdol-64759",
    "https://www.shiksha.com/college/gb-pant-social-science-institute-gbpssi-allahabad-22582",
    "https://www.shiksha.com/college/ipsr-group-of-institutions-lucknow-48823",
    "https://www.shiksha.com/university/dr-c-v-raman-university-bihar-vaishali-56441",
    "https://www.shiksha.com/college/isttm-business-school-hi-tech-city-hyderabad-33378",
    "https://www.shiksha.com/college/school-of-engineering-and-technology-cmr-university-hennur-bagalur-road-bangalore-52030",
    "https://www.shiksha.com/college/union-christian-college-kerala-other-3739",
    "https://www.shiksha.com/university/gondwana-university-maharashtra-other-58561",
    "https://www.shiksha.com/college/svce-sri-venkateshwara-college-of-engineering-yelahanaka-bangalore-26993",
    "https://www.shiksha.com/college/nirmala-college-of-management-studies-thrissur-147009",
    "https://www.shiksha.com/university/magadh-university-gaya-51659",
    "https://www.shiksha.com/college/pearl-academy-bangalore-residency-road-89391",
    "https://www.shiksha.com/university/lamrin-tech-skills-university-shahid-bhagat-singh-nagar-211135",
    "https://www.shiksha.com/college/kruti-institute-of-technology-and-engineering-kite-chattisgarh-raipur-43036",
    "https://www.shiksha.com/college/mvr-college-of-engineering-and-technology-andhra-pradesh-other-43222",
    "https://www.shiksha.com/college/dr-d-y-patil-institute-of-technology-talegaon-dabhade-pune-36827",
    "https://www.shiksha.com/college/institute-of-product-leadership-hosur-road-bangalore-48684",
    "https://www.shiksha.com/university/swami-vivekananda-yoga-anusandhana-samsthana-bangalore-57875",
    "https://www.shiksha.com/university/itm-university-gwalior-36449",
    "https://www.shiksha.com/college/trinity-college-of-engineering-and-research-kondhwa-pune-52368",
    "https://www.shiksha.com/college/indian-institute-of-digital-education-new-delhi-south-ex-2-212287",
    "https://www.shiksha.com/college/st-wilfred-s-college-of-management-studies-thane-230770",
    "https://www.shiksha.com/college/amrita-sai-institute-of-science-and-technology-andhra-pradesh-other-43244",
    "https://www.shiksha.com/university/monad-university-hapur-42883",
    "https://www.shiksha.com/college/kannur-university-thalassery-campus-203533",
    "https://www.shiksha.com/university/hemchandracharya-north-gujarat-university-gujarat-other-4001",
    "https://www.shiksha.com/college/mahatma-phule-institute-of-management-and-computer-studies-hadapsar-pune-20581",
    "https://www.shiksha.com/college/narayana-engineering-college-nec-nellore-25424",
    "https://www.shiksha.com/college/zeal-institute-of-management-and-computer-application-narhe-pune-64723",
    "https://www.shiksha.com/college/arihant-institute-of-business-management-bavdhan-pune-190521",
    "https://www.shiksha.com/college/himalayan-school-of-management-studies-swami-rama-himalayan-university-dehradun-121595",
    "https://www.shiksha.com/college/international-agribusiness-management-institute-anand-agricultural-university-58367",
    "https://www.shiksha.com/college/rit-rajeev-institute-of-technology-hassan-42677",
    "https://www.shiksha.com/college/national-institute-of-tourism-and-hospitality-management-nithm-gachibowli-hyderabad-20747",
    "https://www.shiksha.com/college/fuel-business-school-pirangut-pune-213031",
    "https://www.shiksha.com/college/srit-sri-ramakrishna-institute-of-technology-coimbatore-42551",
    "https://www.shiksha.com/college/apoorva-institute-of-management-and-sciences-karimnagar-48201",
    "https://www.shiksha.com/college/indian-institute-of-finance-greater-noida-3253",
    "https://www.shiksha.com/college/nehru-college-of-management-coimbatore-24922",
    "https://www.shiksha.com/university/the-icfai-university-jharkhand-ranchi-38096",
    "https://www.shiksha.com/college/vemu-institute-of-technology-chittoor-43106",
    "https://www.shiksha.com/university/amity-university-hyderabad-243688",
    "https://www.shiksha.com/college/dc-school-of-management-and-technology-dcsmat-trivandrum-campus-thiruvananthapuram-3552",
    "https://www.shiksha.com/college/sunder-deep-engineering-college-ghaziabad-25055",
    "https://www.shiksha.com/college/farook-institute-of-management-studies-calicut-30696",
    "https://www.shiksha.com/university/vikram-university-ujjain-23086",
    "https://www.shiksha.com/college/lokmanya-college-satellite-ahmedabad-101475",
    "https://www.shiksha.com/university/madhyanchal-professional-university-bhopal-58839",
    "https://www.shiksha.com/college/annai-college-of-arts-and-science-thanjavur-66497",
    "https://www.shiksha.com/college/grd-institute-of-management-and-technology-dehradun-48711",
    "https://www.shiksha.com/college/maharaja-surajmal-institute-janakpuri-delhi-49395",
    "https://www.shiksha.com/college/iimt-group-of-colleges-meerut-59877",
    "https://www.shiksha.com/college/sims-sanghvi-institute-of-management-and-science-indore-30433",
    "https://www.shiksha.com/university/nehru-gram-bharati-university-kotwa-ngbu-allahabad-38042",
    "https://www.shiksha.com/college/miet-engineering-college-tiruchirappalli-42653",
    "https://www.shiksha.com/college/ramachandra-college-of-engineering-west-godavari-42623",
    "https://www.shiksha.com/college/vasavi-mca-and-mba-college-prakasam-62503",
    "https://www.shiksha.com/college/institute-of-sports-science-and-technology-poonam-pune-28602",
    "https://www.shiksha.com/college/kamla-nehru-group-of-institutions-sultanpur-59719",
    "https://www.shiksha.com/college/mit-group-of-institutes-mahakal-ujjain-4055",
    "https://www.shiksha.com/college/andhra-mahila-sabha-school-of-informatics-osmania-university-hyderabad-37367",
    "https://www.shiksha.com/college/dhanwantari-academy-for-management-studies-bangalore-210985",
    "https://www.shiksha.com/college/dr-sivanthi-aditanar-college-of-engineering-tamil-nadu-other-24256",
    "https://www.shiksha.com/college/sinhgad-institute-of-business-management-chandivali-mumbai-42529",
    "https://www.shiksha.com/college/rvs-institute-of-management-studies-and-research-coimbatore-21024",
    "https://www.shiksha.com/college/asm-institute-of-professional-studies-pune-pimpri-28137",
    "https://www.shiksha.com/college/uma-krishna-shetty-institute-of-management-studies-and-research-kurla-east-mumbai-37634",
    "https://www.shiksha.com/college/subhas-bose-institute-of-hotel-management-rajarhat-kolkata-26958",
    "https://www.shiksha.com/college/synergy-group-of-institutes-synergy-pune-laxminagar-48706",
    "https://www.shiksha.com/university/west-bengal-state-university-kolkata-58423",
    "https://www.shiksha.com/college/vaageswari-college-of-engineering-karimnagar-61359",
    "https://www.shiksha.com/college/aarupadai-veedu-institute-of-technology-paiyanoor-chengalpattu-vinayaka-mission-s-research-foundation-old-mahabalipuram-road-chennai-25013",
    "https://www.shiksha.com/university/des-pune-university-213485",
    "https://www.shiksha.com/college/koustuv-business-school-kbs-bbsr-bhubaneswar-47761",
    "https://www.shiksha.com/university/mizoram-university-aizawl-46862",
    "https://www.shiksha.com/college/cdac-centre-for-development-of-advanced-computing-pashan-pune-50998",
    "https://www.shiksha.com/college/st-berchmans-institute-of-management-studies-bims-kerela-kottayam-31058",
    "https://www.shiksha.com/college/sipna-college-of-engineering-and-technology-amravati-59431",
    "https://www.shiksha.com/university/annamacharya-university-kadapa-227577",
    "https://www.shiksha.com/college/st-albert-s-college-kochi-48345",
    "https://www.shiksha.com/college/dr-panjabrao-deshmukh-institute-of-management-technology-and-research-nagpur-64215",
    "https://www.shiksha.com/college/avc-college-of-engineering-tamil-nadu-other-22444",
    "https://www.shiksha.com/college/auxilium-college-vellore-42786",
    "https://www.shiksha.com/college/srm-pg-college-karimnagar-21313",
    "https://www.shiksha.com/university/acharya-n-g-ranga-agricultural-university-hyderabad-24889",
    "https://www.shiksha.com/college/bharath-college-of-science-and-management-thanjavur-38017",
    "https://www.shiksha.com/college/mesco-institute-of-management-and-computer-sciences-hyderabad-52810",
    "https://www.shiksha.com/university/pt-sundarlal-sharma-open-university-bilaspur-61241",
    "https://www.shiksha.com/college/national-institute-of-management-and-research-studies-andheri-east-mumbai-101553",
    "https://www.shiksha.com/college/k-c-college-of-engineering-and-management-studies-and-research-thane-mumbai-41625",
    "https://www.shiksha.com/college/kiot-knowledge-institute-of-technology-salem-47361",
    "https://www.shiksha.com/college/swami-devi-dyal-group-of-professional-institutions-panchkula-21349",
    "https://www.shiksha.com/college/upes-knowledge-acres-campus-dehradun-62285",
    "https://www.shiksha.com/university/shri-krishna-university-chhatarpur-64781",
    "https://www.shiksha.com/university/kushabhau-thakre-patrakarita-avam-jansanchar-vishwavidyalaya-raipur-63927",
    "https://www.shiksha.com/college/priyadarshini-p-g-college-mba-hyderabad-62191",
    "https://www.shiksha.com/college/r-b-s-college-agra-110295",
    "https://www.shiksha.com/college/gardi-vidyapith-group-of-institutions-rajkot-60095",
    "https://www.shiksha.com/college/ellenki-college-of-engineering-and-technology-patancheru-hyderabad-19976",
    "https://www.shiksha.com/college/bengal-college-of-engineering-and-technology-durgapur-25045",
    "https://www.shiksha.com/college/biyani-institute-of-science-and-management-jaipur-32609",
    "https://www.shiksha.com/college/st-pious-x-degree-and-pg-college-for-women-telangana-other-59283",
    "https://www.shiksha.com/college/govindram-seksaria-institute-of-management-and-research-indore-67807",
    "https://www.shiksha.com/college/ips-academy-institute-of-business-management-and-research-indore-147313",
    "https://www.shiksha.com/college/indian-institute-of-tourism-and-travel-management-noida-37961",
    "https://www.shiksha.com/college/global-institute-of-engineering-and-technology-giet-telangana-ranga-reddy-42564",
    "https://www.shiksha.com/university/nitte-university-mangalore-56671",
    "https://www.shiksha.com/college/sri-chaitanya-technical-campus-telangana-other-62073",
    "https://www.shiksha.com/college/midas-school-of-entrepreneurship-pune-38303",
    "https://www.shiksha.com/college/vidya-dayini-college-of-information-technology-hyderabad-62219",
    "https://www.shiksha.com/college/metas-adventist-college-surat-69131",
    "https://www.shiksha.com/college/centre-for-liberal-and-advanced-studies-sage-university-bhopal-231840",
    "https://www.shiksha.com/college/mcc-boyd-tandon-school-of-business-chennai-215781",
    "https://www.shiksha.com/college/sri-ramakrishna-college-of-arts-and-science-coimbatore-8330",
    "https://www.shiksha.com/university/iec-university-solan-35967",
    "https://www.shiksha.com/college/mother-teresa-pg-college-ranga-reddy-62157",
    "https://www.shiksha.com/college/dr-k-v-subba-reddy-institute-of-technology-kvsrit-kurnool-43355",
    "https://www.shiksha.com/college/pydah-college-of-engineering-and-technology-visakhapatnam-42533",
    "https://www.shiksha.com/college/tist-toc-h-institute-of-science-technology-ernakulum-31077",
    "https://www.shiksha.com/college/astral-institute-of-technology-and-research-astral-indore-43287",
    "https://www.shiksha.com/college/shri-rgp-gujarati-professional-institute-indore-54517",
    "https://www.shiksha.com/college/shridevi-institute-of-engineering-and-technology-tumkur-59163",
    "https://www.shiksha.com/college/sri-meenakshi-government-arts-college-for-women-madurai-68685",
    "https://www.shiksha.com/college/justice-k-s-hegde-institute-of-management-mangalore-34648",
    "https://www.shiksha.com/university/mohammad-ali-jauhar-university-uttar-pradesh-other-38051",
    "https://www.shiksha.com/college/sir-chotu-ram-institute-of-engineering-and-technology-meerut-54558",
    "https://www.shiksha.com/college/grg-school-of-management-studies-for-women-grgsms-coimbatore-30704",
    "https://www.shiksha.com/college/al-ameen-institute-of-management-studies-hosur-road-bangalore-28127",
    "https://www.shiksha.com/college/srisiim-sri-sharada-institute-of-indian-management-research-vasant-kunj-delhi-30619",
    "https://www.shiksha.com/college/sree-dattha-group-of-educational-institutions-ranga-reddy-47423",
    "https://www.shiksha.com/college/pallavi-engineering-college-rangareddy-hyderabad-68345",
    "https://www.shiksha.com/college/mam-college-of-engineering-tiruchirappalli-23776",
    "https://www.shiksha.com/college/iift-kakinada-indian-institute-of-foreign-trade-67499",
    "https://www.shiksha.com/university/sanjivani-university-ahmednagar-225249",
    "https://www.shiksha.com/university/himalayan-university-itanagar-52301",
    "https://www.shiksha.com/university/vijayanagara-sri-krishnadevaraya-university-ballari-64595",
    "https://www.shiksha.com/college/som-lalit-education-and-research-foundation-slerf-navrangpura-ahmedabad-1049",
    "https://www.shiksha.com/college/st-agnes-college-mangalore-64423",
    "https://www.shiksha.com/college/chmm-college-of-advanced-studies-thiruvananthapuram-71067",
    "https://www.shiksha.com/college/r-b-institute-of-management-studies-rbims-thakkar-bapa-ahmedabad-31355",
    "https://www.shiksha.com/college/nalanda-college-patna-51648",
    "https://www.shiksha.com/college/narmada-college-of-management-bharuch-69143",
    "https://www.shiksha.com/college/v-l-b-janakiammal-college-of-arts-and-science-vlbjcas-coimbatore-10852",
    "https://www.shiksha.com/college/mckv-institute-of-engineering-liluah-kolkata-36574",
    "https://www.shiksha.com/college/vizag-institute-of-technology-vit-visakhapatnam-42762",
    "https://www.shiksha.com/college/g-h-raisoni-institute-of-business-management-jalgaon-53331",
    "https://www.shiksha.com/college/new-delhi-institute-for-information-technology-and-management-kalkaji-26886",
    "https://www.shiksha.com/college/khalsa-college-of-technology-and-business-studies-mohali-64995",
    "https://www.shiksha.com/college/lakireddy-bali-reddy-college-of-engineering-krishna-20498",
    "https://www.shiksha.com/college/sheat-college-of-engineering-varanasi-59755",
    "https://www.shiksha.com/college/manpower-development-college-hyderabad-148471",
    "https://www.shiksha.com/college/aravali-college-of-engineering-and-management-faridabad-37140",
    "https://www.shiksha.com/university/graphic-era-hill-university-haldwani-150807",
    "https://www.shiksha.com/university/takshashila-university-villupuram-211837",
    "https://www.shiksha.com/college/dr-d-y-patil-center-for-management-and-research-mba-chikhali-road-pune-64211",
    "https://www.shiksha.com/college/guru-gobind-singh-educational-society-s-technical-campus-bokaro-steel-city-65183",
    "https://www.shiksha.com/college/sushila-suryawanshi-management-institute-of-technology-advancement-amravati-213271",
    "https://www.shiksha.com/college/apeejay-institute-of-management-and-engineering-technical-campus-jalandhar-24788",
    "https://www.shiksha.com/college/sjcet-st-joseph-s-college-of-engineering-and-technology-kottayam-36625",
    "https://www.shiksha.com/college/avs-engineering-college-salem-37543",
    "https://www.shiksha.com/college/indian-institute-of-tourism-and-travel-management-gwalior-25237",
    "https://www.shiksha.com/college/sri-indu-college-of-engineering-and-technology-ranga-reddy-44819",
    "https://www.shiksha.com/college/institute-of-management-education-ghaziabad-295",
    "https://www.shiksha.com/college/anil-neerukonda-institute-of-technology-and-sciences-visakhapatnam-22423",
    "https://www.shiksha.com/college/lmcst-lourdes-matha-college-of-science-and-technology-thiruvananthapuram-24951",
    "https://www.shiksha.com/college/sankalp-business-school-ambegaon-bk-pune-36843",
    "https://www.shiksha.com/university/rayalaseema-university-kurnool-57197",
    "https://www.shiksha.com/college/acharyapuram-agri-business-management-school-greater-noida-226979",
    "https://www.shiksha.com/college/solamalai-college-of-engineering-madurai-20946",
    "https://www.shiksha.com/college/kanpur-institute-of-management-studies-unnao-38004",
    "https://www.shiksha.com/college/icri-jaipur-national-university-jaipur-56521",
    "https://www.shiksha.com/college/pannala-ram-reddy-college-of-business-management-hyderabad-62181",
    "https://www.shiksha.com/college/j-j-college-of-arts-and-science-pudukkottai-72369",
    "https://www.shiksha.com/college/k-k-vigyan-avam-vyavsaik-adhyayan-mahavidyalaya-indore-72537",
    "https://www.shiksha.com/college/dhanalakshmi-srinivasan-college-of-arts-and-science-for-women-tamil-nadu-other-42499",
    "https://www.shiksha.com/college/rajendra-mane-college-of-engineering-and-technology-rmcet-ratnagiri-20959",
    "https://www.shiksha.com/college/madhusudan-institute-of-co-operative-management-bhubaneswar-42988",
    "https://www.shiksha.com/college/aditya-engineering-college-east-godavari-38011",
    "https://www.shiksha.com/college/mewa-vanguard-business-school-jayanagar-bangalore-210965",
    "https://www.shiksha.com/college/m-kumarasamy-college-of-engineering-karur-20536",
    "https://www.shiksha.com/university/mahatma-gandhi-chitrakoot-gramodaya-vishwavidyalaya-mgcgv-madhya-pradesh-other-20578",
    "https://www.shiksha.com/college/cit-ranchi-cambridge-institute-of-technology-47394",
    "https://www.shiksha.com/college/dr-m-c-saxena-group-of-colleges-mcsgoc-lucknow-24074",
    "https://www.shiksha.com/college/doon-business-school-dehradun-admission-office-38577",
    "https://www.shiksha.com/college/institute-of-management-studies-career-development-and-research-ahmednagar-64181",
    "https://www.shiksha.com/college/providence-college-of-engineering-pce-kerala-other-48940",
    "https://www.shiksha.com/college/guru-gobind-singh-foundation-s-guru-gobind-singh-college-of-engineering-and-research-centre-nashik-59747",
    "https://www.shiksha.com/college/matrusri-institute-of-pg-studies-hyderabad-62153",
    "https://www.shiksha.com/college/st-john-s-pg-college-rangareddy-hyderabad-62249",
    "https://www.shiksha.com/college/marian-academy-of-management-studies-ernakulum-73449",
    "https://www.shiksha.com/college/st-george-college-of-management-science-and-nursing-banasavadi-bangalore-35111",
    "https://www.shiksha.com/university/imu-imu-vizag-indian-maritime-university-visakhapatnam-51901",
    "https://www.shiksha.com/college/apeejay-college-of-fine-arts-jalandhar-67321",
    "https://www.shiksha.com/college/sree-rama-engineering-college-tirupati-43228",
    "https://www.shiksha.com/college/vidyasagar-institute-of-management-bhopal-31528",
    "https://www.shiksha.com/college/grv-business-management-academy-ganga-nagar-bangalore-32500",
    "https://www.shiksha.com/college/kgisl-institute-of-technology-kite-coimbatore-49365",
    "https://www.shiksha.com/college/finxl-business-school-baner-pune-213269",
    "https://www.shiksha.com/college/ssbt-s-college-of-engineering-and-technology-jalgaon-21148",
    "https://www.shiksha.com/college/saroj-institute-of-technology-and-management-lucknow-24802",
    "https://www.shiksha.com/college/phonics-university-haridwar-37633",
    "https://www.shiksha.com/college/potti-sriramulu-college-of-engineering-and-technology-vijayawada-60875",
    "https://www.shiksha.com/college/sri-indu-institute-of-management-telangana-other-62207",
    "https://www.shiksha.com/university/jan-nayak-ch-devi-lal-vidyapeeth-jcdv-haryana-other-23179",
    "https://www.shiksha.com/college/gandhi-institute-of-technology-and-management-bhubaneswar-36696",
    "https://www.shiksha.com/college/vivek-college-of-management-technology-bijnaur-uttar-pradesh-other-65535",
    "https://www.shiksha.com/university/gulbarga-university-karnataka-other-38374",
    "https://www.shiksha.com/college/v-v-sangh-s-basaveshwara-institute-of-information-technology-barkatpura-hyderabad-62051",
    "https://www.shiksha.com/college/sjc-institute-of-technology-chikballpura-21210",
    "https://www.shiksha.com/university/manav-rachna-international-institute-of-research-studies-faridabad-52460",
    "https://www.shiksha.com/college/pravara-institute-of-research-and-education-in-natural-and-social-sciences-ahmednagar-64199",
    "https://www.shiksha.com/college/al-barkaat-institute-of-management-studies-aligarh-59859",
    "https://www.shiksha.com/college/aman-bhalla-group-of-institutes-pathankot-56925",
    "https://www.shiksha.com/college/imperial-college-of-engineering-and-research-wagholi-pune-59691",
    "https://www.shiksha.com/college/vaish-college-of-engineering-rohtak-24422",
    "https://www.shiksha.com/college/kingston-engineering-college-vellore-48104",
    "https://www.shiksha.com/college/icri-ajeenkya-dy-patil-university-pune-charholi-budruk-53340",
    "https://www.shiksha.com/college/rathinam-school-of-business-at-tips-global-powered-by-sunstone-coimbatore-211669",
    "https://www.shiksha.com/college/the-american-college-satellite-campus-madurai-215767",
    "https://www.shiksha.com/college/dr-ambedkar-memorial-institute-of-information-technology-and-management-science-damits-rourkela-42994",
    "https://www.shiksha.com/college/reah-school-of-business-management-hyderabad-62213",
    "https://www.shiksha.com/college/pune-vidyarthi-griha-s-college-of-engineering-s-s-dhamankar-institute-of-management-nashik-228509",
    "https://www.shiksha.com/college/d-d-goverdhan-doss-vaishnav-college-arumbakkam-chennai-19788",
    "https://www.shiksha.com/college/fatima-college-fc-madurai-24926",
    "https://www.shiksha.com/college/nethaji-subash-chandra-bose-college-thiruvarur-74049",
    "https://www.shiksha.com/college/malla-reddy-institute-of-technology-secunderabad-42626",
    "https://www.shiksha.com/college/ibmr-ibs-college-bangalore-koramangala-33445",
    "https://www.shiksha.com/college/ashoka-women-s-engineering-college-kurnool-146245",
    "https://www.shiksha.com/college/shrimati-indira-gandhi-college-sigc-tiruchirappalli-21188",
    "https://www.shiksha.com/college/jawaharlal-college-of-engineering-and-technology-palakkad-48310",
    "https://www.shiksha.com/college/dhanalakshmi-srinivasan-college-of-engineering-and-technology-dscet-east-coast-road-chennai-52359",
    "https://www.shiksha.com/college/government-first-grade-college-davanagere-davangere-102515",
    "https://www.shiksha.com/college/mba-esg-adypu-pune-bangalore-211571",
    "https://www.shiksha.com/college/gudlavalleru-engineering-college-andhra-pradesh-other-22613",
    "https://www.shiksha.com/college/arjun-college-of-technology-and-sciences-ranga-reddy-42780",
    "https://www.shiksha.com/university/seacom-skills-university-ssu-west-bengal-other-48708",
    "https://www.shiksha.com/college/uei-global-delhi-rohini-200",
    "https://www.shiksha.com/college/pioneer-institute-of-professional-studies-indore-32371",
    "https://www.shiksha.com/college/vivekananda-institute-of-management-rajajinagar-bangalore-67309",
    "https://www.shiksha.com/college/swayam-siddhi-college-of-management-and-research-sscmr-upper-thane-thane-32948",
    "https://www.shiksha.com/college/rajarshi-shahu-institute-of-management-aurangabad-52831",
    "https://www.shiksha.com/college/aditya-school-of-business-management-mumbai-147807",
    "https://www.shiksha.com/university/aisect-university-hazaribagh-56199",
    "https://www.shiksha.com/college/fr-c-rodrigues-institute-of-management-studies-navi-mumbai-64159",
    "https://www.shiksha.com/university/cblu-bhiwani-64505",
    "https://www.shiksha.com/college/l-j-institute-of-engineering-and-technology-l-j-i-e-t-sarkhej-ahmedabad-38282",
    "https://www.shiksha.com/college/vasireddy-venkatadri-international-technological-university-guntur-52611",
    "https://www.shiksha.com/college/bishop-jerome-institute-kollam-60325",
    "https://www.shiksha.com/university/martin-luther-christian-university-shillong-65317",
    "https://www.shiksha.com/college/institute-of-agribusiness-management-tirupati-acharya-n-g-ranga-agricultural-university-106325",
    "https://www.shiksha.com/college/nest-academy-of-sports-management-nasm-malad-west-mumbai-48937",
    "https://www.shiksha.com/university/gujarat-maritime-university-gandhinagar-64045",
    "https://www.shiksha.com/college/imas-business-school-salt-lake-city-kolkata-224859",
    "https://www.shiksha.com/college/trinity-institute-of-management-and-research-kondhwa-budruk-pune-36116",
    "https://www.shiksha.com/college/cms-institute-of-management-studies-coimbatore-86927",
    "https://www.shiksha.com/college/centre-for-studies-in-rural-management-gujarat-vidyapith-gandhinagar-38035",
    "https://www.shiksha.com/college/shri-madhwa-vadiraja-institute-of-technology-and-management-smvitm-karnataka-other-48259",
    "https://www.shiksha.com/college/lcet-ludhiana-college-of-engineering-and-technology-42854",
    "https://www.shiksha.com/college/proudhadevaraya-institute-of-technology-pdit-karnataka-other-20910",
    "https://www.shiksha.com/college/gojan-school-of-business-and-technology-edapalayam-chennai-42588",
    "https://www.shiksha.com/university/khallikote-university-berhampur-64927",
    "https://www.shiksha.com/college/dattakala-institute-pune-88561",
    "https://www.shiksha.com/college/indian-institute-of-sustainability-ahmedabad-203797",
    "https://www.shiksha.com/college/st-johns-institute-of-science-and-technology-hyderabad-62247",
    "https://www.shiksha.com/college/chintamanrao-institute-of-management-development-and-research-cimdr-maharashtra-sangli-11843",
    "https://www.shiksha.com/college/khalsa-college-amritsar-25386",
    "https://www.shiksha.com/college/kec-kavery-engineering-college-salem-42732",
    "https://www.shiksha.com/college/psn-college-of-engineering-and-technology-tirunelveli-24034",
    "https://www.shiksha.com/college/r-m-dhariwal-sinhgad-management-school-taluka-shirur-pune-48199",
    "https://www.shiksha.com/college/institute-of-professional-studies-and-research-ipsar-cuttack-31089",
    "https://www.shiksha.com/college/ilam-jagannath-university-delhi-nehru-place-39551",
    "https://www.shiksha.com/college/rns-first-grade-college-bca-bba-b-com-bangalore-69485",
    "https://www.shiksha.com/college/institute-of-productivity-and-management-ghaziabad-25551",
    "https://www.shiksha.com/university/snu-sai-nath-university-ranchi-37265",
    "https://www.shiksha.com/university/avinashilingam-institute-for-home-science-and-higher-education-for-women-coimbatore-64335",
    "https://www.shiksha.com/college/pa-college-of-engineering-mangalore-25146",
    "https://www.shiksha.com/college/institute-of-logistics-and-aviation-management-bangalore-indiranagar-39554",
    "https://www.shiksha.com/college/manel-srinivas-nayak-institute-of-management-mangalore-69397",
    "https://www.shiksha.com/college/gopalan-college-of-commerce-bangalore-186323",
    "https://www.shiksha.com/college/sree-vidyanikethan-institute-of-management-tirupati-25480",
    "https://www.shiksha.com/college/st-wilfreds-p-g-college-jaipur-48070",
    "https://www.shiksha.com/college/mar-athanasios-college-for-advanced-studies-macfast-pathanamthitta-51912",
    "https://www.shiksha.com/university/niftem-national-institute-of-food-technology-entrepreneurship-and-management-sonepat-49399",
    "https://www.shiksha.com/university/motherhood-university-roorkee-50699",
    "https://www.shiksha.com/college/city-premier-college-nagpur-71237",
    "https://www.shiksha.com/college/pvg-s-college-of-engineering-and-technology-and-g-k-pate-wani-institute-of-management-parvati-paytha-pune-20921",
    "https://www.shiksha.com/college/modern-institute-of-technology-and-management-bhubaneswar-34322",
    "https://www.shiksha.com/college/disha-institute-of-management-and-technology-raipur-28172",
    "https://www.shiksha.com/college/c-k-college-of-engineering-technology-cuddalore-60467",
    "https://www.shiksha.com/college/sjb-college-of-management-studies-bangalore-111579",
    "https://www.shiksha.com/college/ct-group-of-institutions-north-campus-jalandhar-3150",
    "https://www.shiksha.com/university/makhanlal-chaturvedi-national-university-of-journalism-and-communication-bhopal-53518",
    "https://www.shiksha.com/college/j-d-c-bytco-institute-of-management-studies-and-research-nashik-4523",
    "https://www.shiksha.com/college/zeal-institute-of-business-administration-computer-application-and-research-narhe-pune-64695",
    "https://www.shiksha.com/college/j-s-s-dental-college-and-hospital-jss-academy-of-higher-education-and-research-mysore-58549",
    "https://www.shiksha.com/college/snd-college-of-engineering-research-center-nashik-59729",
    "https://www.shiksha.com/college/ludhiana-group-of-colleges-42793",
    "https://www.shiksha.com/college/anantha-lakshmi-institute-of-technology-and-sciences-anantapur-46395",
    "https://www.shiksha.com/college/ahalia-school-of-management-palakkad-68657",
    "https://www.shiksha.com/college/chikkanna-government-arts-college-tirupur-71207",
    "https://www.shiksha.com/college/sant-samarth-institute-of-management-hyderabad-148489",
    "https://www.shiksha.com/college/roland-institute-of-technology-berhampur-61381",
    "https://www.shiksha.com/college/south-point-institute-of-technology-management-sonepat-40381",
    "https://www.shiksha.com/college/dadi-institute-of-engineering-and-technology-visakhapatnam-43058",
    "https://www.shiksha.com/college/g-s-college-of-commerce-wardha-64479",
    "https://www.shiksha.com/college/gautam-group-of-colleges-hamirpur-h-p-68423",
    "https://www.shiksha.com/college/scm-hub-kochi-26825",
    "https://www.shiksha.com/college/hbs-hallmark-business-school-tiruchirappalli-48189",
    "https://www.shiksha.com/college/rajaram-shinde-college-of-engineering-mandar-education-society-ratnagiri-20950",
    "https://www.shiksha.com/university/prist-university-deemed-to-be-university-thanjavur-26480",
    "https://www.shiksha.com/college/accman-institute-of-management-greater-noida-29017",
    "https://www.shiksha.com/college/ngf-college-of-engineering-and-technology-faridabad-32561",
    "https://www.shiksha.com/college/loyola-business-school-sanjay-nagar-bangalore-48828",
    "https://www.shiksha.com/college/st-vincent-p-g-college-ghatkesar-hyderabad-62295",
    "https://www.shiksha.com/university/eternal-university-himachal-pradesh-other-38025",
    "https://www.shiksha.com/college/ssr-institute-of-management-and-research-ssrimr-silvassa-47976",
    "https://www.shiksha.com/university/mangalayatan-university-jabalpur-63615",
    "https://www.shiksha.com/college/nbn-sinhgad-school-of-management-studies-ambegaon-bk-pune-52013",
    "https://www.shiksha.com/college/alluri-institute-of-management-sciences-warangal-62341",
    "https://www.shiksha.com/college/terna-engineering-college-navi-mumbai-24776",
    "https://www.shiksha.com/college/iimt-group-of-institutions-varanasi-27882",
    "https://www.shiksha.com/college/international-school-of-management-sciences-isms-kanakapura-road-bangalore-36315",
    "https://www.shiksha.com/college/prestige-institute-of-engineering-management-and-research-indore-58595",
    "https://www.shiksha.com/college/college-of-engineering-and-rural-technology-meerut-19747",
    "https://www.shiksha.com/college/st-bosco-college-of-management-lucknow-31515",
    "https://www.shiksha.com/college/bansal-institute-of-engineering-and-technology-biet-lucknow-48293",
    "https://www.shiksha.com/college/p-s-v-college-of-engineering-and-technology-tamil-nadu-other-43285",
    "https://www.shiksha.com/college/dayanand-academy-of-management-studies-dams-kanpur-28116",
    "https://www.shiksha.com/college/glf-business-school-salt-lake-city-kolkata-49065",
    "https://www.shiksha.com/college/sri-sathya-sai-institute-of-higher-learning-muddenahalli-chikkaballapur-bangalore-64721",
    "https://www.shiksha.com/college/the-east-point-college-of-higher-education-bangalore-69691",
    "https://www.shiksha.com/college/international-school-of-business-studies-gurgaon-180889",
    "https://www.shiksha.com/college/indore-international-college-157113",
    "https://www.shiksha.com/college/iilm-institute-for-business-and-management-gurgaon-27864",
    "https://www.shiksha.com/college/krishna-group-of-institutions-kanpur-37439",
    "https://www.shiksha.com/university/siddharth-university-uttar-pradesh-other-59051",
    "https://www.shiksha.com/college/praxis-tech-school-kolkata-salt-lake-city-213659",
    "https://www.shiksha.com/college/aditya-college-of-engineering-andhra-pradesh-other-37548",
    "https://www.shiksha.com/college/international-school-of-hospitality-management-salt-lake-city-kolkata-56013",
    "https://www.shiksha.com/university/karnataka-state-akkamahadevi-women-s-university-bijapur-58779",
    "https://www.shiksha.com/college/vanita-vishram-women-s-university-surat-69309",
    "https://www.shiksha.com/college/university-evening-college-mangalore-184897",
    "https://www.shiksha.com/college/hindustan-institute-of-technology-and-management-agra-89375",
    "https://www.shiksha.com/college/arihant-group-of-institutes-camp-campus-camp-pune-34516",
    "https://www.shiksha.com/college/darshan-university-rajkot-60127",
    "https://www.shiksha.com/university/the-icfai-university-meghalaya-meghalaya-other-42924",
    "https://www.shiksha.com/college/people-institute-of-management-studies-kasargode-74417",
    "https://www.shiksha.com/college/kiet-east-godavari-46540",
    "https://www.shiksha.com/college/baba-farid-college-baba-farid-group-of-institutions-bathinda-52971",
    "https://www.shiksha.com/college/rayat-bahra-university-powered-by-sunstone-mohali-151293",
    "https://www.shiksha.com/college/al-quarmoshi-institute-of-business-management-aqibm-hyderabad-barkas-19489",
    "https://www.shiksha.com/college/national-institute-of-business-management-thiruvanmiyur-chennai-25169",
    "https://www.shiksha.com/college/noble-university-junagadh-60125",
    "https://www.shiksha.com/college/shalby-academy-prahlad-nagar-ahmedabad-105883",
    "https://www.shiksha.com/college/jagruti-p-g-college-narayanguda-hyderabad-21738",
    "https://www.shiksha.com/college/aimfill-international-jayanagar-bangalore-37095",
    "https://www.shiksha.com/college/madhav-institute-of-technology-and-science-gwalior-38165",
    "https://www.shiksha.com/college/elijah-institute-of-management-studies-elims-thrissur-51861",
    "https://www.shiksha.com/college/isl-engineering-college-hyderabad-60557",
    "https://www.shiksha.com/college/gems-b-school-tirupati-64127",
    "https://www.shiksha.com/college/shankarrao-dhawad-polytechnic-nagpur-147565",
    "https://www.shiksha.com/college/nagindas-khandwala-college-malad-west-mumbai-64527",
    "https://www.shiksha.com/college/lotus-institute-of-management-lim-bareilly-30545",
    "https://www.shiksha.com/university/sikkim-professional-university-gangtok-62575",
    "https://www.shiksha.com/college/dr-g-d-pol-foundation-s-ymt-college-of-management-navi-mumbai-31446",
    "https://www.shiksha.com/college/ilam-ahmedabad-institute-of-logistics-and-aviation-management-ahmedabad-thaltej-56613",
    "https://www.shiksha.com/university/raiganj-university-uttar-dinajpur-57159",
    "https://www.shiksha.com/college/iims-international-institute-of-management-sciences-uluberia-palara-kolkata-20329",
    "https://www.shiksha.com/college/techno-international-new-town-rajarhat-kolkata-48632",
    "https://www.shiksha.com/university/radha-govind-university-ramgarh-64525",
    "https://www.shiksha.com/college/patel-group-of-institutions-banglore-bellandur-bangalore-67271",
    "https://www.shiksha.com/college/indu-devi-ranjeet-kumar-prakash-professional-college-vaishali-146507",
    "https://www.shiksha.com/college/indo-asian-academy-group-of-institutions-kalyan-nagar-bangalore-470",
    "https://www.shiksha.com/university/north-east-frontier-technical-university-arunachal-pradesh-other-64565",
    "https://www.shiksha.com/college/hari-shankar-singhania-school-of-business-jaipur-214659",
    "https://www.shiksha.com/college/khalsa-institute-of-management-and-technology-for-women-ludhiana-24148",
    "https://www.shiksha.com/college/mcmat-marthoma-college-of-management-and-technology-ernakulum-30802",
    "https://www.shiksha.com/college/academy-of-hospital-administration-noida-35057",
    "https://www.shiksha.com/college/gct-gnanamani-college-of-technology-namakkal-42721",
    "https://www.shiksha.com/college/azad-college-of-engineering-and-technology-azadcet-moinabad-hyderabad-43189",
    "https://www.shiksha.com/college/international-school-of-design-andheri-west-andheri-west-mumbai-50269",
    "https://www.shiksha.com/college/rajdhani-college-bhubaneswar-58639",
    "https://www.shiksha.com/college/ta-pai-management-institute-yelahanaka-bangalore-182285",
    "https://www.shiksha.com/college/albertian-institute-of-management-kochi-13653",
    "https://www.shiksha.com/college/ifet-college-of-engineering-villupuram-chennai-20164",
    "https://www.shiksha.com/college/samata-college-visakhapatnam-43313",
    "https://www.shiksha.com/college/kmct-college-of-engineering-kozhikode-60433",
    "https://www.shiksha.com/college/bon-secours-college-for-women-thanjavur-71037",
    "https://www.shiksha.com/college/gaya-college-194977",
    "https://www.shiksha.com/college/kannur-university-dr-p-k-rajan-memorial-campus-kasargode-203583",
    "https://www.shiksha.com/college/nef-college-of-management-technology-guwahati-4310",
    "https://www.shiksha.com/college/vivekanadha-college-of-engineering-for-women-vivekanandha-educational-institutions-for-women-namakkal-42641",
    "https://www.shiksha.com/college/rpiit-technical-campus-karnal-34345",
    "https://www.shiksha.com/university/william-carey-university-shillong-64857",
    "https://www.shiksha.com/university/south-asian-university-sau-delhi-35661",
    "https://www.shiksha.com/college/sasurie-college-of-engineering-tirupur-42814",
    "https://www.shiksha.com/college/itm-financial-markets-institute-navi-mumbai-23404",
    "https://www.shiksha.com/college/himalayan-institute-of-technology-dehradun-52663",
    "https://www.shiksha.com/college/gvr-s-college-of-engineering-technology-guntur-60783",
    "https://www.shiksha.com/college/sri-padmavathi-studies-of-computer-sciences-and-technology-tirupati-68839",
    "https://www.shiksha.com/university/d-y-patil-education-society-kolhapur-231594",
    "https://www.shiksha.com/college/haryana-engineering-college-yamuna-nagar-33281",
    "https://www.shiksha.com/college/fbs-fisat-business-school-kochi-38329",
    "https://www.shiksha.com/college/shri-mangalam-college-of-management-studies-noida-39142",
    "https://www.shiksha.com/college/gonna-institute-of-information-technology-and-sciences-visakhapatnam-60648",
    "https://www.shiksha.com/college/doaba-group-of-colleges-nawanshahr-campus-nawanshahar-66209",
    "https://www.shiksha.com/college/shayona-institute-of-business-management-ahmedabad-69195",
    "https://www.shiksha.com/college/tkws-institute-of-banking-and-finance-rajendra-nagar-delhi-33056",
    "https://www.shiksha.com/college/shree-h-n-shukla-group-of-colleges-rajkot-37134",
    "https://www.shiksha.com/college/vision-p-g-college-ghatkesar-hyderabad-62283",
    "https://www.shiksha.com/university/dr-preeti-global-university-indore-216077",
    "https://www.shiksha.com/college/shri-vishnu-engineering-college-for-women-west-godavari-21184",
    "https://www.shiksha.com/college/mailam-engineering-college-tamil-nadu-other-22775",
    "https://www.shiksha.com/college/national-institute-of-financial-management-faridabad-27993",
    "https://www.shiksha.com/college/n-r-institute-of-business-management-nribm-ellis-bridge-ahmedabad-37055",
    "https://www.shiksha.com/university/abhilashi-university-mandi-56079",
    "https://www.shiksha.com/college/university-college-of-engineering-bharathidasan-institute-of-technology-tiruchirappalli-anna-university-61449",
    "https://www.shiksha.com/college/dr-bv-hiray-college-of-management-and-research-centre-malegaon-nashik-64367",
    "https://www.shiksha.com/college/amritsar-group-of-colleges-24780",
    "https://www.shiksha.com/college/sri-sri-institute-of-management-studies-margao-28261",
    "https://www.shiksha.com/college/swarna-bharathi-institute-of-science-and-technology-sbist-khammam-37786",
    "https://www.shiksha.com/college/luxury-connect-business-school-gurgaon-48612",
    "https://www.shiksha.com/university/sardarkrushinagar-dantiwada-agricultural-university-banaskantha-65939",
    "https://www.shiksha.com/college/u-d-pathrikar-institute-of-management-aurangabad-209025",
    "https://www.shiksha.com/university/baba-ghulam-shah-badshah-university-jammu-25269",
    "https://www.shiksha.com/college/nims-nehru-institute-of-management-studies-coimbatore-28608",
    "https://www.shiksha.com/university/sri-chandrasekharendra-saraswathi-viswa-mahavidyalaya-chennai-36961",
    "https://www.shiksha.com/college/poddar-business-school-jaipur-213813",
    "https://www.shiksha.com/college/conspi-academy-of-management-studies-thiruvananthapuram-30686",
    "https://www.shiksha.com/college/nandini-nagar-technical-campus-gonda-60007",
    "https://www.shiksha.com/college/udaya-school-of-engineering-kanyakumari-61753",
    "https://www.shiksha.com/college/avanthi-degree-and-pg-college-kachiguda-hyderabad-64491",
    "https://www.shiksha.com/college/sharda-school-of-business-studies-agra-225419",
    "https://www.shiksha.com/college/uei-global-chandigarh-33592",
    "https://www.shiksha.com/college/babu-banarsi-das-institute-of-technology-ghaziabad-37647",
    "https://www.shiksha.com/college/avanthi-p-g-and-research-academy-hyderabad-62033",
    "https://www.shiksha.com/college/institute-of-management-studies-roorkee-1813",
    "https://www.shiksha.com/college/syed-ammal-engineering-college-saec-ramanathapuram-madurai-21355",
    "https://www.shiksha.com/college/pet-engineering-college-tirunelveli-22864",
    "https://www.shiksha.com/university/st-peter-s-institute-of-higher-education-and-research-chennai-24046",
    "https://www.shiksha.com/college/modern-institute-of-technology-and-research-centre-mitrc-alwar-38899",
    "https://www.shiksha.com/college/institute-of-excellence-in-management-science-hubli-67261",
    "https://www.shiksha.com/college/vijetha-academy-secunderabad-101783",
    "https://www.shiksha.com/university/kerala-university-of-digital-sciences-innovation-and-technology-thiruvananthapuram-154899",
    "https://www.shiksha.com/college/aligarh-college-of-engineering-and-technology-24927",
    "https://www.shiksha.com/college/rustomjee-business-school-dahisar-west-mumbai-26597",
    "https://www.shiksha.com/college/institute-of-technology-and-management-nanded-64269",
    "https://www.shiksha.com/college/sheth-manshukhlal-chhaganlal-college-of-dairy-science-anand-224605",
    "https://www.shiksha.com/college/kvg-college-of-engineering-sullia-20489",
    "https://www.shiksha.com/university/shobhit-university-gangoh-saharanpur-40052",
    "https://www.shiksha.com/college/mar-baselios-institute-of-technology-and-science-kothamangalam-ernakulum-60475",
    "https://www.shiksha.com/college/mount-zion-college-of-engineering-mzce-pathanamthitta-23798",
    "https://www.shiksha.com/college/siitam-sun-international-institute-of-tourism-and-management-hyderabad-ramnagar-33259",
    "https://www.shiksha.com/college/ojaswini-institute-of-management-technology-madhya-pradesh-other-43395",
    "https://www.shiksha.com/college/anwar-ul-uloom-college-for-computer-studies-hyderabad-62031",
    "https://www.shiksha.com/college/dr-h-n-national-college-of-engineering-bangalore-231094",
    "https://www.shiksha.com/college/dbs-global-university-powered-by-emversity-dehradun-237156",
    "https://www.shiksha.com/college/mount-carmel-institute-of-management-for-women-palace-road-bangalore-511",
    "https://www.shiksha.com/college/s-p-more-college-navi-mumbai-26892",
    "https://www.shiksha.com/college/mit-school-of-distance-education-kothrud-pune-44330",
    "https://www.shiksha.com/college/madras-institute-of-fashion-technology-mift-vadapalani-chennai-48722",
    "https://www.shiksha.com/college/sakthi-institute-of-information-and-management-studies-coimbatore-75431",
    "https://www.shiksha.com/college/qis-college-of-engineering-technology-prakasam-20927",
    "https://www.shiksha.com/college/bimt-gurgaon-33251",
    "https://www.shiksha.com/college/meghnad-saha-institute-of-technology-uchhepota-kolkata-42624",
    "https://www.shiksha.com/college/kalyani-charitable-trust-s-k-r-sapkal-college-of-management-studies-nashik-47100",
    "https://www.shiksha.com/college/p-v-k-k-institute-of-technology-anantapur-49351",
    "https://www.shiksha.com/college/mittal-institute-of-technology-bhopal-52764",
    "https://www.shiksha.com/college/nagarjuna-college-of-management-studies-chikballpura-69431",
    "https://www.shiksha.com/college/vimal-jyothi-institute-of-management-and-research-kannur-146997",
    "https://www.shiksha.com/college/santhigiri-institute-of-management-idukki-147013",
    "https://www.shiksha.com/college/st-joseph-s-pg-college-warangal-148475",
    "https://www.shiksha.com/college/wisdom-school-of-management-wsm-powered-by-sunstone-coimbatore-204899",
    "https://www.shiksha.com/college/mes-advanced-institute-of-management-and-technology-kochi-48206",
    "https://www.shiksha.com/college/kalyan-post-graduate-college-bhilai-nagar-durg-72581",
    "https://www.shiksha.com/university/kishkinda-university-ballari-228729",
    "https://www.shiksha.com/college/loyola-institute-of-technology-and-science-lites-kanyakumari-42602",
    "https://www.shiksha.com/college/mantra-school-of-business-management-l-b-nagar-hyderabad-62143",
    "https://www.shiksha.com/college/sunstone-aditya-institute-of-management-narhe-pune-151827",
    "https://www.shiksha.com/college/iilm-graduate-school-of-management-greater-noida-22240",
    "https://www.shiksha.com/college/pr-patil-college-of-engineering-and-technology-prpcet-amravati-36205",
    "https://www.shiksha.com/college/mahendra-institute-of-management-and-technical-studies-orissa-other-37664",
    "https://www.shiksha.com/college/institute-of-tourism-studies-uttar-pradesh-its-lucknow-20316",
    "https://www.shiksha.com/university/capital-university-jharkhand-other-63315",
    "https://www.shiksha.com/college/post-graduate-college-siddipet-medak-139513",
    "https://www.shiksha.com/college/step-harcourt-butler-technological-institute-kanpur-37369",
    "https://www.shiksha.com/college/vidya-college-of-engineering-meerut-42879",
    "https://www.shiksha.com/college/j-m-patel-arts-commerce-and-science-college-bhandara-72385",
    "https://www.shiksha.com/college/chameli-devi-institute-of-professional-studies-indore-157101",
    "https://www.shiksha.com/college/bandhan-school-of-business-birbhum-242334",
    "https://www.shiksha.com/college/sri-krishnadevaraya-institute-of-management-skim-college-anantapur-42996",
    "https://www.shiksha.com/college/kipm-college-of-management-gorakhpur-59945",
    "https://www.shiksha.com/college/holy-mother-p-g-college-hyderabad-62101",
    "https://www.shiksha.com/college/reva-institute-of-science-and-technology-bangalore-69483",
    "https://www.shiksha.com/college/skybird-aviation-hyderabad-ameerpet-51986",
    "https://www.shiksha.com/college/nibe-the-international-business-college-sadashiv-peth-pune-106557",
    "https://www.shiksha.com/college/alpine-institute-of-technology-ujjain-43218",
    "https://www.shiksha.com/college/nilai-institute-of-management-jharkhand-other-43314",
    "https://www.shiksha.com/college/arunachala-college-of-engineering-for-women-tamil-nadu-other-48090",
    "https://www.shiksha.com/college/dr-ram-manohar-lohia-institute-drmli-modinagar-49448",
    "https://www.shiksha.com/college/sri-venkateswara-college-of-engineering-and-technology-thiruvarur-65529",
    "https://www.shiksha.com/college/chadalawada-ramanamma-engineering-college-tirupati-31061",
    "https://www.shiksha.com/college/aiet-appa-institute-of-engineering-and-technology-gulbarga-42853",
    "https://www.shiksha.com/college/vaishnavi-institutes-of-technology-and-science-bhopal-60251",
    "https://www.shiksha.com/college/gourishankar-institute-of-management-sciences-satara-64343",
    "https://www.shiksha.com/college/sri-gaayathri-college-of-management-sciences-warangal-68689",
    "https://www.shiksha.com/university/jagannath-university-jaipur-40379",
    "https://www.shiksha.com/college/abs-academy-of-science-technology-and-management-durgapur-41533",
    "https://www.shiksha.com/college/sagar-institute-of-technology-and-management-sitm-barabanki-uttar-pradesh-other-42611",
    "https://www.shiksha.com/college/university-arts-and-science-college-subedari-kakatiya-university-warangal-210213",
    "https://www.shiksha.com/college/lachoo-memorial-college-of-science-and-technology-jodhpur-20495",
    "https://www.shiksha.com/college/smt-shanti-devi-college-of-management-and-technology-rewari-68627",
    "https://www.shiksha.com/college/rajiv-gandhi-degree-college-andhra-pradesh-andhra-pradesh-other-7818",
    "https://www.shiksha.com/college/bldea-s-a-s-patil-college-of-commerce-autonomous-bijapur-24968",
    "https://www.shiksha.com/college/indo-global-group-of-colleges-mohali-28011",
    "https://www.shiksha.com/college/einstein-academy-of-technology-and-management-bhubaneswar-34312",
    "https://www.shiksha.com/college/presidency-school-of-management-and-computer-sciences-hyderabad-62183",
    "https://www.shiksha.com/college/institute-of-technical-education-research-and-management-akurdi-maharashtra-other-67349",
    "https://www.shiksha.com/college/jyothi-institute-of-commerce-and-management-bangalore-211877",
    "https://www.shiksha.com/college/iilm-college-of-management-studies-greater-noida-30512",
    "https://www.shiksha.com/university/spicer-adventist-university-pune-48421",
    "https://www.shiksha.com/college/kuniya-college-of-management-and-information-technology-kasargode-232366",
    "https://www.shiksha.com/college/bhubaneswar-institute-of-management-and-information-technology-bimit-23510",
    "https://www.shiksha.com/college/allenhouse-institute-of-technology-kanpur-56741",
    "https://www.shiksha.com/college/maharaja-institute-of-technology-thandavapura-mysore-63795",
    "https://www.shiksha.com/college/safety-rise-institute-of-fire-and-safety-management-malad-east-mumbai-70051",
    "https://www.shiksha.com/university/godavari-global-university-rajahmundry-229165",
    "https://www.shiksha.com/college/kasireddy-narayan-reddy-college-of-engineering-and-research-ranga-reddy-62121",
    "https://www.shiksha.com/college/visvesvaraya-technological-university-kalaburagi-karnataka-other-185071",
    "https://www.shiksha.com/university/punjab-engineering-college-chandigarh-3773",
    "https://www.shiksha.com/college/gkm-college-of-engineering-and-technology-gkmcet-tambaram-sanatorium-chennai-20050",
    "https://www.shiksha.com/college/bhai-gurdas-institute-of-engineering-and-technology-sangrur-29003",
    "https://www.shiksha.com/college/khalsa-college-lyallpur-institute-of-management-technology-jalandhar-64593",
    "https://www.shiksha.com/university/sai-university-chennai-152431",
    "https://www.shiksha.com/college/avanthi-s-scientific-technological-and-research-academy-hayat-nagar-hyderabad-46582",
    "https://www.shiksha.com/university/career-point-university-cpur-kota-52853",
    "https://www.shiksha.com/college/sir-issac-newton-arts-and-science-college-nagapattinam-68691",
    "https://www.shiksha.com/college/centre-for-liberal-and-advanced-studies-sage-university-indore-237996",
    "https://www.shiksha.com/college/j-d-women-s-college-jdwc-patna-4536",
    "https://www.shiksha.com/college/lyallpur-khalsa-college-jalandhar-20531",
    "https://www.shiksha.com/college/audisankara-college-of-engineering-and-technology-nellore-46542",
    "https://www.shiksha.com/college/prr-college-of-commerce-and-management-hyderabad-74537",
    "https://www.shiksha.com/college/vathsalya-college-of-business-management-banjara-hills-hyderabad-62303",
    "https://www.shiksha.com/college/c-b-bhandari-jain-college-basavanagudi-bangalore-127927",
    "https://www.shiksha.com/college/hindustan-business-school-marathahalli-bangalore-427",
    "https://www.shiksha.com/college/kalpataru-institute-of-technology-kit-tiptur-tumkur-20415",
    "https://www.shiksha.com/college/narayana-institute-of-management-anantapur-68737",
    "https://www.shiksha.com/college/k-m-m-college-of-arts-and-science-kochi-72555",
    "https://www.shiksha.com/college/scott-christian-college-nagercoil-75671",
    "https://www.shiksha.com/college/goel-institute-of-higher-studies-luckhnow-lucknow-201913",
    "https://www.shiksha.com/university/maharashtra-state-skills-university-mumbai-206197",
    "https://www.shiksha.com/college/mother-teresa-institute-of-science-and-technology-khammam-20675",
    "https://www.shiksha.com/college/odisha-university-of-technology-and-research-bhubaneswar-37899",
    "https://www.shiksha.com/college/bansal-institute-of-science-and-technology-bhopal-59403",
    "https://www.shiksha.com/college/giet-engineering-college-rajahmundry-63779",
    "https://www.shiksha.com/college/srm-degree-and-pg-college-karimnagar-68411",
    "https://www.shiksha.com/college/sambhram-institute-of-technology-jalahalli-bangalore-25126",
    "https://www.shiksha.com/college/shri-guru-sandipani-institute-of-management-ujjain-68613",
    "https://www.shiksha.com/college/sanjivani-institute-of-management-studies-ahmednagar-215795",
    "https://www.shiksha.com/university/maya-devi-university-uttarakhand-other-225271",
    "https://www.shiksha.com/college/rao-bahadur-y-mahabaleswarappa-engineering-college-rymec-karnataka-other-21509",
    "https://www.shiksha.com/college/siwan-engineering-and-technical-institute-seti-siwan-bihar-other-23761",
    "https://www.shiksha.com/college/bhabha-engineering-research-institute-bhopal-43330",
    "https://www.shiksha.com/college/holy-mary-institute-of-technology-and-management-ranga-reddy-62345",
    "https://www.shiksha.com/college/genesis-institute-of-management-and-technology-kasba-kolkata-62983",
    "https://www.shiksha.com/college/lloyd-institute-of-management-and-technology-uttar-pradesh-other-148609",
    "https://www.shiksha.com/college/bright-business-school-hubli-232154",
    "https://www.shiksha.com/college/the-indian-institute-of-financial-planning-jhandewalan-extension-delhi-28037",
    "https://www.shiksha.com/college/kasturi-institute-of-management-kim-coimbatore-34390",
    "https://www.shiksha.com/university/rayat-bahra-professional-university-rbpu-hoshiarpur-47380",
    "https://www.shiksha.com/college/babulal-tarabai-institute-of-research-and-technology-btirt-sagar-48237",
    "https://www.shiksha.com/college/j-k-k-nattraja-college-of-engineering-and-technology-namakkal-54051",
    "https://www.shiksha.com/college/vivekananda-college-of-technology-and-management-aligarh-59063",
    "https://www.shiksha.com/college/st-joseph-s-institute-of-technology-old-mahabalipuram-road-chennai-61315",
    "https://www.shiksha.com/university/sido-kanhu-murmu-university-skmu-jharkhand-other-64763",
    "https://www.shiksha.com/college/d-a-v-college-jalandhar-25378",
    "https://www.shiksha.com/college/college-of-engineering-and-technology-bikaner-46868",
    "https://www.shiksha.com/college/indira-gandhi-sahkari-prabandh-sansthan-lucknow-59907",
    "https://www.shiksha.com/university/malwanchal-university-indore-67421",
    "https://www.shiksha.com/university/medhavi-skills-university-sikkim-sikkim-other-203793",
    "https://www.shiksha.com/university/swami-keshwanand-rajasthan-agricultural-university-skrau-rajasthan-other-4420",
    "https://www.shiksha.com/college/pondicherry-engineering-college-pec-25083",
    "https://www.shiksha.com/college/usha-and-lakshmi-mittal-institute-of-management-kasturba-gandhi-marg-delhi-30488",
    "https://www.shiksha.com/college/eluru-college-of-engineering-and-technology-ecet-eluru-west-godavari-42718",
    "https://www.shiksha.com/college/ganapathy-engineering-collge-warangal-62093",
    "https://www.shiksha.com/university/om-sterling-global-university-hisar-86871",
    "https://www.shiksha.com/university/fs-university-firozabad-214783",
    "https://www.shiksha.com/college/h-k-e-society-s-sln-college-of-engineering-raichur-52567",
    "https://www.shiksha.com/university/maulana-azad-university-jodhpur-65083",
    "https://www.shiksha.com/college/mar-thoma-institute-of-information-technology-kollam-147049",
    "https://www.shiksha.com/college/a-c-patil-college-of-engineering-navi-mumbai-189845",
    "https://www.shiksha.com/college/eva-stalin-business-school-tambaram-sanatorium-chennai-32968",
    "https://www.shiksha.com/college/school-of-business-management-global-education-centre-ranga-reddy-48194",
    "https://www.shiksha.com/university/andhra-university-vizianagaram-campus-51378",
    "https://www.shiksha.com/college/brindavan-group-of-institutions-yelahanaka-bangalore-yelahanaka-54307",
    "https://www.shiksha.com/college/vinayaka-college-of-it-and-business-management-kondapak-telangana-other-62251",
    "https://www.shiksha.com/university/bareilly-international-university-65889",
    "https://www.shiksha.com/college/royal-institute-of-management-and-advanced-studies-ratlam-88033",
    "https://www.shiksha.com/college/university-institute-of-technology-alappuzha-alleppey-114385",
    "https://www.shiksha.com/college/institute-of-business-management-and-agripreneurship-gurgaon-152647",
    "https://www.shiksha.com/college/abes-business-school-ghaziabad-180121",
    "https://www.shiksha.com/college/konark-institute-of-science-and-technology-kist-bhubaneswar-24070",
    "https://www.shiksha.com/college/kt-patil-college-of-engineering-and-technology-osmanabad-maharashtra-other-59605",
    "https://www.shiksha.com/college/mahatma-gandhi-vidyamandir-s-institute-of-management-and-research-nashik-64637",
    "https://www.shiksha.com/university/cluster-university-srinagar-64761",
    "https://www.shiksha.com/college/mulshi-institute-of-business-management-pune-147815",
    "https://www.shiksha.com/college/don-bosco-institute-of-management-guwahati-41973",
    "https://www.shiksha.com/college/maharana-pratap-college-of-technology-institutions-gwalior-43195",
    "https://www.shiksha.com/college/sri-balaji-chockalingam-engineering-college-tamil-nadu-other-53897",
    "https://www.shiksha.com/college/ana-group-of-institutions-bareilly-63245",
    "https://www.shiksha.com/college/jd-school-of-design-powered-by-jd-institute-bangalore-brigade-road-210597",
    "https://www.shiksha.com/university/itm-skills-university-navi-mumbai-213055",
    "https://www.shiksha.com/university/mother-teresa-women-s-university-mtwu-kodaikanal-25236",
    "https://www.shiksha.com/college/surya-group-of-institutions-chennai-villupuram-31066",
    "https://www.shiksha.com/college/kalol-institute-of-management-gujarat-other-37141",
    "https://www.shiksha.com/college/megha-institute-of-engineering-and-technology-for-women-telangana-other-62133",
    "https://www.shiksha.com/university/aaft-university-of-media-and-arts-raipur-63859",
    "https://www.shiksha.com/college/vatel-hotel-and-tourism-business-school-sushant-university-gurgaon-47994",
    "https://www.shiksha.com/university/birla-institute-of-technology-mesra-jaipur-extension-center-51590",
    "https://www.shiksha.com/college/doon-group-of-colleges-dehradun-52621",
    "https://www.shiksha.com/college/a-j-institute-of-engineering-and-technology-karnataka-other-59553",
    "https://www.shiksha.com/college/sri-shivani-institute-of-management-karimnagar-62331",
    "https://www.shiksha.com/university/kk-university-nalanda-63943",
    "https://www.shiksha.com/college/hec-group-of-institutions-haridwar-65127",
    "https://www.shiksha.com/college/career-college-of-management-bhopal-68607",
    "https://www.shiksha.com/college/vaishnavi-institute-of-management-bhopal-68625",
    "https://www.shiksha.com/college/nabira-mahavidyalaya-nagpur-73867",
    "https://www.shiksha.com/college/vjcet-viswajyothi-college-of-engineering-and-technology-ernakulum-13698",
    "https://www.shiksha.com/college/naemd-national-academy-of-event-management-and-development-jaipur-27223",
    "https://www.shiksha.com/college/institute-of-business-management-and-technology-banashankari-bangalore-28071",
    "https://www.shiksha.com/college/malout-institute-of-management-and-information-technology-muktsar-28939",
    "https://www.shiksha.com/college/christ-institute-of-management-cim-rajkot-37155",
    "https://www.shiksha.com/college/symbiosis-school-of-media-communication-symbiosis-international-bangalore-hosur-road-47836",
    "https://www.shiksha.com/college/sapthagiri-college-of-engineering-dharmapuri-tamil-nadu-other-48882",
    "https://www.shiksha.com/college/truba-college-of-science-and-technology-bhopal-58703",
    "https://www.shiksha.com/university/sant-baba-bhag-singh-university-jalandhar-64897",
    "https://www.shiksha.com/college/st-ann-s-degree-and-pg-college-for-women-mallapur-secunderabad-68413",
    "https://www.shiksha.com/university/kk-modi-university-bhilai-152859",
    "https://www.shiksha.com/college/thanthai-hans-roever-college-of-arts-and-science-tamil-nadu-other-4390",
    "https://www.shiksha.com/college/virudhunagar-hindu-nadars-senthikumara-nadar-college-21517",
    "https://www.shiksha.com/college/abul-quadir-jeelani-centre-for-post-graduate-studies-aqj-visakhapatnam-22389",
    "https://www.shiksha.com/college/riet-jaipur-rajasthan-institute-of-engineering-and-technology-23206",
    "https://www.shiksha.com/college/r-l-institute-of-management-studies-madurai-28424",
    "https://www.shiksha.com/college/nec-nandha-engineering-college-erode-38148",
    "https://www.shiksha.com/college/shadan-institute-of-management-studies-for-boys-khairatabad-hyderabad-62257",
    "https://www.shiksha.com/college/maulana-azad-educational-trust-s-millennium-institute-of-management-aurangabad-64657",
    "https://www.shiksha.com/college/international-institute-of-management-science-chinchwad-pune-64701",
    "https://www.shiksha.com/college/school-of-business-management-iftm-university-moradabad-20251",
    "https://www.shiksha.com/college/jyothishmathi-institute-of-technology-and-science-karimnagar-20401",
    "https://www.shiksha.com/college/vrs-and-yrn-college-andhra-pradesh-other-23102",
    "https://www.shiksha.com/college/scms-institute-of-masscom-studies-sims-kochi-28779",
    "https://www.shiksha.com/college/eswar-college-of-engineering-guntur-29073",
    "https://www.shiksha.com/college/mother-teresa-college-of-management-and-computer-applications-ranga-reddy-62131",
    "https://www.shiksha.com/college/bharti-vidya-mandir-college-of-management-education-gwalior-70995",
    "https://www.shiksha.com/college/quad-ai-school-of-technology-and-management-patna-240132",
    "https://www.shiksha.com/college/svpm-s-institute-of-management-malegaon-pune-21155",
    "https://www.shiksha.com/college/st-michael-college-of-engineering-and-technology-tamil-nadu-other-23013",
    "https://www.shiksha.com/college/isbm-gurgaon-indus-school-of-business-management-gurgaon-34399",
    "https://www.shiksha.com/college/jp-institute-of-engineering-and-technology-meerut-37306",
    "https://www.shiksha.com/university/sri-sai-university-himachal-pradesh-other-38095",
    "https://www.shiksha.com/college/apollo-institute-of-technology-kanpur-42866",
    "https://www.shiksha.com/college/global-institutes-amritsar-47457",
    "https://www.shiksha.com/college/impact-institute-of-management-studies-sahakara-nagar-bangalore-38220",
    "https://www.shiksha.com/college/ilam-jaipur-national-university-jaipur-56615",
    "https://www.shiksha.com/college/kingston-pg-college-ranga-reddy-62119",
    "https://www.shiksha.com/college/new-science-pg-college-warangal-62163",
    "https://www.shiksha.com/college/prabhath-institute-of-business-management-kurnool-62373",
    "https://www.shiksha.com/college/musaliar-institute-of-management-pathanamthitta-63403",
    "https://www.shiksha.com/college/global-institute-of-management-sangamner-ahmednagar-64227",
    "https://www.shiksha.com/college/jay-bhavani-institute-of-management-jalna-179845",
    "https://www.shiksha.com/college/icri-bangalore-institute-of-clinical-research-india-bangalore-indiranagar-3596",
    "https://www.shiksha.com/college/millennium-group-of-institution-bhopal-31006",
    "https://www.shiksha.com/college/pt-l-r-college-of-technology-technical-campus-plrct-faridabad-36899",
    "https://www.shiksha.com/college/department-of-pg-studies-visvesvaraya-technological-university-kalaburagi-karnataka-other-51746",
    "https://www.shiksha.com/college/maharana-institute-of-professional-studies-kanpur-53989",
    "https://www.shiksha.com/college/trinity-college-of-engineering-and-technology-karimnagar-61329",
    "https://www.shiksha.com/college/indian-institute-of-aviation-and-hospitality-management-kalyan-east-mumbai-153237",
    "https://www.shiksha.com/college/gyanveer-group-of-institution-sagar-72125",
    "https://www.shiksha.com/college/indian-school-of-public-policy-ispp-hauz-khas-delhi-150841",
    "https://www.shiksha.com/college/kmct-school-of-management-kozhikode-156385",
    "https://www.shiksha.com/college/dayanand-anglo-vedic-institute-of-engineering-and-technology-jalandhar-19805",
    "https://www.shiksha.com/college/st-ann-s-college-of-engineering-and-technology-prakasam-21319",
    "https://www.shiksha.com/college/pict-school-of-technology-and-management-balewadi-pune-22109",
    "https://www.shiksha.com/college/priyadarshini-institute-of-technology-and-management-pitm-guntur-42616",
    "https://www.shiksha.com/college/international-institute-of-industrial-safety-management-nagarbhavi-bangalore-47409",
    "https://www.shiksha.com/college/mangalvedhekar-institute-of-management-solapur-64303",
    "https://www.shiksha.com/college/ldc-institute-of-technical-studies-allahabad-23674",
    "https://www.shiksha.com/college/herbarium-institute-of-international-hotel-studies-vikas-puri-delhi-29955",
    "https://www.shiksha.com/college/dolphin-pg-institute-of-biomedical-and-natural-sciences-dehradun-33363",
    "https://www.shiksha.com/college/government-engineering-college-jhalawar-gecj-42719",
    "https://www.shiksha.com/college/j-k-k-munirajah-college-of-technology-jkkmct-erode-54266",
    "https://www.shiksha.com/college/swami-vivekanand-college-of-engineering-indore-60411",
    "https://www.shiksha.com/college/nuovos-ajeenkya-d-y-patil-university-charholi-budruk-pune-202643",
    "https://www.shiksha.com/college/shri-swami-samarth-institute-of-management-technology-maharashtra-other-213275",
    "https://www.shiksha.com/college/samrat-ashok-technological-institute-vidisha-19408",
    "https://www.shiksha.com/college/dr-k-n-modi-institute-of-engineering-and-technology-modinagar-19942",
    "https://www.shiksha.com/college/yres-s-bapurao-deshmukh-college-of-engineering-wardha-22458",
    "https://www.shiksha.com/college/bn-college-of-engineering-and-technology-lucknow-31657",
    "https://www.shiksha.com/college/sri-sai-institute-of-technology-and-science-ssits-kadapa-43187",
    "https://www.shiksha.com/university/p-k-university-madhya-pradesh-other-64745",
    "https://www.shiksha.com/college/cp-and-berar-arts-commerce-college-nagpur-126197",
    "https://www.shiksha.com/college/gujarat-institute-of-hotel-management-vadodara-26477",
    "https://www.shiksha.com/college/t-john-institute-of-management-and-science-bannerghatta-road-bangalore-28397",
    "https://www.shiksha.com/college/remo-international-college-of-aviation-guindy-guindy-chennai-47205",
    "https://www.shiksha.com/college/emeralds-advanced-institute-of-management-studies-tirupati-53055",
    "https://www.shiksha.com/college/lingaraj-appa-engineering-college-bidar-59437",
    "https://www.shiksha.com/college/nigama-engineering-college-karimnagar-62161",
    "https://www.shiksha.com/college/jagannath-institute-of-management-sciences-rohini-rohini-delhi-45543",
    "https://www.shiksha.com/college/footwear-design-and-development-institute-hyderabad-110929",
    "https://www.shiksha.com/college/apeejay-institute-of-mass-communication-dwarka-delhi-aimc-dwarka-3039",
    "https://www.shiksha.com/college/shriram-institute-of-management-and-technology-kashipur-30625",
    "https://www.shiksha.com/college/golden-valley-integrated-campus-chittoor-60636",
    "https://www.shiksha.com/college/college-of-engineering-thalassery-kannur-60678",
    "https://www.shiksha.com/college/sdm-p-g-centre-for-management-studies-and-research-mangalore-69527",
    "https://www.shiksha.com/college/parijat-college-indore-142837",
    "https://www.shiksha.com/college/pgp-college-of-arts-and-science-pgpcas-namakkal-22866",
    "https://www.shiksha.com/college/ramanujan-college-of-management-rcm-haryana-other-28005",
    "https://www.shiksha.com/university/jagan-nath-university-haryana-jhajjar-30525",
    "https://www.shiksha.com/college/wings-business-school-wbs-andhra-pradesh-tirupati-37684",
    "https://www.shiksha.com/college/kaps-krishnapatnam-academy-of-professional-studies-nellore-57669",
    "https://www.shiksha.com/college/seshadripuram-college-karnataka-other-69533",
    "https://www.shiksha.com/college/shri-rama-krishna-college-of-polytechnic-and-management-satna-100453",
    "https://www.shiksha.com/college/sau-leena-kishor-mamidwar-institute-of-management-studies-and-research-chandrapur-66465",
    "https://www.shiksha.com/college/maharaja-business-school-khurda-148053",
    "https://www.shiksha.com/university/kn-university-ahmedabad-228871",
    "https://www.shiksha.com/college/nimbus-academy-of-management-dehradun-4307",
    "https://www.shiksha.com/college/bharathiar-school-of-management-and-entrepreneur-development-bsmed-coimbatore-19611",
    "https://www.shiksha.com/college/infant-jesus-college-of-engineering-tirunelveli-48102",
    "https://www.shiksha.com/college/department-of-pg-studies-visvesvaraya-technological-university-bangalore-chikkaballapur-51579",
    "https://www.shiksha.com/college/shri-jaysukhlal-vadhar-institute-of-management-studies-jamnagar-54495",
    "https://www.shiksha.com/college/shree-venkateshwara-hi-tech-engineering-college-erode-61619",
    "https://www.shiksha.com/college/priyadarshini-p-g-college-mca-hyderabad-62193",
    "https://www.shiksha.com/college/vinuthna-college-of-management-warangal-62227",
    "https://www.shiksha.com/college/m-s-panwar-group-of-institutions-solan-64965",
    "https://www.shiksha.com/college/snb-college-of-pharmacy-and-management-patna-179975",
    "https://www.shiksha.com/college/ibmr-institute-of-business-management-research-prantik-pally-kolkata-4287",
    "https://www.shiksha.com/college/prince-institute-of-innovative-technology-greater-noida-30429",
    "https://www.shiksha.com/college/malineni-lakshmaiah-womens-engineering-college-guntur-60668",
    "https://www.shiksha.com/college/amu-murshidabad-centre-144581",
    "https://www.shiksha.com/university/jagadguru-rambhadracharya-handicapped-university-jrhu-uttar-pradesh-other-23138",
    "https://www.shiksha.com/college/dayal-group-of-institution-lucknow-38375",
    "https://www.shiksha.com/college/mahaveer-institute-of-technology-meerut-43213",
    "https://www.shiksha.com/college/new-prince-shri-bhavani-college-of-engineering-and-technology-velachery-chennai-46788",
    "https://www.shiksha.com/college/rabiammal-ahamed-maideen-college-for-women-thiruvarur-74743",
    "https://www.shiksha.com/college/skp-engineering-college-skpec-tamil-nadu-other-22962",
    "https://www.shiksha.com/college/b-m-group-of-institutions-bmgi-gurgaon-24138",
    "https://www.shiksha.com/college/narasaraopeta-engineering-college-autonomous-guntur-25422",
    "https://www.shiksha.com/college/tite-templecity-institute-of-technology-and-engineering-khurda-34315",
    "https://www.shiksha.com/college/yamuna-group-of-institutions-yamuna-nagar-40177",
    "https://www.shiksha.com/college/agra-public-group-of-institutions-59313",
    "https://www.shiksha.com/college/lnct-group-of-colleges-bhopal-156717",
    "https://www.shiksha.com/college/sngist-sree-narayana-guru-institute-of-science-and-technology-ernakulum-13705",
    "https://www.shiksha.com/college/priyadarshini-engineering-college-chennai-59445",
    "https://www.shiksha.com/college/mahatma-gandhi-college-guntur-66319",
    "https://www.shiksha.com/college/k-e-s-pratibha-institute-of-business-management-pune-72531",
    "https://www.shiksha.com/college/city-college-of-management-and-technology-lucknow-149037",
    "https://www.shiksha.com/college/svkp-dr-k-s-raju-arts-and-science-college-andhra-pradesh-other-23026",
    "https://www.shiksha.com/college/sona-college-of-technology-salem-36802",
    "https://www.shiksha.com/college/seth-sriniwas-agarwal-institute-of-management-ssaim-kanpur-38019",
    "https://www.shiksha.com/college/department-of-management-sumandeep-vidyapeeth-university-vadodara-52682",
    "https://www.shiksha.com/college/hmfa-memorial-institute-of-engineering-and-technology-allahabad-59903",
    "https://www.shiksha.com/college/maharaja-purna-chandra-autonomous-college-baripada-68947",
    "https://www.shiksha.com/college/r-e-s-s-college-of-computer-science-and-information-technology-latur-74679",
    "https://www.shiksha.com/college/sri-sai-bharath-college-of-arts-and-science-dindigul-76683",
    "https://www.shiksha.com/college/wesley-degree-college-hyderabad-77965",
    "https://www.shiksha.com/college/kmct-school-of-healthcare-administration-and-general-management-kozhikode-147083",
    "https://www.shiksha.com/university/agrawan-heritage-university-229331",
    "https://www.shiksha.com/college/indus-institute-of-technology-and-management-iitm-kanpur-43229",
    "https://www.shiksha.com/university/afu-al-falah-university-faridabad-55997",
    "https://www.shiksha.com/college/vignan-s-lara-institute-of-technology-science-andhra-pradesh-other-60949",
    "https://www.shiksha.com/college/velammal-college-of-engineering-and-technology-madurai-61785",
    "https://www.shiksha.com/college/krishna-chaitanya-educational-institutions-nellore-63619",
    "https://www.shiksha.com/university/bikaner-technical-university-64933",
    "https://www.shiksha.com/college/audyogik-shikshan-mandals-institute-of-professional-studies-pune-70793",
    "https://www.shiksha.com/college/dsrf-institute-of-computer-science-and-management-studies-dsrf-nagar-road-pune-19803",
    "https://www.shiksha.com/college/goutham-college-basaveshwaranagar-bangalore-22307",
    "https://www.shiksha.com/college/apex-institute-of-technology-chandigarh-university-mohali-63405",
    "https://www.shiksha.com/college/the-sankara-nethralaya-academy-st-thomas-mount-chennai-66455",
    "https://www.shiksha.com/college/acharya-rajendra-suri-shiksha-mahavidhyalaya-mandsaur-67165",
    "https://www.shiksha.com/college/dr-virendra-swarup-institute-of-professional-studies-vsips-kanpur-37359",
    "https://www.shiksha.com/college/mohandas-college-of-engineering-and-technology-thiruvananthapuram-37887",
    "https://www.shiksha.com/college/matoshri-ushatai-jadhav-institute-of-management-studies-and-research-centre-muimrc-thane-east-thane-38048",
    "https://www.shiksha.com/college/scope-college-of-engineering-bhopal-46889",
    "https://www.shiksha.com/university/sardar-patel-university-balaghat-66075",
    "https://www.shiksha.com/college/fighter-wings-aviation-academy-vadapalani-chennai-67361",
    "https://www.shiksha.com/college/ahmedabad-institute-of-business-studies-usmanpura-242660",
    "https://www.shiksha.com/college/the-school-of-business-logistics-mylapore-chennai-4284",
    "https://www.shiksha.com/college/rajarshi-rananjay-sinh-institute-of-management-and-technology-rrsimt-uttar-pradesh-other-37490",
    "https://www.shiksha.com/college/tagore-institute-of-engineering-and-technology-tiet-salem-42851",
    "https://www.shiksha.com/college/abss-institute-of-technology-meerut-43283",
    "https://www.shiksha.com/college/st-martin-s-institute-of-business-management-secunderabad-62151",
    "https://www.shiksha.com/college/venutai-chavan-college-satara-77663",
    "https://www.shiksha.com/college/sanjivani-institute-of-technology-and-management-bahraich-89261",
    "https://www.shiksha.com/college/jagruti-pg-college-of-management-studies-ranga-reddy-148531",
    "https://www.shiksha.com/college/k-j-institute-of-management-mehsana-196811",
    "https://www.shiksha.com/college/isbr-powered-by-emversity-electronic-city-bangalore-236022",
    "https://www.shiksha.com/college/kali-charan-nigam-institute-of-technology-uttar-pradesh-other-25001",
    "https://www.shiksha.com/college/corporate-institute-of-management-bhopal-59263",
    "https://www.shiksha.com/college/k-l-e-s-s-k-l-e-college-of-engineering-and-technology-chikodi-karnataka-other-59393",
    "https://www.shiksha.com/college/nagarjuna-degree-college-bangalore-69429",
    "https://www.shiksha.com/college/shri-girraj-maharaj-college-mathura-76029",
    "https://www.shiksha.com/college/jagan-s-institute-of-management-and-computer-studies-nellore-146221",
    "https://www.shiksha.com/college/khandesh-college-education-society-s-college-of-engineering-and-management-jalgaon-147861",
    "https://www.shiksha.com/college/gyanodaya-institute-of-professional-studies-dewas-157073",
    "https://www.shiksha.com/college/bangalore-management-institute-jalahalli-180475",
    "https://www.shiksha.com/college/institute-of-computer-science-and-technology-icst-varanasi-23409",
    "https://www.shiksha.com/college/aditya-m-b-a-college-maharashtra-other-38016",
    "https://www.shiksha.com/college/college-of-agriculture-jorhat-54274",
    "https://www.shiksha.com/college/jawaharlal-nehru-college-of-technology-rewa-60373",
    "https://www.shiksha.com/college/sai-krupa-institute-of-management-science-ahmednagar-64633",
    "https://www.shiksha.com/college/swami-sahajanand-college-of-commerce-and-management-bhavnagar-69215",
    "https://www.shiksha.com/college/smt-parmeshwaridevi-durgadutt-tibrewala-lions-juhu-college-of-arts-commerce-and-science-andheri-east-mumbai-74819",
    "https://www.shiksha.com/university/dr-abdul-haq-urdu-university-kurnool-62311",
    "https://www.shiksha.com/college/indian-school-of-science-and-management-hyderabad-kukatpally-63821",
    "https://www.shiksha.com/college/jaihind-institute-of-management-and-research-pune-228529",
    "https://www.shiksha.com/college/kanya-maha-vidyalaya-jalandhar-23257",
    "https://www.shiksha.com/college/s-d-college-of-management-studies-sdcms-muzaffarnagar-37382",
    "https://www.shiksha.com/college/kuppam-engineering-college-chittoor-37826",
    "https://www.shiksha.com/college/r-k-college-of-engineering-vijayawada-46605",
    "https://www.shiksha.com/college/ideal-institute-of-technology-govindpuram-ghaziabad-53364",
    "https://www.shiksha.com/college/the-bhopal-school-of-social-sciences-59811",
    "https://www.shiksha.com/college/capital-engineering-college-khurda-61391",
    "https://www.shiksha.com/college/dvm-college-of-business-management-nalgonda-62085",
    "https://www.shiksha.com/college/anekant-institute-of-management-studies-baramati-pune-64207",
    "https://www.shiksha.com/college/institute-of-management-sciences-jammu-67599",
    "https://www.shiksha.com/college/asan-memorial-college-of-arts-and-science-chennai-140711",
    "https://www.shiksha.com/college/mangalmay-institute-of-management-and-technology-seekho-greater-noida-212309",
    "https://www.shiksha.com/college/indore-mahavidyalaya-147323",
    "https://www.shiksha.com/college/prin-k-p-mangalvedhekar-institute-of-management-career-development-and-research-solapur-147889",
    "https://www.shiksha.com/college/cii-school-of-logistics-amity-university-kolkata-salt-lake-city-212597",
    "https://www.shiksha.com/college/v-m-patel-institute-of-management-gujarat-other-4342",
    "https://www.shiksha.com/college/national-academy-of-event-management-and-development-ahmedabad-navrangpura-27226",
    "https://www.shiksha.com/college/imperial-college-of-business-studies-bangalore-jayanagar-34508",
    "https://www.shiksha.com/college/al-ameen-education-medical-foundation-s-college-of-engineering-management-studies-taluka-shirur-pune-47225",
    "https://www.shiksha.com/college/college-of-commerce-arts-and-science-magadh-university-patna-51635",
    "https://www.shiksha.com/college/timespro-bennett-university-greater-noida-53197",
    "https://www.shiksha.com/college/institute-of-advanced-research-gandhinagar-60207",
    "https://www.shiksha.com/college/kbn-college-pg-center-krishna-62487",
    "https://www.shiksha.com/college/utkarsh-college-of-management-education-bareilly-65543",
    "https://www.shiksha.com/college/shri-rawatpura-sarkar-institutions-datia-88035",
    "https://www.shiksha.com/college/progressive-education-society-s-modern-institute-of-business-studies-mibs-pune-nigdi-150759",
    "https://www.shiksha.com/college/m-s-college-of-management-palghar-209023",
    "https://www.shiksha.com/college/vivekananda-school-of-post-graduate-studies-vspgs-hyderabad-yellareddiguda-21537",
    "https://www.shiksha.com/college/satya-group-of-institutions-faridabad-32878",
    "https://www.shiksha.com/college/sgsjk-s-aruna-manharlal-shah-institute-of-management-and-research-amsimr-mumbai-ghatkopar-west-34783",
    "https://www.shiksha.com/college/noble-institute-of-management-and-technology-nimt-lucknow-35055",
    "https://www.shiksha.com/college/selvam-educational-institutions-namakkal-42752",
    "https://www.shiksha.com/college/chaitanya-engineering-college-visakhapatnam-44922",
    "https://www.shiksha.com/college/bomma-institute-of-technology-and-science-khammam-52692",
    "https://www.shiksha.com/college/footwear-design-and-development-institute-rohtak-110931",
    "https://www.shiksha.com/college/ditm-delhi-institute-of-technology-and-management-sonepat-32777",
    "https://www.shiksha.com/university/dr-k-n-modi-university-rajasthan-other-33260",
    "https://www.shiksha.com/college/jain-college-of-engineering-and-technology-hubli-59177",
    "https://www.shiksha.com/college/pankaj-laddhad-institute-of-technology-and-management-studies-buldana-maharashtra-other-59485",
    "https://www.shiksha.com/college/rasiklal-m-dhariwal-sinhgad-technical-institutes-campus-maharashtra-other-59749",
    "https://www.shiksha.com/college/david-memorial-institute-of-management-hyderabad-71397",
    "https://www.shiksha.com/college/rourkela-institute-of-management-studies-74687",
    "https://www.shiksha.com/college/international-maritime-business-academy-dehradun-145693",
    "https://www.shiksha.com/college/oriental-institute-of-management-lalburra-balaghat-157031",
    "https://www.shiksha.com/college/karanjekar-college-of-engineering-and-management-sakoli-213381",
    "https://www.shiksha.com/college/mr-dav-institute-of-management-studies-rohtak-31495",
    "https://www.shiksha.com/college/vijaya-institute-of-technology-for-women-andhra-pradesh-other-43066",
    "https://www.shiksha.com/university/assam-rajiv-gandhi-university-of-co-operative-management-assam-other-64939",
    "https://www.shiksha.com/college/m-r-m-institute-of-management-ranga-reddy-73215",
    "https://www.shiksha.com/college/r-s-college-of-management-and-science-bangalore-115411",
    "https://www.shiksha.com/college/sns-b-spine-an-experiential-b-school-coimbatore-146141",
    "https://www.shiksha.com/college/dr-g-r-damodaran-institute-of-management-coimbatore-148249",
    "https://www.shiksha.com/college/aists-international-academy-of-sport-science-and-technology-lower-parel-mumbai-150319",
    "https://www.shiksha.com/college/shri-ravindranath-tagore-institute-of-professional-studies-khandwa-157023",
    "https://www.shiksha.com/college/international-institute-for-special-education-iise-lucknow-28490",
    "https://www.shiksha.com/college/ar-institute-of-management-and-technology-arimt-meerut-30481",
    "https://www.shiksha.com/college/institute-of-co-operative-management-dehradun-72305",
    "https://www.shiksha.com/college/karmaveer-bhausaheb-hiray-institute-of-management-and-research-nashik-72613",
    "https://www.shiksha.com/college/saraswati-group-of-institutions-rudrapur-75577",
    "https://www.shiksha.com/college/asian-institute-of-professional-studies-indore-147475",
    "https://www.shiksha.com/college/kedarnath-aggarwal-institute-of-management-kaim-haryana-other-4267",
    "https://www.shiksha.com/college/jagannath-community-college-rohini-delhi-26045",
    "https://www.shiksha.com/college/brm-institute-of-management-and-information-technology-bhubaneswar-28167",
    "https://www.shiksha.com/college/aishwarya-institute-of-management-and-information-technology-udaipur-28404",
    "https://www.shiksha.com/college/sgi-samalkha-group-of-institutions-panipat-32303",
    "https://www.shiksha.com/college/noble-school-of-business-nsb-j-p-nagar-bangalore-36984",
    "https://www.shiksha.com/college/wisdom-school-of-management-coimbatore-wsm-coimbatore-37040",
    "https://www.shiksha.com/college/indraprasth-institute-of-management-gurgaon-37383",
    "https://www.shiksha.com/college/international-school-of-design-kandivali-kandivali-west-mumbai-48452",
    "https://www.shiksha.com/college/amrita-school-of-arts-and-sciences-amrita-vishwa-vidyapeetham-mysuru-campus-mysore-48559",
    "https://www.shiksha.com/college/jcet-jaya-college-of-engineering-and-technology-poonamallee-chennai-53754",
    "https://www.shiksha.com/college/miracle-educational-society-group-of-institutions-vizianagaram-60688",
    "https://www.shiksha.com/college/james-college-of-engineering-and-technology-kanyakumari-42764",
    "https://www.shiksha.com/college/radharaman-engineering-college-bhopal-43060",
    "https://www.shiksha.com/college/sree-chaitanya-institute-of-technological-sciences-scits-karimnagar-43295",
    "https://www.shiksha.com/college/monti-international-institute-of-management-studies-kerala-other-51868",
    "https://www.shiksha.com/college/fit-group-of-institutions-meerut-52709",
    "https://www.shiksha.com/college/seth-vishambhar-nath-group-of-educational-institutions-barabanki-59709",
    "https://www.shiksha.com/university/kerala-university-of-fisheries-and-ocean-studies-kochi-60353",
    "https://www.shiksha.com/college/ideal-college-of-arts-and-sciences-kakinada-62363",
    "https://www.shiksha.com/college/karavali-institute-of-technology-mangalore-65241",
    "https://www.shiksha.com/college/mkm-group-of-colleges-for-girls-palwal-68931",
    "https://www.shiksha.com/college/r-h-patel-institute-of-management-gujarat-other-69165",
    "https://www.shiksha.com/college/icri-srinivas-university-mangalore-145695",
    "https://www.shiksha.com/college/rvs-institute-of-management-studies-coimbatore-148227",
    "https://www.shiksha.com/college/merit-swiss-asian-school-of-hotel-management-ooty-1040",
    "https://www.shiksha.com/college/centre-for-management-technology-c-mat-noida-19685",
    "https://www.shiksha.com/college/dr-rizvi-college-of-engineering-uttar-pradesh-other-24940",
    "https://www.shiksha.com/college/cms-bangalore-lalbagh-rd-36510",
    "https://www.shiksha.com/college/skr-engineering-college-poonamallee-chennai-39503",
    "https://www.shiksha.com/college/vivekanand-institute-of-technology-and-science-ghaziabad-42656",
    "https://www.shiksha.com/college/nirmala-college-of-engineering-thrissur-47524",
    "https://www.shiksha.com/college/naranlala-college-of-commerce-and-management-navsari-59067",
    "https://www.shiksha.com/college/lnct-excellence-college-bhopal-60714",
    "https://www.shiksha.com/college/indira-institute-of-engineering-and-technology-thiruvarur-61629",
    "https://www.shiksha.com/college/vignanasudha-institute-of-management-and-technology-chittoor-62511",
    "https://www.shiksha.com/college/dr-r-g-bhoyar-group-of-institutions-wardha-74053",
    "https://www.shiksha.com/college/sanjay-rungta-group-of-institutions-bhilai-212575",
    "https://www.shiksha.com/college/vidya-prasarak-mandal-s-institute-of-management-studies-vpm-s-ims-thane-242424",
    "https://www.shiksha.com/college/niilm-centre-for-management-studies-greater-noida-426",
    "https://www.shiksha.com/college/millia-institute-of-technology-bihar-other-23321",
    "https://www.shiksha.com/college/g-r-damodaran-academy-of-management-grdam-coimbatore-24812",
    "https://www.shiksha.com/college/nibms-borivali-east-mumbai-31939",
    "https://www.shiksha.com/college/innovation-the-business-school-ibs-orissa-orissa-other-37471",
    "https://www.shiksha.com/college/indian-institute-of-fashion-technology-iift-bareilly-40912",
    "https://www.shiksha.com/college/ushodaya-institute-of-management-and-technology-ibrahimpatnam-hyderabad-46932",
    "https://www.shiksha.com/college/r-l-jalappa-institute-of-technology-bangalore-karnataka-other-59707",
    "https://www.shiksha.com/college/kirsan-s-mission-institute-of-management-gondia-64331",
    "https://www.shiksha.com/college/nadar-saraswathi-college-of-arts-and-science-theni-68649",
    "https://www.shiksha.com/college/madhuban-institute-of-professional-studies-indore-68989",
    "https://www.shiksha.com/college/jhankar-college-gurgaon-208767",
    "https://www.shiksha.com/college/integral-university-seekho-lucknow-212305",
    "https://www.shiksha.com/college/mvm-college-of-arts-science-management-yelahanaka-bangalore-231136",
    "https://www.shiksha.com/college/sindhi-college-hebbal-bangalore-36278",
    "https://www.shiksha.com/college/yadavrao-tasgaonkar-institute-of-management-studies-and-research-raigad-37693",
    "https://www.shiksha.com/college/pace-institute-of-technology-and-sciences-prakasam-46562",
    "https://www.shiksha.com/college/patel-college-of-science-and-technology-bhopal-52561",
    "https://www.shiksha.com/college/shantiniketan-business-school-sbs-nagpur-30856",
    "https://www.shiksha.com/college/apex-group-of-institutions-jaipur-35725",
    "https://www.shiksha.com/college/school-of-management-studies-guru-nanak-institutions-technical-campus-ranga-reddy-43350",
    "https://www.shiksha.com/college/anurag-college-of-engineering-ranga-reddy-47276",
    "https://www.shiksha.com/university/guru-nanak-dev-university-regional-campus-gurdaspur-punjab-other-55311",
    "https://www.shiksha.com/college/pallavi-college-of-business-management-secunderabad-68407",
    "https://www.shiksha.com/college/shri-ram-institute-of-management-jabalpur-68615",
    "https://www.shiksha.com/college/thakur-shivkumarsingh-memorial-management-college-burhanpur-68621",
    "https://www.shiksha.com/college/iqbal-institute-of-technology-and-management-srinagar-68721",
    "https://www.shiksha.com/college/bishop-cotton-academy-of-professional-management-yelahanaka-bangalore-71019",
    "https://www.shiksha.com/college/ku-post-graduate-center-gadag-103917",
    "https://www.shiksha.com/college/leaders-college-kannur-210253",
    "https://www.shiksha.com/college/gl-bajaj-college-of-technology-and-management-greater-noida-213689",
    "https://www.shiksha.com/college/center-for-pg-studies-vtu-belgaum-21527",
    "https://www.shiksha.com/college/vysya-institute-of-management-studies-vimt-salem-21547",
    "https://www.shiksha.com/college/school-of-business-and-strategy-dnyaan-prasad-global-university-pune-243410",
    "https://www.shiksha.com/college/jamal-institute-of-management-tiruchirappalli-47696",
    "https://www.shiksha.com/college/sgit-school-of-management-sanskar-educational-group-ghaziabad-59179",
    "https://www.shiksha.com/college/bhopal-institute-of-technology-and-management-61705",
    "https://www.shiksha.com/college/aurobindo-college-of-computer-science-olive-p-g-college-ranga-reddy-62037",
    "https://www.shiksha.com/college/st-joseph-s-college-of-engineering-and-technology-thanjavur-66811",
    "https://www.shiksha.com/college/vogue-dr-kariappa-business-school-doddaballapur-rd-bangalore-151025",
    "https://www.shiksha.com/college/chanakya-institute-of-management-and-higher-studies-bihar-other-179973",
    "https://www.shiksha.com/college/gems-b-school-chennai-saidapet-31010",
    "https://www.shiksha.com/college/prin-n-g-naralkar-institute-of-career-development-and-research-sadashiv-peth-pune-36243",
    "https://www.shiksha.com/college/impact-college-of-engineering-and-applied-sciences-sahakara-nagar-bangalore-38911",
    "https://www.shiksha.com/college/st-mary-s-technical-campus-barasat-kolkata-42646",
    "https://www.shiksha.com/college/naemd-national-academy-of-event-management-and-development-noida-46796",
    "https://www.shiksha.com/university/mandsaur-university-madhya-pradesh-other-48876",
    "https://www.shiksha.com/college/government-engineering-college-thrissur-52578",
    "https://www.shiksha.com/college/chiranjeevi-reddy-institute-of-engineering-and-technology-anantapur-46499",
    "https://www.shiksha.com/college/bonam-venkata-chalamayya-institute-of-technology-and-science-east-godavari-52691",
    "https://www.shiksha.com/college/department-of-management-studies-iiit-allahabad-52940",
    "https://www.shiksha.com/college/aimed-aachi-institute-of-management-and-entrepreneurial-development-anna-nagar-chennai-55849",
    "https://www.shiksha.com/college/indur-p-g-college-of-business-management-nizamabad-62205",
    "https://www.shiksha.com/college/nadar-mahajana-sangam-s-vellaichamy-nadar-college-madurai-66361",
    "https://www.shiksha.com/college/ranibai-agnihotri-institute-of-computer-science-and-information-technology-wardha-68683",
    "https://www.shiksha.com/college/akal-group-of-technical-and-management-institution-mastuana-sangrur-68711",
    "https://www.shiksha.com/college/lala-lajpat-rai-memorial-institute-of-management-and-technology-moga-148111",
    "https://www.shiksha.com/college/shikshaa-institute-of-advanced-technologies-tamil-nadu-other-225027",
    "https://www.shiksha.com/college/mother-teresa-women-s-university-research-and-extension-centre-chennai-saidapet-228387",
    "https://www.shiksha.com/college/padmashree-institute-of-management-and-sciences-kengeri-bangalore-25409",
    "https://www.shiksha.com/college/maharishi-arvind-institute-of-science-and-management-jaipur-28456",
    "https://www.shiksha.com/college/aryan-institute-of-technology-ghaziabad-28806",
    "https://www.shiksha.com/college/ggs-college-of-modern-technology-ggs-mohali-43031",
    "https://www.shiksha.com/college/shri-aurbindo-institute-of-management-indore-68663",
    "https://www.shiksha.com/college/ooa-mavmm-school-of-management-madurai-74209",
    "https://www.shiksha.com/college/oriental-school-of-business-thane-147943",
    "https://www.shiksha.com/college/e-g-s-pillay-arts-and-science-college-nagapattinam-148419",
    "https://www.shiksha.com/college/avanthi-s-school-of-business-management-moosarambagh-hyderabad-155713",
    "https://www.shiksha.com/college/satya-college-of-engineering-and-technology-palwal-195527",
    "https://www.shiksha.com/college/directorate-of-distance-and-continuing-education-utkal-university-khordha-195725",
    "https://www.shiksha.com/college/m-r-college-of-management-and-allied-health-sciences-west-bengal-other-211621",
    "https://www.shiksha.com/college/nizam-institute-of-engineering-and-technology-niet-hyederabad-nalgonda-22840",
    "https://www.shiksha.com/college/institute-for-excellence-in-higher-education-bhopal-23146",
    "https://www.shiksha.com/college/skiet-shri-krishan-institute-of-engineering-and-technology-kurukshetra-24906",
    "https://www.shiksha.com/college/pragnya-group-of-institutes-pune-28560",
    "https://www.shiksha.com/college/bharat-group-of-institutions-sonepat-32347",
    "https://www.shiksha.com/college/aakash-institute-of-business-management-mallathalli-bangalore-33098",
    "https://www.shiksha.com/college/international-institute-of-fashion-technology-north-delhi-model-town-34817",
    "https://www.shiksha.com/college/utkal-institute-of-technology-and-management-khordha-209001",
    "https://www.shiksha.com/college/newton-s-institute-of-engineering-nie-guntur-20778",
    "https://www.shiksha.com/college/aizza-college-of-engineering-and-technology-telangana-other-23293",
    "https://www.shiksha.com/college/noble-institute-of-science-and-technology-visakhapatnam-23795",
    "https://www.shiksha.com/college/puran-murti-campus-sonepat-32346",
    "https://www.shiksha.com/college/hasvita-institute-of-engineering-and-technology-ameerpet-hyderabad-43241",
    "https://www.shiksha.com/college/gmr-aviation-academy-hyderabad-shamshabad-47059",
    "https://www.shiksha.com/college/nct-nandha-college-of-technology-erode-48508",
    "https://www.shiksha.com/college/centre-for-management-studies-orissa-engineering-college-bhubaneswar-54394",
    "https://www.shiksha.com/college/mahaveer-college-of-commerce-jaipur-59267",
    "https://www.shiksha.com/college/harinadha-reddy-institute-of-management-sciences-chittoor-62481",
    "https://www.shiksha.com/college/sri-vani-institute-of-management-and-sciences-anantapur-62529",
    "https://www.shiksha.com/college/suraj-institute-of-management-beed-maharashtra-other-64655",
    "https://www.shiksha.com/college/prabhat-engineering-college-kanpur-65509",
    "https://www.shiksha.com/college/neelam-college-of-engineering-and-technology-agra-66375",
    "https://www.shiksha.com/college/swami-sarvanand-group-of-institutes-gurdaspur-56919",
    "https://www.shiksha.com/college/sanjay-bhokare-group-of-institutes-maharashtra-other-59083",
    "https://www.shiksha.com/college/adarsh-post-graduate-college-of-computer-science-mahabubnagar-telangana-other-62017",
    "https://www.shiksha.com/college/vijaya-p-g-college-ranga-reddy-62287",
    "https://www.shiksha.com/college/pentium-point-technical-college-rewa-74345",
    "https://www.shiksha.com/college/sengamala-thayaar-educational-trust-women-s-college-thiruvarur-75701",
    "https://www.shiksha.com/college/the-mandvi-education-society-institute-of-business-management-and-computer-studies-surat-101713",
    "https://www.shiksha.com/college/vet-institute-of-arts-and-science-college-erode-228365",
    "https://www.shiksha.com/college/northern-institute-of-management-and-technology-dr-mukherjee-nagar-delhi-27039",
    "https://www.shiksha.com/college/camp-education-society-s-institute-of-management-nigdi-pune-37042",
    "https://www.shiksha.com/college/periyar-management-and-computer-college-jasola-vihar-delhi-41787",
    "https://www.shiksha.com/college/jayalakshmi-institute-of-technology-jit-dharmapuri-tamil-nadu-other-42748",
    "https://www.shiksha.com/college/suraj-group-of-institutions-haryana-other-45551",
    "https://www.shiksha.com/college/adarsh-college-of-engineering-kakinada-46723",
    "https://www.shiksha.com/college/sacred-heart-institute-of-management-and-technology-sitapur-59769",
    "https://www.shiksha.com/college/vijaya-krishna-institute-of-technology-and-sciences-shamshabad-hyderabad-43225",
    "https://www.shiksha.com/college/maharajah-s-post-graduate-college-mrpg-vizianagaram-49369",
    "https://www.shiksha.com/college/vijaya-engineering-college-khammam-58977",
    "https://www.shiksha.com/college/vaagdevi-institute-of-management-sciences-warangal-62195",
    "https://www.shiksha.com/college/sri-harsha-institute-of-pg-studies-nellore-62415",
    "https://www.shiksha.com/college/sri-padmavathi-college-of-computer-sciences-and-technology-chittoor-62537",
    "https://www.shiksha.com/college/lsa-college-dhar-73063",
    "https://www.shiksha.com/college/l-t-r-institute-of-management-meerut-149041",
    "https://www.shiksha.com/university/central-tribal-university-of-andhra-pradesh-vizianagaram-203161",
    "https://www.shiksha.com/college/shiva-institute-of-management-studies-sims-ghaziabad-9057",
    "https://www.shiksha.com/college/t-j-institute-of-technology-old-mahabalipuram-road-chennai-19429",
    "https://www.shiksha.com/college/ashoka-institute-of-engineering-and-technology-ramoji-film-city-hyderabad-36435",
    "https://www.shiksha.com/college/aot-academy-of-technology-west-bengal-other-41537",
    "https://www.shiksha.com/college/rcvs-college-of-engineering-rvscet-tamil-nadu-other-42696",
    "https://www.shiksha.com/college/cce-christ-college-of-engineering-thrissur-55797",
    "https://www.shiksha.com/college/arulmigu-meenakshi-amman-college-of-engineering-kanchipuram-19535",
    "https://www.shiksha.com/university/the-icfai-university-raipur-38055",
    "https://www.shiksha.com/university/indus-international-university-iiu-una-38107",
    "https://www.shiksha.com/college/dev-bhoomi-group-of-institutions-dbgi-saharanpur-47803",
    "https://www.shiksha.com/college/indian-maritime-management-and-research-institute-immri-business-school-immri-george-town-chennai-48962",
    "https://www.shiksha.com/college/aurora-s-scientific-technological-and-research-academy-chandrayanagutta-hyderabad-57849",
    "https://www.shiksha.com/college/rvs-group-of-institution-dindigul-campus-151891",
    "https://www.shiksha.com/college/ahmedabad-institute-of-hospitality-management-154197",
    "https://www.shiksha.com/college/jai-shriram-engineering-college-tirupur-193829",
    "https://www.shiksha.com/university/shri-shankaracharya-professional-university-bhilai-202471",
    "https://www.shiksha.com/college/a-n-g-ideal-group-of-institutions-varanasi-226983",
    "https://www.shiksha.com/college/arya-college-jaipur-236418",
    "https://www.shiksha.com/college/primus-b-school-bangalore-243502",
    "https://www.shiksha.com/college/sidvin-school-of-business-banashankari-bangalore-13709",
    "https://www.shiksha.com/college/malineni-group-of-colleges-prakasam-20604",
    "https://www.shiksha.com/college/st-mary-s-college-of-engineering-technology-medak-61311",
    "https://www.shiksha.com/college/edge-international-b-school-chittoor-62357",
    "https://www.shiksha.com/college/dr-manorama-and-prof-haribhau-shankarrao-pundkar-arts-commerce-and-science-college-akola-66585",
    "https://www.shiksha.com/college/chathamkulam-institute-of-research-and-advanced-studies-palakkad-147041",
    "https://www.shiksha.com/college/delhi-global-institute-of-management-faridabad-195223",
    "https://www.shiksha.com/college/sri-ramachandra-faculty-of-management-science-porur-chennai-215579",
    "https://www.shiksha.com/college/guru-nanak-khalsa-group-of-educational-institutions-yamuna-nagar-22621",
    "https://www.shiksha.com/college/kovai-kalaimagal-college-of-arts-and-science-coimbatore-23766",
    "https://www.shiksha.com/college/jre-group-of-institutions-jre-greater-noida-31123",
    "https://www.shiksha.com/college/sriram-group-of-institutions-greater-noida-32810",
    "https://www.shiksha.com/college/global-institute-of-information-technology-greater-noida-37353",
    "https://www.shiksha.com/college/maris-stella-college-vijayawada-57457",
    "https://www.shiksha.com/college/all-saints-college-of-engineering-bhopal-61935",
    "https://www.shiksha.com/college/icri-sushant-university-gurgaon-63693",
    "https://www.shiksha.com/college/jairams-arts-and-science-college-karur-68707",
    "https://www.shiksha.com/college/school-of-health-sciences-sushant-university-gurgaon-48751",
    "https://www.shiksha.com/college/biyani-girls-college-jaipur-52180",
    "https://www.shiksha.com/college/dattakala-group-of-institution-maharashtra-other-60063",
    "https://www.shiksha.com/college/sree-narayana-institute-of-technology-adoor-pathanamthitta-60632",
    "https://www.shiksha.com/college/vignana-bharathi-engineering-college-ibrahimpatnam-hyderabad-68417",
    "https://www.shiksha.com/college/dnyan-kala-krida-and-krushi-pratishthan-maharashtra-institute-of-management-pune-71483",
    "https://www.shiksha.com/college/shahjahan-college-of-business-management-hyderabad-75805",
    "https://www.shiksha.com/college/fisheries-business-school-vaniyanchavadi-tamil-nadu-fisheries-university-chennai-106345",
    "https://www.shiksha.com/college/gate-institute-of-technology-and-sciences-nalgonda-148539",
    "https://www.shiksha.com/college/international-school-of-design-ahmedabad-ellis-bridge-224759",
    "https://www.shiksha.com/university/surajmal-university-kichha-235946",
    "https://www.shiksha.com/college/llriet-lala-lajpat-rai-institute-of-engineering-technology-moga-20504",
    "https://www.shiksha.com/college/kalka-institute-for-research-and-advanced-studies-meerut-21774",
    "https://www.shiksha.com/college/r-k-institute-of-management-and-computer-science-sarjapur-road-bangalore-28425",
    "https://www.shiksha.com/college/dr-i-t-group-of-institutions-rajpura-28451",
    "https://www.shiksha.com/college/aurobindo-college-of-business-management-ranga-reddy-70799",
    "https://www.shiksha.com/college/bm-professional-institute-indore-147459",
    "https://www.shiksha.com/college/ganesh-institute-of-management-studies-khurda-148045",
    "https://www.shiksha.com/college/smt-k-g-mittal-institute-of-management-mumbai-190363",
    "https://www.shiksha.com/college/g-h-raisoni-skill-tech-university-nagpur-227591",
    "https://www.shiksha.com/college/asan-institute-of-management-velachery-chennai-13658",
    "https://www.shiksha.com/college/bldea-s-v-p-dr-p-g-halakatti-college-of-engineering-and-technology-bijapur-24959",
    "https://www.shiksha.com/college/ritee-business-school-ribs-chhattisgarh-raipur-30854",
    "https://www.shiksha.com/college/rrs-college-of-engineering-and-technology-patancheru-hyderabad-42618",
    "https://www.shiksha.com/college/lord-jegannath-college-of-engineering-and-technology-ljcet-kanyakumari-43299",
    "https://www.shiksha.com/college/satya-institute-of-technology-and-management-vizianagaram-46609",
    "https://www.shiksha.com/college/gurukul-vidyapeeth-institute-of-engineering-and-technology-patiala-46853",
    "https://www.shiksha.com/college/eminent-college-of-management-and-technology-ecmt-barasat-kolkata-48864",
    "https://www.shiksha.com/college/apex-institute-of-technology-rampur-59347",
    "https://www.shiksha.com/college/vikas-group-of-institutions-vijayawada-60927",
    "https://www.shiksha.com/college/gyan-sagar-college-of-engineering-61221",
    "https://www.shiksha.com/college/cms-academy-of-management-and-technology-coimbatore-68641",
    "https://www.shiksha.com/college/mba-esg-ahmedabad-146041",
    "https://www.shiksha.com/college/panache-academy-goa-panjim-182163",
    "https://www.shiksha.com/college/kewalshree-institute-of-management-indore-210173",
    "https://www.shiksha.com/college/ambedkar-institute-of-higher-education-patna-231338",
    "https://www.shiksha.com/college/scient-institute-of-technology-sit-ibrahimpatnam-21114",
    "https://www.shiksha.com/college/swarnandhra-college-of-engineering-and-technology-west-godavari-21352",
    "https://www.shiksha.com/college/sree-visvesvaraya-institute-of-technology-and-science-svits-mahabubnagar-telangana-other-23485",
    "https://www.shiksha.com/college/dhanalakshmi-srinivasan-college-of-engineering-tamil-nadu-other-42706",
    "https://www.shiksha.com/college/annamacharya-institute-of-technology-and-sciences-rajampet-kadapa-46594",
    "https://www.shiksha.com/college/trigya-school-of-finance-and-management-tsfm-new-delhi-barakhamba-road-47835",
    "https://www.shiksha.com/college/bhagwati-institute-of-technology-and-science-ghaziabad-59519",
    "https://www.shiksha.com/college/lakshmi-narain-college-of-technology-jabalpur-60355",
    "https://www.shiksha.com/university/atal-bihari-vajpayee-hindi-vishwavidyalaya-bhopal-61245",
    "https://www.shiksha.com/college/institute-of-technology-and-management-lucknow-47435",
    "https://www.shiksha.com/college/mathuradevi-group-of-institutes-indore-48136",
    "https://www.shiksha.com/college/mysuru-royal-institute-of-technology-mysore-59743",
    "https://www.shiksha.com/college/sree-chaitanya-p-g-college-karimnagar-62077",
    "https://www.shiksha.com/college/rklk-pg-college-telangana-other-62217",
    "https://www.shiksha.com/college/snmv-college-of-arts-and-science-coimbatore-63561",
    "https://www.shiksha.com/college/gautam-institute-of-management-and-technology-hamirpur-68725",
    "https://www.shiksha.com/college/mahalaxmi-group-of-institutions-meerut-68999",
    "https://www.shiksha.com/college/malwa-college-bathinda-73333",
    "https://www.shiksha.com/college/kcmt-campus-2-bareilly-148965",
    "https://www.shiksha.com/college/university-college-of-arts-commerce-and-law-guntur-202093",
    "https://www.shiksha.com/college/hindustan-institute-for-international-trade-and-management-studies-ameerpet-hyderabad-203657",
    "https://www.shiksha.com/college/malla-reddy-university-powered-by-univirt-kompalli-hyderabad-212395",
    "https://www.shiksha.com/college/gomti-nandan-institute-of-management-and-research-sagar-230154",
    "https://www.shiksha.com/college/hi-tech-institute-of-engineering-technology-powered-by-sunstone-ghaziabad-239300",
    "https://www.shiksha.com/college/gyanoday-institute-of-management-and-technology-madhya-pradesh-other-72121",
    "https://www.shiksha.com/college/mumbai-educational-trusts-institute-management-studies-73789",
    "https://www.shiksha.com/college/sun-institute-of-management-and-technology-shahjahanpur-77033",
    "https://www.shiksha.com/college/meenakshi-ramasamy-arts-and-science-college-trichy-111259",
    "https://www.shiksha.com/college/imperial-institute-of-advanced-management-bangalore-146961",
    "https://www.shiksha.com/college/g-n-i-t-college-of-management-greater-noida-200003",
    "https://www.shiksha.com/college/dsifd-mumbai-chembur-206115",
    "https://www.shiksha.com/college/s-d-college-of-engineering-and-technology-muzaffarnagar-21028",
    "https://www.shiksha.com/college/chm-institute-of-hotel-and-business-management-ghaziabad-24874",
    "https://www.shiksha.com/college/engineering-college-ajmer-25156",
    "https://www.shiksha.com/college/vignan-s-foundation-for-science-technology-and-research-hyderabad-25505",
    "https://www.shiksha.com/college/the-hindu-college-mba-andhra-pradesh-other-37299",
    "https://www.shiksha.com/university/techno-global-university-shillong-42913",
    "https://www.shiksha.com/college/global-institute-of-technology-noida-47194",
    "https://www.shiksha.com/college/iimt-group-of-colleges-agra-55879",
    "https://www.shiksha.com/college/guru-gram-business-school-gurgaon-27935",
    "https://www.shiksha.com/college/indian-institute-of-tourism-and-travel-management-nellore-38053",
    "https://www.shiksha.com/college/jayam-college-of-engineering-and-technology-tamil-nadu-other-42784",
    "https://www.shiksha.com/college/neelkanth-group-of-institutions-meerut-47632",
    "https://www.shiksha.com/university/adesh-university-bathinda-54658",
    "https://www.shiksha.com/college/icri-himgiri-zee-university-dehradun-57321",
    "https://www.shiksha.com/college/maheshwari-girls-p-g-college-jaipur-57549",
    "https://www.shiksha.com/college/dr-sri-sri-sri-shivakumara-mahaswamy-college-of-engineering-bangalore-61209",
    "https://www.shiksha.com/college/st-mary-s-engineering-college-ranga-reddy-61307",
    "https://www.shiksha.com/college/unity-p-g-college-nalgonda-62339",
    "https://www.shiksha.com/college/vignan-degree-and-pg-college-guntur-62385",
    "https://www.shiksha.com/college/g-d-memorial-group-of-colleges-jodhpur-62589",
    "https://www.shiksha.com/college/rajendra-prasad-college-of-management-azamgarh-65537",
    "https://www.shiksha.com/college/viswam-degree-and-pg-college-chittoor-68919",
    "https://www.shiksha.com/college/annapoorna-institute-of-management-research-belgaum-70683",
    "https://www.shiksha.com/college/sardar-bhagat-singh-college-of-technology-and-management-sbsctm-lucknow-37624",
    "https://www.shiksha.com/college/sasurie-academy-of-engineering-coimbatore-42686",
    "https://www.shiksha.com/college/karnal-institute-of-technology-and-management-kurukshetra-42775",
    "https://www.shiksha.com/college/shree-ram-mulkh-institute-of-engineering-and-technology-ambala-43305",
    "https://www.shiksha.com/college/skywings-academy-of-aviation-and-tourism-kochi-48795",
    "https://www.shiksha.com/college/guru-nanak-institute-of-management-and-technology-ludhiana-52742",
    "https://www.shiksha.com/college/hoshiarpur-institute-of-management-and-technology-56913",
    "https://www.shiksha.com/college/ufly-international-new-dehli-connaught-place-delhi-57455",
    "https://www.shiksha.com/college/kmm-institute-of-technology-and-science-tirupati-60568",
    "https://www.shiksha.com/college/nanakram-bhagwan-das-science-college-hyderabad-62159",
    "https://www.shiksha.com/college/foster-development-school-of-management-aurangabad-64225",
    "https://www.shiksha.com/college/hi-tech-institute-of-technology-khurda-65217",
    "https://www.shiksha.com/college/v-r-institute-of-post-graduate-studies-nellore-68697",
    "https://www.shiksha.com/college/n-j-sonecha-management-and-technical-institute-gujarat-other-69135",
    "https://www.shiksha.com/college/johns-business-school-hyderabad-148563",
    "https://www.shiksha.com/college/swami-vivekanand-institute-of-management-shahdol-210179",
    "https://www.shiksha.com/college/akash-institute-of-engineering-and-technology-hubli-213411",
    "https://www.shiksha.com/college/sreenivasa-institute-of-technology-and-management-studies-chittoor-21250",
    "https://www.shiksha.com/college/ronald-ross-p-g-college-of-management-studies-ranga-reddy-25155",
    "https://www.shiksha.com/college/regional-group-of-institutions-gurgaon-29715",
    "https://www.shiksha.com/college/oasys-institute-of-technology-tiruchirappalli-43344",
    "https://www.shiksha.com/college/general-shivdev-singh-diwan-gurbachan-singh-khalsa-college-patiala-65167",
    "https://www.shiksha.com/college/ssld-varshney-institute-of-management-engineering-aligarh-65679",
    "https://www.shiksha.com/college/morigaon-college-69057",
    "https://www.shiksha.com/college/nrupatunga-degree-college-kachiguda-hyderabad-71091",
    "https://www.shiksha.com/university/centurion-university-of-technology-and-management-andhra-pradesh-visakhapatnam-91605",
    "https://www.shiksha.com/college/shri-gajanan-shiksha-samiti-college-hoshangabad-147183",
    "https://www.shiksha.com/college/shree-institute-of-progressive-studies-indore-147187",
    "https://www.shiksha.com/college/swaminarayan-siddhanta-institute-of-technology-nagpur-147553",
    "https://www.shiksha.com/college/bhubaneswar-institute-of-management-khordha-156339",
    "https://www.shiksha.com/college/mayurbhanj-college-of-accountancy-and-management-baripada-73569",
    "https://www.shiksha.com/college/smit-post-graduate-centre-for-management-studies-brahmapur-76377",
    "https://www.shiksha.com/college/adarsha-school-of-engineering-and-international-polytechnic-angul-147995",
    "https://www.shiksha.com/college/swami-vivekananda-institute-of-management-khurda-148049",
    "https://www.shiksha.com/college/r-v-s-college-of-engineering-dindigul-148315",
    "https://www.shiksha.com/college/priyadarshini-college-of-engineering-and-technology-nellore-22879",
    "https://www.shiksha.com/college/galaxy-global-group-of-institutions-ambala-34735",
    "https://www.shiksha.com/college/anand-institute-of-higher-technology-old-mahabalipuram-road-chennai-38141",
    "https://www.shiksha.com/college/avalon-business-school-visakhapatnam-42371",
    "https://www.shiksha.com/college/lucky-institute-of-professional-studies-jodhpur-58719",
    "https://www.shiksha.com/college/vilasrao-deshmukh-college-of-engineering-and-technology-nagpur-59823",
    "https://www.shiksha.com/college/malla-reddy-college-of-engineering-secunderabad-62145",
    "https://www.shiksha.com/college/nips-hotel-management-bhubaneswar-63263",
    "https://www.shiksha.com/college/madhu-vachaspati-school-of-management-uttar-pradesh-other-65541",
    "https://www.shiksha.com/college/vms-college-of-management-batala-66245",
    "https://www.shiksha.com/college/gurgaon-college-of-engineering-38235",
    "https://www.shiksha.com/college/dakshin-institute-of-management-sciences-dims-perungudi-chennai-41656",
    "https://www.shiksha.com/college/northern-institute-of-engineering-technical-campus-niet-alwar-42304",
    "https://www.shiksha.com/college/tmi-academy-of-travel-tourism-and-aviation-studies-mumbai-andheri-west-49291",
    "https://www.shiksha.com/college/dbsom-don-bosco-school-of-management-jayanagar-bangalore-56737",
    "https://www.shiksha.com/university/cmj-university-meghalaya-other-58121",
    "https://www.shiksha.com/college/lingayas-institute-of-management-and-technology-vijayawada-60628",
    "https://www.shiksha.com/college/gandhi-institute-of-excellent-technocrats-bhubaneswar-61403",
    "https://www.shiksha.com/college/dhanvanthari-institute-of-management-sciences-khammam-62083",
    "https://www.shiksha.com/college/kommuri-pratap-reddy-institute-of-management-telangana-other-62123",
    "https://www.shiksha.com/college/sri-balaji-pg-college-anantapur-62253",
    "https://www.shiksha.com/college/kishori-college-of-mba-maharashtra-other-64661",
    "https://www.shiksha.com/college/ajk-institute-of-management-coimbatore-68673",
    "https://www.shiksha.com/college/chandra-mauli-institute-of-management-sciences-and-technology-gorakhpur-71163",
    "https://www.shiksha.com/college/khadir-mohideen-college-thanjavur-72651",
    "https://www.shiksha.com/college/gyanmanjari-institute-of-technology-bhavnagar-58911",
    "https://www.shiksha.com/college/musaliar-college-of-engineering-technology-pathanamthitta-60487",
    "https://www.shiksha.com/college/institute-of-management-and-science-sakegaon-jalgaon-64319",
    "https://www.shiksha.com/college/pune-vidyarthi-griha-s-institute-of-management-nashik-64629",
    "https://www.shiksha.com/college/mitthulalji-sarda-mba-college-maharashtra-other-64659",
    "https://www.shiksha.com/college/mla-academy-of-higher-learning-bangalore-69413",
    "https://www.shiksha.com/college/institute-of-science-pune-72333",
    "https://www.shiksha.com/college/mata-sita-sunder-college-of-education-sitamarhi-117927",
    "https://www.shiksha.com/college/mohamed-sathak-college-of-arts-and-science-chennai-134287",
    "https://www.shiksha.com/college/indian-institute-of-materials-management-mumbai-147635",
    "https://www.shiksha.com/college/ch-college-mhow-indore-157131",
    "https://www.shiksha.com/college/kalinga-institute-of-management-and-technology-khordha-195743",
    "https://www.shiksha.com/college/aditya-degree-college-asilmetta-visakhapatnam-210001",
    "https://www.shiksha.com/college/little-angel-institute-of-professional-studies-indore-210189",
    "https://www.shiksha.com/college/samrat-college-berhampur-214887",
    "https://www.shiksha.com/college/seva-sadan-mahavidyalaya-burhanpur-75745",
    "https://www.shiksha.com/college/school-of-business-management-and-technology-bulandshahr-131769",
    "https://www.shiksha.com/college/shri-ram-college-bhopal-147179",
    "https://www.shiksha.com/college/madurai-institute-of-social-science-college-193767",
    "https://www.shiksha.com/college/pibm-global-mulshi-pune-213625",
    "https://www.shiksha.com/college/aditya-college-of-engineering-and-technology-bangalore-213705",
    "https://www.shiksha.com/college/sree-amman-arts-science-college-tamil-nadu-erode-21240",
    "https://www.shiksha.com/college/sri-venkatesa-perumal-college-of-engineering-and-technology-svpcet-chittoor-21299",
    "https://www.shiksha.com/college/chirala-engineering-college-andhra-pradesh-other-22501",
    "https://www.shiksha.com/college/isba-institute-of-professional-studies-indore-31603",
    "https://www.shiksha.com/college/sdvs-sangh-s-annapoorna-institute-of-management-research-aimr-belgaum-47977",
    "https://www.shiksha.com/college/spears-school-of-strategy-and-management-s3m-global-mylapore-chennai-48048",
    "https://www.shiksha.com/university/pdm-university-bahadurgarh-49282",
    "https://www.shiksha.com/university/birla-institute-of-technology-mesra-allahabad-extension-center-51604",
    "https://www.shiksha.com/college/millennium-institute-of-management-aurangabad-54502",
    "https://www.shiksha.com/college/radha-govind-group-of-institutions-meerut-25003",
    "https://www.shiksha.com/college/vsm-college-andhra-pradesh-other-25493",
    "https://www.shiksha.com/college/imperial-institute-of-hotel-management-chandigarh-35091",
    "https://www.shiksha.com/college/carlton-business-school-somajiguda-hyderabad-35366",
    "https://www.shiksha.com/college/uei-global-dehradun-36363",
    "https://www.shiksha.com/college/prathyusha-engineering-college-tiruvallur-chennai-52854",
    "https://www.shiksha.com/college/amardeep-singh-shergill-memorial-college-gndu-shahid-bhagat-singh-nagar-55021",
    "https://www.shiksha.com/college/malwa-institute-of-science-technology-indore-61243",
    "https://www.shiksha.com/college/vani-niketan-institute-of-management-studies-karimnagar-62297",
    "https://www.shiksha.com/college/holy-cross-college-of-management-and-technology-idukki-66721",
    "https://www.shiksha.com/college/aryabhatta-group-of-institutes-barnala-68007",
    "https://www.shiksha.com/college/lingaraj-college-belgaum-72673",
    "https://www.shiksha.com/college/modern-institute-of-professional-studies-indore-73713",
    "https://www.shiksha.com/college/gurukul-academy-indore-147355",
    "https://www.shiksha.com/college/gandhi-global-business-studies-ganjam-148051",
    "https://www.shiksha.com/college/geethanjali-institute-of-pg-studies-nellore-62479",
    "https://www.shiksha.com/college/sanjeev-institute-of-planning-and-management-east-godavari-62539",
    "https://www.shiksha.com/college/renaissance-institute-of-management-studies-chandrapur-64205",
    "https://www.shiksha.com/university/sri-siddhartha-academy-of-higher-education-tumkur-64603",
    "https://www.shiksha.com/college/saraswati-institute-of-management-and-technology-rudrapur-187459",
    "https://www.shiksha.com/college/sinhagad-institute-of-business-management-mumbai-189909",
    "https://www.shiksha.com/college/ahmedabad-institute-of-hospitality-management-212187",
    "https://www.shiksha.com/college/sage-university-bhopal-powered-by-seekho-212923",
    "https://www.shiksha.com/college/desportz-vadodara-230818",
    "https://www.shiksha.com/college/bhagwant-institute-of-technology-bit-muzaffarnagar-19604",
    "https://www.shiksha.com/college/m-s-bidve-engineering-college-latur-20543",
    "https://www.shiksha.com/college/noble-post-graduate-college-andhra-pradesh-hyderabad-20791",
    "https://www.shiksha.com/college/vishisht-school-of-management-indore-31751",
    "https://www.shiksha.com/college/impact-institute-of-event-management-iiem-delhi-south-ex-1-32985",
    "https://www.shiksha.com/college/sahyadri-valley-college-of-engineering-and-technology-mumbai-pune-road-pune-36815",
    "https://www.shiksha.com/college/ibmr-business-school-jhajjar-146699",
    "https://www.shiksha.com/college/pirens-institute-of-business-management-and-administration-ahmednagar-147731",
    "https://www.shiksha.com/college/kushagra-professional-college-ujjain-156969",
    "https://www.shiksha.com/college/vision-school-of-management-and-design-balewadi-pune-212993",
    "https://www.shiksha.com/college/bhaderwah-campus-doda-213421",
    "https://www.shiksha.com/college/mamta-institute-of-education-siwan-229393",
    "https://www.shiksha.com/college/college-of-hospitality-and-tourism-faridabad-3034",
    "https://www.shiksha.com/college/gokula-krishna-college-of-engineering-nellore-20063",
    "https://www.shiksha.com/college/rattan-institute-of-technology-and-management-ritm-haryana-haryana-other-27924",
    "https://www.shiksha.com/college/prannath-parnami-institute-for-professional-studies-hisar-37466",
    "https://www.shiksha.com/college/acn-college-of-engineering-and-management-studies-aligarh-37573",
    "https://www.shiksha.com/college/abr-college-of-engineering-and-technology-abrcet-prakasam-46311",
    "https://www.shiksha.com/college/brindavan-college-of-management-studies-rmv-extension-bangalore-54309",
    "https://www.shiksha.com/college/modern-group-of-instituitons-ghaziabad-59987",
    "https://www.shiksha.com/college/dnr-college-of-engineering-and-technology-bhimavaram-60722",
    "https://www.shiksha.com/college/indian-retail-school-delhi-naraina-28502",
    "https://www.shiksha.com/college/college-of-advanced-technology-studies-cats-dickenson-road-bangalore-32072",
    "https://www.shiksha.com/college/affinity-business-school-bhubaneswar-33983",
    "https://www.shiksha.com/college/aimfill-international-visakhapatnam-37099",
    "https://www.shiksha.com/college/st-soldier-institute-of-engineering-and-technology-jalandhar-43237",
    "https://www.shiksha.com/college/bbs-institute-of-management-technology-allahabad-43363",
    "https://www.shiksha.com/college/thadomal-shahani-centre-for-media-and-communication-bandra-west-mumbai-47747",
    "https://www.shiksha.com/college/klr-college-of-business-management-khammam-48991",
    "https://www.shiksha.com/college/ufly-international-cochin-kochi-57465",
    "https://www.shiksha.com/college/mes-institute-of-technology-and-management-chathannoor-kollam-60505",
    "https://www.shiksha.com/college/aurobindo-college-of-business-management-olive-p-g-college-telangana-other-62035",
    "https://www.shiksha.com/college/accman-business-school-greater-noida-64039",
    "https://www.shiksha.com/college/jyoti-college-of-management-science-and-technology-bareilly-68617",
    "https://www.shiksha.com/college/chanakya-foundation-college-patna-124771",
    "https://www.shiksha.com/college/indian-school-of-commerce-kochi-156637",
    "https://www.shiksha.com/college/real-institute-of-management-and-research-nagpur-64375",
    "https://www.shiksha.com/college/centre-for-management-studies-and-research-kherva-mehsana-66555",
    "https://www.shiksha.com/college/rudra-group-of-institutions-meerut-68635",
    "https://www.shiksha.com/college/government-arts-college-udhagamandalam-tamil-nadu-other-71789",
    "https://www.shiksha.com/college/people-s-college-nanded-74423",
    "https://www.shiksha.com/college/sagar-institute-of-pharmaceutical-sciences-88057",
    "https://www.shiksha.com/college/rc-patel-institute-of-pharmacy-shirpur-89121",
    "https://www.shiksha.com/college/sarada-degree-college-prakasam-115721",
    "https://www.shiksha.com/university/shri-dharmasthala-manjunatheshwara-university-dharwad-182477",
    "https://www.shiksha.com/college/betwanchal-group-of-institutions-vidisha-230050",
    "https://www.shiksha.com/college/pma-safi-human-resources-institute-malappuram-232382",
    "https://www.shiksha.com/college/disha-institute-of-science-and-technology-uttar-pradesh-other-3177",
    "https://www.shiksha.com/college/gimt-geeta-institute-of-management-and-technology-kurukshetra-31008",
    "https://www.shiksha.com/college/sri-sai-group-of-institutes-badhani-pathankot-37062",
    "https://www.shiksha.com/college/management-commerce-institute-of-global-synergy-ajmer-37085",
    "https://www.shiksha.com/college/inurture-swarrnim-university-ahmedabad-145939",
    "https://www.shiksha.com/college/laxmi-bai-sahuji-institute-of-management-jabalpur-147293",
    "https://www.shiksha.com/college/sree-amman-institute-of-management-and-research-erode-148403",
    "https://www.shiksha.com/college/christ-institute-of-management-ghaziabad-199863",
    "https://www.shiksha.com/college/footwear-design-and-development-institute-guna-204805",
    "https://www.shiksha.com/college/sree-sastha-institute-of-engineering-and-technology-powered-by-sunstone-chembarambakkam-chennai-212259",
    "https://www.shiksha.com/college/gla-university-seekho-mathura-212297",
    "https://www.shiksha.com/college/government-arts-and-science-college-idappadi-salem-213267",
    "https://www.shiksha.com/university/bharti-vishwavidyalaya-durg-226951",
    "https://www.shiksha.com/college/ahmedabad-business-school-s-p-ring-road-240950",
    "https://www.shiksha.com/college/international-management-centre-south-ex-1-delhi-4250",
    "https://www.shiksha.com/college/business-school-of-delhi-greater-noida-23691",
    "https://www.shiksha.com/college/maharishi-arvind-school-of-management-studies-jaipur-30777",
    "https://www.shiksha.com/college/pkg-group-of-institutions-panipat-32300",
    "https://www.shiksha.com/college/school-of-new-team-i-ashok-nagar-bangalore-33197",
    "https://www.shiksha.com/college/patel-institute-of-management-and-technology-rajpura-68331",
    "https://www.shiksha.com/college/daripally-anantha-ramulu-college-of-engineering-and-technology-khammam-68395",
    "https://www.shiksha.com/college/radha-devi-ramchandra-mangal-institute-neemuch-121689",
    "https://www.shiksha.com/college/atlas-ideal-international-college-malappuram-147087",
    "https://www.shiksha.com/college/icri-sandeep-university-nashik-153027",
    "https://www.shiksha.com/college/sheela-devi-institute-of-management-and-technology-faridabad-156209",
    "https://www.shiksha.com/college/selvam-college-of-technology-namakkal-193831",
    "https://www.shiksha.com/college/indian-institute-of-fashion-and-design-mohali-202729",
    "https://www.shiksha.com/college/nath-school-of-business-and-technology-aurangabad-205125",
    "https://www.shiksha.com/college/lbsim-lal-bahadur-shastri-institute-of-management-and-technology-bareilly-20503",
    "https://www.shiksha.com/college/r-s-college-of-management-science-karnataka-bangalore-20936",
    "https://www.shiksha.com/college/anand-school-of-engineering-and-technology-agra-22419",
    "https://www.shiksha.com/college/ct-institute-of-engineering-management-and-technology-jalandhar-24809",
    "https://www.shiksha.com/college/ratan-global-business-school-telangana-other-30872",
    "https://www.shiksha.com/college/green-heaven-institute-of-management-and-research-ghimr-nagpur-31151",
    "https://www.shiksha.com/college/shri-jain-diwakar-mahavidyalaya-indore-147181",
    "https://www.shiksha.com/college/khajuraho-institute-of-pharmaceutical-sciences-chhatarpur-147301",
    "https://www.shiksha.com/college/adarsh-shikshan-prasarak-mandal-s-k-t-patil-college-of-mba-osmanabad-228593",
    "https://www.shiksha.com/college/sri-chundi-ranganayakulu-engineering-college-screc-guntur-2656",
    "https://www.shiksha.com/college/bits-group-of-institutions-bits-bhiwani-haryana-other-3991",
    "https://www.shiksha.com/college/maharishi-institute-of-management-mim-noida-greater-noida-20574",
    "https://www.shiksha.com/college/oxford-engineering-college-tiruchirappalli-20815",
    "https://www.shiksha.com/college/sai-spurthi-institute-of-technology-ssit-khammam-21056",
    "https://www.shiksha.com/college/indo-german-training-centre-bangalore-cunningham-road-city-22654",
    "https://www.shiksha.com/college/the-techno-school-tts-bhubaneswar-23420",
    "https://www.shiksha.com/college/cii-institute-of-logistics-velachery-chennai-23575",
    "https://www.shiksha.com/college/punjab-institute-of-management-and-technology-gobindgarh-24382",
    "https://www.shiksha.com/college/sant-longowal-institute-of-engineering-and-technology-sangrur-25241",
    "https://www.shiksha.com/college/vns-business-school-vnsbs-bhopal-37446",
    "https://www.shiksha.com/college/vivekananda-group-of-institutions-batasingaram-village-ramoji-film-city-hyderabad-43281",
    "https://www.shiksha.com/college/chinmaya-institute-of-management-cooke-town-bangalore-37925",
    "https://www.shiksha.com/college/gateway-institute-of-engineering-and-technology-gateway-education-sonepat-38658",
    "https://www.shiksha.com/college/modern-engineering-and-management-studies-balasore-48008",
    "https://www.shiksha.com/college/ganadipathy-tulsi-s-jain-engineering-college-vellore-61681",
    "https://www.shiksha.com/college/pydah-college-pg-courses-visakhapatnam-62435",
    "https://www.shiksha.com/college/rayalaseema-institute-of-information-and-management-sciences-tirupati-62545",
    "https://www.shiksha.com/college/institute-of-management-and-science-bhusawal-jalgaon-72567",
    "https://www.shiksha.com/college/palanisamy-college-of-arts-erode-74311",
    "https://www.shiksha.com/college/tirupur-kumaran-college-for-women-77449",
    "https://www.shiksha.com/college/u-c-college-ernakulum-77473",
    "https://www.shiksha.com/college/nachiketa-institute-of-management-and-information-technology-jabalpur-106589",
    "https://www.shiksha.com/college/thanthai-hans-roever-college-of-education-perambalur-141893",
    "https://www.shiksha.com/college/vikrant-institute-of-management-gwalior-147109",
    "https://www.shiksha.com/college/shree-balaji-institute-of-professional-studies-indore-147189",
    "https://www.shiksha.com/college/vivekanand-arts-commerce-college-chandrapur-190293",
    "https://www.shiksha.com/university/bhagwant-global-university-uttarakhand-other-65589",
    "https://www.shiksha.com/college/s-n-g-institute-of-management-and-research-maharashtra-other-69041",
    "https://www.shiksha.com/college/sai-rajeswari-institute-of-technology-kadapa-70899",
    "https://www.shiksha.com/college/central-india-college-of-business-management-and-studies-nagpur-71141",
    "https://www.shiksha.com/college/global-institute-of-management-and-technology-markarpur-krishna-71731",
    "https://www.shiksha.com/college/swaraj-institute-of-management-satara-77173",
    "https://www.shiksha.com/college/horticulture-vocational-education-institute-jawaharlal-nehru-krishi-vishwavidyalaya-sagar-106261",
    "https://www.shiksha.com/college/xavier-institute-of-management-jabalpur-205207",
    "https://www.shiksha.com/college/isbr-business-school-powered-by-sunstone-select-electronic-city-phase-1-bangalore-213095",
    "https://www.shiksha.com/college/institute-of-environment-and-management-lucknow-3268",
    "https://www.shiksha.com/college/ambedkar-institute-of-management-studies-aims-vishakhapatnam-visakhapatnam-4495",
    "https://www.shiksha.com/college/regency-institute-of-technology-andhra-pradesh-other-25470",
    "https://www.shiksha.com/college/beehive-college-of-management-technology-bcmt-dehradun-30484",
    "https://www.shiksha.com/college/sadanam-institute-of-commerce-and-management-studies-sicoms-palakkad-30927",
    "https://www.shiksha.com/college/k-k-modi-international-institute-lajpat-nagar-delhi-32220",
    "https://www.shiksha.com/college/don-bosco-pg-college-guntur-62475",
    "https://www.shiksha.com/college/institute-of-engineering-technology-chennai-68609",
    "https://www.shiksha.com/college/maharanis-commerce-and-management-college-for-women-mysore-68661",
    "https://www.shiksha.com/college/arya-school-of-management-and-information-technology-bhubaneswar-70745",
    "https://www.shiksha.com/college/t-b-m-l-college-nagapattinam-77211",
    "https://www.shiksha.com/college/aggarwal-college-faridabad-122101",
    "https://www.shiksha.com/college/dr-l-b-college-visakhapatnam-124261",
    "https://www.shiksha.com/college/sevantilal-kantilal-school-of-business-management-patan-146607",
    "https://www.shiksha.com/college/iasscom-fortune-institute-of-technology-bhopal-147339",
    "https://www.shiksha.com/college/don-bosco-technical-institute-dbti-okhla-delhi-150145",
    "https://www.shiksha.com/college/rajarshi-chhatrapati-shahu-maharaj-college-of-agriculture-business-management-sangli-1539,07"
    "https://www.shiksha.com/college/shriram-school-of-business-studies-morena-210165",
    "https://www.shiksha.com/college/institute-of-management-studies-ashok-nagar-ashoknagar-210195",
    "https://www.shiksha.com/college/cimage-center-of-digital-technology-and-entrepreneurship-patna-232578",
    "https://www.shiksha.com/college/jss-college-of-arts-commerce-and-science-jsscacs-mysore-3702",
    "https://www.shiksha.com/college/prof-ram-meghe-college-of-engineering-and-management-badnera-amravati-60437",
    "https://www.shiksha.com/college/sree-venkateswara-college-of-engineering-nellore-61025",
    "https://www.shiksha.com/college/vasavi-institute-of-management-and-computer-science-kadapa-62525",
    "https://www.shiksha.com/college/mother-theresa-institute-of-management-andhra-pradesh-other-68729",
    "https://www.shiksha.com/college/st-joseph-s-college-for-women-visakhapatnam-68885",
    "https://www.shiksha.com/college/rjs-first-grade-college-koramangala-bangalore-69481",
    "https://www.shiksha.com/college/bunts-sangha-s-higher-education-institutions-kurla-east-mumbai-71035",
    "https://www.shiksha.com/college/tips-school-of-management-coimbatore-91679",
    "https://www.shiksha.com/college/abdulkalam-institute-of-technological-sciences-telangana-other-97451",
    "https://www.shiksha.com/university/himalayiya-university-dehradun-145989",
    "https://www.shiksha.com/college/international-school-of-business-east-godavari-146207",
    "https://www.shiksha.com/college/indore-international-college-dhar-147327",
    "https://www.shiksha.com/college/aspire-institute-indore-147473",
    "https://www.shiksha.com/college/jaya-institute-of-business-management-khammam-148497",
    "https://www.shiksha.com/college/meerut-institute-of-technology-149165",
    "https://www.shiksha.com/college/international-institute-of-aviation-bangalore-kudalu-gate-56909",
    "https://www.shiksha.com/college/international-centre-of-excellence-in-engineering-and-management-aurangabad-59631",
    "https://www.shiksha.com/college/kakinada-institute-of-engineering-and-technology-east-godavari-61333",
    "https://www.shiksha.com/college/nips-hotel-management-ranchi-63265",
    "https://www.shiksha.com/university/konkan-krishi-vidyapeeth-ratnagiri-64841",
    "https://www.shiksha.com/college/shri-vivekananda-institute-of-science-guntakal-68801",
    "https://www.shiksha.com/college/craft-development-institute-srinagar-71315",
    "https://www.shiksha.com/college/gandhi-institute-of-management-studies-rayagada-71681",
    "https://www.shiksha.com/college/k-k-parekh-institute-of-management-studies-amreli-72541",
    "https://www.shiksha.com/college/brindavan-college-national-fgc-bangalore-115481",
    "https://www.shiksha.com/college/i-b-m-r-college-of-computer-application-dharwad-115603",
    "https://www.shiksha.com/college/atma-college-bangalore-146855",
    "https://www.shiksha.com/college/dream-sky-aviation-training-academy-pathanamthitta-152807",
    "https://www.shiksha.com/college/omega-post-graduate-college-m-c-a-ghatkesar-194257",
    "https://www.shiksha.com/college/shri-vaishnav-insitute-of-manegment-gwalior-210191",
    "https://www.shiksha.com/college/ufly-international-bangalore-jayanagar-57453",
    "https://www.shiksha.com/college/sanskaar-college-of-management-and-computer-applications-allahabad-60023",
    "https://www.shiksha.com/college/nashik-gramin-shikshan-prasarak-mandal-brahma-valley-institute-of-management-64639",
    "https://www.shiksha.com/college/tdl-college-of-technology-and-management-lucknow-125981",
    "https://www.shiksha.com/college/haridwar-education-college-kanya-gurukul-campus-134391",
    "https://www.shiksha.com/college/shrimad-rajchandra-institute-of-management-and-computer-application-surat-146579",
    "https://www.shiksha.com/college/preston-college-gwalior-147243",
    "https://www.shiksha.com/college/anant-institute-of-business-studies-ashoknagar-147481",
    "https://www.shiksha.com/college/sardar-vallabh-bhai-patel-mahavidyalaya-madhya-pradesh-other-147521",
    "https://www.shiksha.com/college/management-and-research-centre-v-m-d-lotlikar-vidya-sankul-mumbai-189875",
    "https://www.shiksha.com/college/gurukul-college-beraisa-bhopal-197061",
    "https://www.shiksha.com/university/aurora-higher-education-and-research-academy-deemed-to-be-university-hyderabad-211609",
    "https://www.shiksha.com/college/anushashan-institute-of-management-katni-230128",
    "https://www.shiksha.com/college/g-h-raisoni-college-of-engineering-and-management-nagpur-236820",
    "https://www.shiksha.com/college/cruise-culinary-academy-visakhapatnam-240128",
    "https://www.shiksha.com/college/dr-k-v-subba-reddy-college-of-engineering-for-women-kvsw-kurnool-46498",
    "https://www.shiksha.com/college/surendera-group-of-institutions-sriganaganagar-46880",
    "https://www.shiksha.com/college/naraina-college-of-engineering-and-technology-kanpur-52789",
    "https://www.shiksha.com/college/balaji-institute-of-engineering-and-management-studies-nellore-54533",
    "https://www.shiksha.com/college/srm-trp-engineering-college-tiruchirappalli-54733",
    "https://www.shiksha.com/college/corporate-institute-of-science-and-technology-bhopal-59183",
    "https://www.shiksha.com/college/mit-college-of-management-moradabad-59983",
    "https://www.shiksha.com/college/laxmipati-institute-of-science-technology-bhopal-60357",
    "https://www.shiksha.com/college/g-s-college-of-commerce-wardha-64229",
    "https://www.shiksha.com/college/mass-college-of-arts-and-science-thanjavur-66337",
    "https://www.shiksha.com/college/christhu-raj-college-trichy-68681",
    "https://www.shiksha.com/college/d-l-patel-institute-of-management-and-technology-sabarkantha-71345",
    "https://www.shiksha.com/college/imperial-college-bargarh-72255",
    "https://www.shiksha.com/college/marudhar-kesari-jain-college-for-women-vaniyambadi-73479",
    "https://www.shiksha.com/college/omkarananda-institute-of-management-and-technology-dehradun-74203",
    "https://www.shiksha.com/college/dav-college-amritsar-25375",
    "https://www.shiksha.com/university/pratap-university-jaipur-38054",
    "https://www.shiksha.com/college/institute-of-business-management-and-research-ibmr-kolkata-e-m-bypass-40727",
    "https://www.shiksha.com/college/aihm-noida-47427",
    "https://www.shiksha.com/college/itm-skills-academy-navi-mumbai-mumbai-49036",
    "https://www.shiksha.com/college/dwaraka-doss-goverdhan-doss-vaishnav-college-arumbakkam-chennai-49449",
    "https://www.shiksha.com/college/school-of-business-management-and-commerce-mvn-university-palwal-53363",
    "https://www.shiksha.com/college/smit-saroj-mohan-institute-of-technology-hooghly-53867",
    "https://www.shiksha.com/college/westford-international-college-okhla-delhi-56417",
    "https://www.shiksha.com/college/nagarjuna-institute-of-engineering-technology-management-nagpur-59703",
    "https://www.shiksha.com/college/mahatma-gandhi-universe-institute-unnao-59971",
    "https://www.shiksha.com/college/balaji-institute-of-it-and-management-kadapa-62467",
    "https://www.shiksha.com/college/noble-college-of-engineering-technology-for-women-nadargul-hyderabad-63719",
    "https://www.shiksha.com/college/adhunik-institute-of-productivity-management-research-ghaziabad-65545",
    "https://www.shiksha.com/college/navneet-college-of-technology-management-azamgarh-65549",
    "https://www.shiksha.com/college/gokul-institute-of-technology-and-sciences-andhra-pradesh-other-23332",
    "https://www.shiksha.com/college/dns-group-of-institutions-amroha-24969",
    "https://www.shiksha.com/college/ghaziabad-institute-of-hotel-management-gihm-25260",
    "https://www.shiksha.com/college/sengunthar-arts-and-science-college-namakkal-25785",
    "https://www.shiksha.com/college/krishna-institute-of-management-meerut-30542",
    "https://www.shiksha.com/college/gopabandhu-school-of-hotel-management-bhubaneswar-30910",
    "https://www.shiksha.com/college/institute-of-integrated-marketing-communication-and-management-sarita-vihar-delhi-31535",
    "https://www.shiksha.com/college/imperial-college-of-business-studies-icbs-jayanagar-jayanagar-bangalore-35985",
    "https://www.shiksha.com/college/iimt-school-of-management-ism-gurgaon-36591",
    "https://www.shiksha.com/college/quba-college-of-engineering-and-technology-qcet-nellore-43271",
    "https://www.shiksha.com/college/school-of-rural-management-ratlam-47412",
    "https://www.shiksha.com/college/management-academy-for-digital-economy-in-india-banashankari-bangalore-55299",
    "https://www.shiksha.com/college/sri-mittapalli-college-of-engineering-guntur-60873",
    "https://www.shiksha.com/college/jesus-pg-college-ranga-reddy-62109",
    "https://www.shiksha.com/college/rcr-institute-of-management-and-technology-chittoor-62429",
    "https://www.shiksha.com/college/aurora-s-school-of-business-studies-ramanthapur-hyderabad-156559",
    "https://www.shiksha.com/college/veer-college-of-management-vidisha-157061",
    "https://www.shiksha.com/college/dr-d-y-patil-school-of-business-management-pune-179833",
    "https://www.shiksha.com/college/university-institute-of-management-thiruvananthapuram-194491",
    "https://www.shiksha.com/college/t-john-group-of-institutions-powered-by-sunstone-bangalore-212285",
    "https://www.shiksha.com/college/rathinam-technical-campus-powered-by-sunstone-coimbatore-239388",
    "https://www.shiksha.com/college/institute-of-management-and-technology-imt-thrissur-25034",
    "https://www.shiksha.com/college/indira-school-of-career-studies-navi-mumbai-mumbai-26560",
    "https://www.shiksha.com/college/ramesh-chand-institute-of-management-ghaziabad-30574",
    "https://www.shiksha.com/college/a-m-reddy-memorial-college-of-engineering-and-technology-guntur-46813",
    "https://www.shiksha.com/college/met-center-for-insurance-training-research-development-bandra-west-mumbai-47092",
    "https://www.shiksha.com/college/shree-rama-educational-society-group-of-institutions-tirupati-47929",
    "https://www.shiksha.com/college/department-of-nonviolence-and-peace-jain-vishva-bharati-institute-rajasthan-other-54128",
    "https://www.shiksha.com/college/swift-technical-campus-patiala-59257",
    "https://www.shiksha.com/college/s-s-agrawal-institute-of-engineering-and-technology-navsari-60157",
    "https://www.shiksha.com/college/prashant-institute-of-professional-studies-gwalior-156977",
    "https://www.shiksha.com/college/vee-academy-gwalior-157093",
    "https://www.shiksha.com/college/nrupatunga-institute-of-technology-and-management-hyderabad-244294",
    "https://www.shiksha.com/college/hindustan-college-of-arts-and-science-kelambakkam-chennai-2946",
    "https://www.shiksha.com/college/mec-mahendra-engineering-college-namakkal-20596",
    "https://www.shiksha.com/college/vimal-jyoti-engineering-college-vjec-kannur-24538",
    "https://www.shiksha.com/college/trident-et-group-of-institutions-ghaziabad-32027",
    "https://www.shiksha.com/college/meri-college-of-engineering-and-technology-meri-cet-bahadurgarh-37432",
    "https://www.shiksha.com/college/lifestyle-and-luxury-management-institute-llmi-chandigarh-37688",
    "https://www.shiksha.com/college/vaishnavi-institute-of-technology-vitt-tirupati-43197",
    "https://www.shiksha.com/college/bridge-school-of-management-gurugram-gurgaon-48441",
    "https://www.shiksha.com/college/vijaya-institute-of-management-khammam-62337",
    "https://www.shiksha.com/college/dr-kariappa-school-of-art-and-design-management-bangalore-63887",
    "https://www.shiksha.com/college/gate-institute-of-technology-and-management-sciences-tirupati-63957",
    "https://www.shiksha.com/university/sri-sathya-sai-institute-of-higher-learning-anantapur-64725",
    "https://www.shiksha.com/college/avanthi-s-st-theressa-institute-of-engineering-and-technology-vizianagaram-23017",
    "https://www.shiksha.com/college/oasis-college-of-science-and-management-undri-pune-24536",
    "https://www.shiksha.com/college/sunder-deep-college-of-management-and-technology-ghaziabad-25056",
    "https://www.shiksha.com/college/msnimt-member-sree-narayana-pillai-institute-of-management-and-technology-kerala-other-25289",
    "https://www.shiksha.com/college/csr-center-of-excellence-mysore-36423",
    "https://www.shiksha.com/college/marwadi-education-foundation-s-group-of-institutions-mefgi-rajkot-37142",
    "https://www.shiksha.com/college/mjrp-college-of-corporate-management-mjrp-ccm-jaipur-40459",
    "https://www.shiksha.com/college/royal-institute-of-technology-and-science-ranga-reddy-46597",
    "https://www.shiksha.com/college/maxx-academy-faridabad-48763",
    "https://www.shiksha.com/college/tmi-academy-of-travel-tourism-and-aviation-studies-kolkata-chowringhee-49295",
    "https://www.shiksha.com/college/raval-institute-of-hotel-management-mira-road-mumbai-54589",
    "https://www.shiksha.com/college/stock-market-institute-jayanagar-bangalore-57021",
    "https://www.shiksha.com/college/sri-sarathi-institute-of-engineering-and-technology-andhra-pradesh-other-60895",
    "https://www.shiksha.com/college/gandhi-academy-of-technology-and-engineering-ganjam-61395",
    "https://www.shiksha.com/college/sivaji-college-of-engineering-and-technology-kanyakumari-61717",
    "https://www.shiksha.com/college/sunstone-patel-institute-of-management-studies-bellandur-bangalore-205095",
    "https://www.shiksha.com/college/kopal-institute-of-management-studies-bhopal-210185",
    "https://www.shiksha.com/college/institute-for-innovative-and-integrated-management-studies-mumbai-239240",
    "https://www.shiksha.com/college/veeranari-chakali-ilama-womens-university-hyderabad-244296",
    "https://www.shiksha.com/college/karavali-group-of-colleges-mangalore-22136",
    "https://www.shiksha.com/college/smot-school-of-business-smot-perungudi-chennai-27142",
    "https://www.shiksha.com/college/sun-institute-of-management-studies-udaipur-28174",
    "https://www.shiksha.com/college/multani-mal-modi-college-patiala-31569",
    "https://www.shiksha.com/college/asia-pacific-institute-of-management-ahmedabad-ashram-road-33014",
    "https://www.shiksha.com/college/aryabhatt-college-of-engineering-and-technology-acet-baghpat-33101",
    "https://www.shiksha.com/college/bimt-bells-institute-of-management-technology-shimla-34465",
    "https://www.shiksha.com/college/bsbs-business-academy-bannerghatta-road-bangalore-35984",
    "https://www.shiksha.com/college/rkdf-institute-of-science-and-technology-rkdfist-bhopal-40375",
    "https://www.shiksha.com/college/agmr-college-of-engineering-and-technology-agmr-hubli-49359",
    "https://www.shiksha.com/college/avlon-academy-dehradun-52868",
    "https://www.shiksha.com/college/university-of-kashmir-north-campus-baramulla-104905",
    "https://www.shiksha.com/college/abc-college-of-education-patna-125585",
    "https://www.shiksha.com/college/sophitorium-management-college-khurda-148005",
    "https://www.shiksha.com/college/r-v-s-college-of-engineering-and-technology-dindigul-148455",
    "https://www.shiksha.com/college/college-of-agriculture-business-management-shrinagar-latur-153915",
    "https://www.shiksha.com/college/priyatam-institute-of-technology-and-science-indore-154121",
    "https://www.shiksha.com/college/sai-nath-college-of-management-gwalior-157001",
    "https://www.shiksha.com/college/devkinandan-college-of-management-gwalior-157085",
    "https://www.shiksha.com/college/krishnaveni-degree-college-narasaraopet-188691",
    "https://www.shiksha.com/college/matoshri-pratishthan-s-school-of-management-nanded-189463",
    "https://www.shiksha.com/college/university-college-for-women-warangal-194483",
    "https://www.shiksha.com/college/gayatri-institute-of-management-khordha-209005",
    "https://www.shiksha.com/college/bharat-institute-of-management-and-technology-balasore-209007",
    "https://www.shiksha.com/college/vijay-laxmi-college-of-management-gwalior-210155",
    "https://www.shiksha.com/college/sri-sathya-sai-academy-of-management-excellence-thiruvananthapuram-213037",
    "https://www.shiksha.com/college/shri-ram-murti-smarak-college-of-engineering-and-technology-lucknow-49442",
    "https://www.shiksha.com/college/kailash-narayan-patidar-college-of-science-and-technology-bhopal-60345",
    "https://www.shiksha.com/college/krishnaveni-engineering-college-for-women-narasaraopet-60612",
    "https://www.shiksha.com/college/mandava-institute-of-engineering-and-technology-krishna-60682",
    "https://www.shiksha.com/college/king-college-of-technology-namakkal-61597",
    "https://www.shiksha.com/college/ranganathan-engineering-college-coimbatore-61609",
    "https://www.shiksha.com/college/cms-college-of-engineering-namakkal-62053",
    "https://www.shiksha.com/college/sairam-institute-of-management-east-godavari-62399",
    "https://www.shiksha.com/college/s-a-v-acharya-institute-of-management-studies-karjat-mumbai-64175",
    "https://www.shiksha.com/college/g-karunakaran-memorial-co-operative-college-of-management-and-technology-thiruvananthapuram-65879",
    "https://www.shiksha.com/college/k-d-polytechnic-college-patan-66751",
    "https://www.shiksha.com/college/sri-vaishnavi-college-of-engineering-srikakulam-66801",
    "https://www.shiksha.com/college/dr-bhimrao-ambedkar-university-agra-civil-lines-campus-68339",
    "https://www.shiksha.com/college/swami-vivekanand-college-of-science-and-technology-bhopal-68719",
    "https://www.shiksha.com/college/phonics-school-of-enginerring-and-business-administration-roorkee-123645",
    "https://www.shiksha.com/college/aurous-institute-of-management-aim-lucknow-32762",
    "https://www.shiksha.com/college/shivdan-singh-institute-of-technology-and-management-aligarh-34609",
    "https://www.shiksha.com/college/malineni-perumallu-educational-society-s-group-of-institutions-guntur-49400",
    "https://www.shiksha.com/college/excellency-group-of-institutions-alwal-hyderabad-51858",
    "https://www.shiksha.com/college/jp-institute-of-management-meerut-52761",
    "https://www.shiksha.com/college/intech-institute-of-business-management-kanakapura-road-bangalore-54293",
    "https://www.shiksha.com/college/rsr-rungta-college-of-engineering-and-technology-bhilai-59027",
    "https://www.shiksha.com/college/kandula-obul-reddy-memorial-college-of-engineering-kadapa-60566",
    "https://www.shiksha.com/college/sri-sai-college-of-it-and-management-kadapa-62403",
    "https://www.shiksha.com/college/ramana-institute-of-technology-west-godavari-62543",
    "https://www.shiksha.com/college/shivneri-institute-of-business-management-taluka-shirur-pune-64321",
    "https://www.shiksha.com/college/svmvv-sangha-s-institute-of-management-studies-bagalkot-67307",
    "https://www.shiksha.com/college/karuna-post-graduate-college-narayanguda-hyderabad-68401",
    "https://www.shiksha.com/college/sir-c-v-raman-institute-of-management-andhra-pradesh-other-68807",
    "https://www.shiksha.com/college/vvs-post-graduate-college-rajahmundry-68925",
    "https://www.shiksha.com/college/symbiosis-centre-for-corporate-education-symbiosis-international-pune-senapati-bapat-road-155189",
    "https://www.shiksha.com/college/vidya-devi-college-of-management-gwalior-157057",
    "https://www.shiksha.com/college/jaihind-college-of-management-bhopal-157089",
    "https://www.shiksha.com/college/gyansthaly-mahavidhyalaya-jhansi-180071",
    "https://www.shiksha.com/college/skyline-crs-kharadi-pune-181387",
    "https://www.shiksha.com/college/vidyalankar-institute-of-technology-mumbai-189821",
    "https://www.shiksha.com/college/siddhartha-women-s-degree-college-hyderabad-210341",
    "https://www.shiksha.com/college/vikram-sarabhai-institute-of-engineering-technology-noida-greater-noida-231940",
    "https://www.shiksha.com/college/champaran-college-of-professional-education-east-champaran-bihar-other-242374",
    "https://www.shiksha.com/college/sri-satyanarayana-engineering-college-ssnec-andhra-pradesh-other-2641",
    "https://www.shiksha.com/college/marian-engineering-college-thiruvananthapuram-20623",
    "https://www.shiksha.com/college/unique-institute-of-management-and-technology-ghaziabad-24394",
    "https://www.shiksha.com/college/applied-college-of-management-and-engineering-haryana-other-24852",
    "https://www.shiksha.com/college/modern-institute-of-technology-rishikesh-25027",
    "https://www.shiksha.com/college/vision-school-of-management-udaipur-25188",
    "https://www.shiksha.com/college/netaji-school-of-management-nalgonda-62165",
    "https://www.shiksha.com/college/vaageswari-institute-of-management-sciences-telangana-other-62187",
    "https://www.shiksha.com/college/patronage-institute-of-management-studies-greater-noida-62681",
    "https://www.shiksha.com/college/akole-taluka-education-societys-technical-campus-college-ahmednagar-64651",
    "https://www.shiksha.com/college/narmadeshwar-management-college-lucknow-65533",
    "https://www.shiksha.com/college/nmam-institute-of-technology-udupi-66357",
    "https://www.shiksha.com/college/vivekanand-arts-sardar-dalipsingh-commerce-and-science-college-aurangabad-66859",
    "https://www.shiksha.com/college/systel-institute-of-management-and-research-dhule-67095",
    "https://www.shiksha.com/college/international-school-of-design-dehradun-67493",
    "https://www.shiksha.com/college/annai-women-s-college-karur-68701",
    "https://www.shiksha.com/college/siddardha-college-of-computer-science-andhra-pradesh-other-68803",
    "https://www.shiksha.com/college/guru-harkrishan-girls-college-sangrur-72081",
    "https://www.shiksha.com/college/kruti-group-of-institutions-raipur-72743",
    "https://www.shiksha.com/college/pee-gee-college-of-arts-and-science-dharmapuri-74397",
    "https://www.shiksha.com/college/wisdom-school-of-management-pollanchi-pollachi-77977",
    "https://www.shiksha.com/college/arunai-engineering-college-tamil-nadu-other-24031",
    "https://www.shiksha.com/college/compucom-institute-of-technology-management-jaipur-24054",
    "https://www.shiksha.com/college/guru-teg-bahadur-khalsa-institute-of-engineering-and-technology-muktsar-26269",
    "https://www.shiksha.com/college/commits-institute-of-journalism-and-mass-communication-h-s-r-layout-bangalore-26730",
    "https://www.shiksha.com/college/jindal-school-of-hotel-management-sigma-university-vadodara-28927",
    "https://www.shiksha.com/college/shri-dhondu-baliram-pawar-college-of-management-nashik-37064",
    "https://www.shiksha.com/college/cardinal-cleemis-school-of-management-studies-ccsms-trivandrum-37695",
    "https://www.shiksha.com/college/csc-candid-school-of-communication-salt-lake-city-kolkata-38350",
    "https://www.shiksha.com/college/akrg-college-of-engineering-and-technology-andhra-pradesh-other-43291",
    "https://www.shiksha.com/college/vvce-vidhya-vikaas-college-of-engineering-and-technology-namakkal-43323",
    "https://www.shiksha.com/college/synetic-business-school-ludhiana-57495",
    "https://www.shiksha.com/college/haindavi-pg-college-mba-anantapur-62485",
    "https://www.shiksha.com/college/sri-venkateswara-school-of-business-anantapur-63959",
    "https://www.shiksha.com/college/smt-padambai-kapurchandji-kotecha-mahila-mahavidyalaya-bhusawal-64867",
    "https://www.shiksha.com/college/patel-group-of-institutions-mehsana-69159",
    "https://www.shiksha.com/college/ansh-college-of-management-gwalior-147479",
    "https://www.shiksha.com/college/guru-nanak-institute-of-technology-ranga-reddy-154209",
    "https://www.shiksha.com/college/swami-vivekanand-institute-of-management-tikamgarh-madhya-pradesh-other-210159",
    "https://www.shiksha.com/college/rj-school-of-management-studies-rjsms-tentulipura-orissa-other-21778",
    "https://www.shiksha.com/college/shri-balwant-institute-of-technology-sonepat-21947",
    "https://www.shiksha.com/college/vishveshwarya-school-of-business-management-greater-noida-30689",
    "https://www.shiksha.com/college/angel-institute-of-international-hospitality-management-greater-noida-31604",
    "https://www.shiksha.com/college/bls-institute-of-management-ghaziabad-32280",
    "https://www.shiksha.com/college/dc-business-school-indore-34629",
    "https://www.shiksha.com/college/neesa-institute-of-management-studies-gandhinagar-34632",
    "https://www.shiksha.com/college/inifd-jalandhar-35202",
    "https://www.shiksha.com/college/massco-media-jhandewalan-delhi-35445",
    "https://www.shiksha.com/college/bse-institute-limited-chennai-teynampet-35890",
    "https://www.shiksha.com/college/national-institute-of-business-excellence-electronic-city-bangalore-38546",
    "https://www.shiksha.com/college/sims-sengunthar-institute-of-management-studies-tamil-nadu-other-42512",
    "https://www.shiksha.com/college/pacific-business-school-udaipur-62581",
    "https://www.shiksha.com/college/rjspm-s-institute-of-computer-and-management-research-alandi-pune-64307",
    "https://www.shiksha.com/college/ideal-institute-of-management-kondigre-kolhapur-67341",
    "https://www.shiksha.com/college/k-l-b-d-a-v-college-for-girls-palampur-68245",
    "https://www.shiksha.com/college/sai-baba-adarsh-mahavidyalaya-chhattisgarh-other-69095",
    "https://www.shiksha.com/college/culinary-guru-institute-of-hotel-management-hyderabad-70279",
    "https://www.shiksha.com/college/college-of-advance-computing-berhampur-71249",
    "https://www.shiksha.com/college/pillai-hoc-institute-of-management-studies-and-research-phimsr-raigad-73249",
    "https://www.shiksha.com/college/swami-vivekanand-college-of-professional-studies-sehore-77127",
    "https://www.shiksha.com/college/scs-autonomous-college-puri-119225",
    "https://www.shiksha.com/college/mahaguru-institute-of-technology-alleppey-147047",
    "https://www.shiksha.com/college/sks-institute-of-business-studies-indore-147161",
    "https://www.shiksha.com/college/s-r-college-bhopal-147221",
    "https://www.shiksha.com/college/excel-business-school-indore-147437",
    "https://www.shiksha.com/college/kanchi-pallavan-engineering-college-kanchipuram-148235",
    "https://www.shiksha.com/college/international-institute-of-fashion-technology-naraina-naraina-delhi-41217",
    "https://www.shiksha.com/college/bhutta-college-of-engineering-and-technology-ludhiana-43191",
    "https://www.shiksha.com/college/sri-mittapalli-institute-of-technology-for-women-smitw-guntur-47920",
    "https://www.shiksha.com/college/n-c-college-of-engineering-panipat-53170",
    "https://www.shiksha.com/college/institute-of-hotel-management-and-culinary-science-jaipur-58543",
    "https://www.shiksha.com/college/dr-om-prakash-institute-of-management-technology-uttar-pradesh-other-59871",
    "https://www.shiksha.com/college/jp-school-of-business-meerut-59939",
    "https://www.shiksha.com/college/m-k-group-of-institutes-amritsar-60415",
    "https://www.shiksha.com/college/rise-krishna-sai-gandhi-group-of-institutions-ongole-60937",
    "https://www.shiksha.com/college/amrita-institution-amrita-vishwa-vidyapeetham-nagercoil-campus-66293",
    "https://www.shiksha.com/college/ckd-institute-of-management-and-technology-taran-taran-tarn-taran-66563",
    "https://www.shiksha.com/college/innocent-hearts-group-of-institutions-jalandhar-66727",
    "https://www.shiksha.com/college/aditya-degree-college-kakinada-67205",
    "https://www.shiksha.com/college/visakha-institute-for-professional-studies-visakhapatnam-68917",
    "https://www.shiksha.com/college/sachchidananda-sinha-college-magadh-university-bihar-other-69077",
    "https://www.shiksha.com/college/madha-engineering-college-kanchipuram-193839",
    "https://www.shiksha.com/college/kopal-college-for-excellence-bhopal-196787",
    "https://www.shiksha.com/college/a-veeriya-vandayar-memorial-sri-pushpam-college-savvmspc-thanjavur-24019",
    "https://www.shiksha.com/college/institute-of-engineering-and-technology-alwar-24935",
    "https://www.shiksha.com/college/abhinav-hi-tech-college-of-engineering-ahtc-himayat-nagar-hyderabad-25497",
    "https://www.shiksha.com/college/uei-global-ludhiana-36360",
    "https://www.shiksha.com/college/hasmukh-goswami-college-of-engineering-nava-naroda-ahmedabad-38260",
    "https://www.shiksha.com/college/monarch-international-college-of-hotel-management-michm-ooty-41110",
    "https://www.shiksha.com/college/yogananda-institute-of-technology-and-science-tirupati-42703",
    "https://www.shiksha.com/college/christ-institute-of-technology-formerly-dr-s-j-s-paul-memorial-college-of-engineering-and-technology-pondicherry-48067",
    "https://www.shiksha.com/college/biluru-gurubasava-mahaswamiji-institute-of-technology-karnataka-other-59505",
    "https://www.shiksha.com/college/st-mark-educational-institution-society-group-of-institution-anantapur-61007",
    "https://www.shiksha.com/college/sahaja-school-of-business-karimnagar-62333",
    "https://www.shiksha.com/college/bhavan-s-priyamvada-birla-institute-of-management-mysore-63487",
    "https://www.shiksha.com/college/aklia-group-of-institutions-bathinda-65175",
    "https://www.shiksha.com/college/arignar-anna-college-krishnagiri-193727",
    "https://www.shiksha.com/college/icri-mewar-university-chittorgarh-212191",
    "https://www.shiksha.com/college/vikrama-simhapuri-university-post-graduate-center-kavali-andhra-pradesh-other-212375",
    "https://www.shiksha.com/college/sanjivani-group-of-institutes-ahmednagar-214781",
    "https://www.shiksha.com/college/koneru-lakshmaiah-education-foundation-ranga-reddy-232452",
    "https://www.shiksha.com/college/niilm-school-of-business-badarpur-delhi-4324",
    "https://www.shiksha.com/college/prakasam-engineering-college-22878",
    "https://www.shiksha.com/college/panchkula-engineering-college-pec-panchkula-24418",
    "https://www.shiksha.com/college/srinivas-school-of-business-ssb-mangalore-24737",
    "https://www.shiksha.com/college/regional-college-for-education-research-and-technology-jaipur-24739",
    "https://www.shiksha.com/college/hdf-school-of-management-cuttack-27201",
    "https://www.shiksha.com/college/bitm-bengal-institute-of-technology-and-management-kolkata-31097",
    "https://www.shiksha.com/college/millennium-school-of-business-msob-delhi-subhash-nagar-31122",
    "https://www.shiksha.com/college/maharishi-arvind-institute-of-engineering-and-technology-jaipur-38100",
    "https://www.shiksha.com/college/regional-college-jaipur-39379",
    "https://www.shiksha.com/college/gokul-group-of-institutions-vizianagaram-63537",
    "https://www.shiksha.com/college/venkateshwara-institue-of-management-sangli-64263",
    "https://www.shiksha.com/college/shrimant-jayshreemaladevi-naik-nimbalkar-institute-of-management-studies-satara-64347",
    "https://www.shiksha.com/college/raja-rajesheshwari-college-of-engineering-mysore-road-bangalore-69479",
    "https://www.shiksha.com/college/csird-institute-of-management-anantapur-71323",
    "https://www.shiksha.com/college/high-rank-business-school-noida-72169",
    "https://www.shiksha.com/college/ojaswani-institute-of-management-and-technology-damoh-74179",
    "https://www.shiksha.com/college/sai-krishna-post-graduate-college-telangana-other-75389",
    "https://www.shiksha.com/college/shree-markandeshwar-institute-of-management-kurukshetra-146681",
    "https://www.shiksha.com/college/indore-international-college-sawer-147325",
    "https://www.shiksha.com/college/bafna-college-madhya-pradesh-other-147465",
    "https://www.shiksha.com/college/nss-college-of-management-mathura-149065",
    "https://www.shiksha.com/college/rishi-institute-of-engineering-and-technology-meerut-149103",
    "https://www.shiksha.com/college/international-centre-for-advance-studies-and-research-icasr-gurgaon-150351",
    "https://www.shiksha.com/college/hm-school-of-business-management-khordha-156359",
    "https://www.shiksha.com/college/sistec-school-of-management-studies-bhopal-49302",
    "https://www.shiksha.com/college/kc-group-of-institutions-una-52060",
    "https://www.shiksha.com/college/panache-academy-vadodara-55445",
    "https://www.shiksha.com/university/mahatma-gandhi-university-meghalaya-meghalaya-other-57679",
    "https://www.shiksha.com/college/aihm-institute-of-tourism-and-hotel-management-greater-noida-58119",
    "https://www.shiksha.com/college/gogate-jogalekar-college-ratnagiri-58935",
    "https://www.shiksha.com/college/nri-institute-of-technology-agiripalli-krishna-60861",
    "https://www.shiksha.com/college/sai-tirumala-n-v-r-engineering-college-narasaraopet-60947",
    "https://www.shiksha.com/college/rai-technology-university-hubli-61291",
    "https://www.shiksha.com/college/horizon-institute-of-technology-ranga-reddy-62103",
    "https://www.shiksha.com/college/vivekananda-institute-of-science-and-information-technology-telangana-other-62279",
    "https://www.shiksha.com/college/velankanni-institute-of-management-studies-nellore-62519",
    "https://www.shiksha.com/college/sri-indu-institute-of-engineering-and-technology-ranga-reddy-63751",
    "https://www.shiksha.com/college/kalka-group-of-institutions-meerut-67485",
    "https://www.shiksha.com/college/gayatri-college-of-management-sambalpur-68679",
    "https://www.shiksha.com/college/venkateshwara-institute-of-technology-meerut-184281",
    "https://www.shiksha.com/college/gh-raisoni-institute-of-information-technology-nagpur-189225",
    "https://www.shiksha.com/college/jagannath-university-powered-by-sunstone-jaipur-213097",
    "https://www.shiksha.com/college/kmct-institute-of-technology-and-management-kuttipuram-kerala-other-213473",
    "https://www.shiksha.com/college/siddhartha-womens-degree-college-ranga-reddy-232456",
    "https://www.shiksha.com/college/motilal-rastogi-school-of-management-lucknow-4305",
    "https://www.shiksha.com/college/lorven-college-of-science-and-management-anekal-bangalore-5729",
    "https://www.shiksha.com/college/purushottam-institute-of-engineering-and-technology-piet-rourkela-20925",
    "https://www.shiksha.com/college/thiruvalluvar-college-of-engineering-and-technology-tamil-nadu-other-23059",
    "https://www.shiksha.com/college/sachdeva-engineering-college-for-girls-mohali-28683",
    "https://www.shiksha.com/college/siet-institute-of-management-mysore-road-bangalore-32721",
    "https://www.shiksha.com/college/aihm-institute-of-tourism-and-hotel-management-agra-34627",
    "https://www.shiksha.com/college/fmg-group-of-institutions-greater-noida-36260",
    "https://www.shiksha.com/college/care-school-of-business-management-tiruchirappalli-37124",
    "https://www.shiksha.com/college/vaagdevi-institute-of-technology-and-science-vits-kadapa-37821",
    "https://www.shiksha.com/college/bm-institute-of-professional-studies-bm-group-of-institutions-indore-68513",
    "https://www.shiksha.com/college/aps-college-of-education-and-technology-meerut-68619",
    "https://www.shiksha.com/college/l-j-institute-of-computer-applications-ahmedabad-68723",
    "https://www.shiksha.com/college/sri-venkateswara-paladugu-nagaiah-chowdary-and-kotha-raghuramaiah-group-of-institutions-narasaraopet-68747",
    "https://www.shiksha.com/college/s-v-arts-and-science-college-nellore-68787",
    "https://www.shiksha.com/college/mrm-institute-of-management-telangana-other-68961",
    "https://www.shiksha.com/college/the-navkonkan-education-societys-institute-of-management-studies-ratnagiri-77339",
    "https://www.shiksha.com/college/sri-annamacharya-institute-of-technology-and-sciences-rajampet-kadapa-89305",
    "https://www.shiksha.com/college/kbr-engineering-college-telangana-other-99175",
    "https://www.shiksha.com/college/sau-sunitatai-eknathrao-dhakane-polytehnic-college-ahmednagar-99203",
    "https://www.shiksha.com/college/jain-institute-gwalior-120561",
    "https://www.shiksha.com/college/sri-s-r-education-college-neemuch-142641",
    "https://www.shiksha.com/college/siddartha-educational-academy-group-of-institutions-chittoor-146283",
    "https://www.shiksha.com/college/r-p-inderaprastha-institute-of-technology-karnal-146691",
    "https://www.shiksha.com/college/sapphire-institute-of-business-management-indore-147205",
    "https://www.shiksha.com/college/nimra-institute-of-engineering-and-technology-andhra-pradesh-other-43243",
    "https://www.shiksha.com/college/transglobe-school-of-logistics-and-aviation-management-kochi-52417",
    "https://www.shiksha.com/college/prananath-college-bhubaneswar-59071",
    "https://www.shiksha.com/college/e-max-group-of-institutions-ambala-60377",
    "https://www.shiksha.com/college/fatima-michael-college-of-engineering-and-technology-madurai-61779",
    "https://www.shiksha.com/college/sahaja-institute-of-technology-sciences-for-women-karimnagar-62231",
    "https://www.shiksha.com/college/suprabhath-pg-college-nalgonda-62321",
    "https://www.shiksha.com/college/global-institute-of-technology-and-management-sciences-kadapa-62477",
    "https://www.shiksha.com/college/dr-k-v-subba-reddy-institute-of-mca-kurnool-63961",
    "https://www.shiksha.com/college/k-b-h-institute-of-management-and-research-nashik-64653",
    "https://www.shiksha.com/college/srix-school-of-entrepreneurship-warangal-65699",
    "https://www.shiksha.com/college/ckd-institute-of-management-and-technology-amritsar-66303",
    "https://www.shiksha.com/college/k-r-pandav-mahavidyalaya-nagpur-66745",
    "https://www.shiksha.com/college/mgsm-s-arts-science-and-commerce-college-jalgaon-67087",
    "https://www.shiksha.com/college/sri-kalahasthiswara-institute-of-information-and-management-sciences-andhra-pradesh-other-68835",
    "https://www.shiksha.com/college/malineni-lakshmaiah-mba-college-prakasam-188399",
    "https://www.shiksha.com/college/mahatma-gandhi-mission-s-institute-of-management-aurangabad-190543",
    "https://www.shiksha.com/college/bharathidasan-school-of-business-erode-193783",
    "https://www.shiksha.com/college/aringar-anna-institute-of-management-studies-and-computer-application-chennai-193797",
    "https://www.shiksha.com/college/sri-balaji-post-graduate-college-siddipet-194043",
    "https://www.shiksha.com/college/khammam-institute-of-technology-and-science-194157",
    "https://www.shiksha.com/college/visvesvaraya-college-of-engineering-technology-hyderabad-194161",
    "https://www.shiksha.com/college/jahangirabad-educational-group-of-institutions-faculty-of-management-barabanki-201909",
    "https://www.shiksha.com/college/hill-woods-academy-of-higher-education-gandhinagar-228873",
    "https://www.shiksha.com/college/sitasrm-institute-of-management-and-technology-simt-greater-noida-239974",
    "https://www.shiksha.com/college/haryana-college-of-technology-and-management-hctm-kaithal-23658",
    "https://www.shiksha.com/college/r-d-foundation-group-of-institutions-modinagar-33104",
    "https://www.shiksha.com/college/rajasthan-college-of-engineering-for-women-rcew-jaipur-36041",
    "https://www.shiksha.com/college/regional-institute-of-management-rim-jhajjar-37377",
    "https://www.shiksha.com/college/surya-group-of-institutions-lucknow-37458",
    "https://www.shiksha.com/college/nagarjuna-p-g-college-nalgonda-62353",
    "https://www.shiksha.com/college/seshachala-institute-of-management-studies-chittoor-62417",
    "https://www.shiksha.com/college/yalamarty-institute-of-computer-sciences-visakhapatnam-62501",
    "https://www.shiksha.com/college/landmark-technical-campus-uttar-pradesh-other-65747",
    "https://www.shiksha.com/college/bharat-group-of-colleges-mansa-66533",
    "https://www.shiksha.com/college/surajmal-laxmidevi-sawarthia-educational-trust-s-group-of-institutions-haldwani-66823",
    "https://www.shiksha.com/college/amruta-institute-of-engineering-and-management-sciences-karnataka-other-67253",
    "https://www.shiksha.com/college/maa-bhagwata-kunwar-institute-of-management-uttar-pradesh-other-68977",
    "https://www.shiksha.com/college/raak-arts-and-science-college-villupuram-74735",
    "https://www.shiksha.com/college/talent-institute-of-management-studies-malappuram-77255",
    "https://www.shiksha.com/college/vidhya-sagar-institute-of-management-bhopal-77681",
    "https://www.shiksha.com/college/vinayak-vidyapeeth-meerut-77785",
    "https://www.shiksha.com/college/sri-vani-group-of-institutions-krishna-87687",
    "https://www.shiksha.com/college/sun-international-institute-of-tourism-and-management-rushikonda-visakhapatnam-101697",
    "https://www.shiksha.com/college/sai-institute-of-paramedical-and-allied-science-dehradun-111837",
    "https://www.shiksha.com/college/adamas-university-seekho-barasat-kolkata-212307",
    "https://www.shiksha.com/college/chennais-amirta-thrissur-216101",
    "https://www.shiksha.com/college/delight-management-studies-and-research-institute-pune-243914",
    "https://www.shiksha.com/college/st-anthony-s-college-karnataka-other-245046",
    "https://www.shiksha.com/college/dvr-college-of-engineering-technology-patancheru-hyderabad-19968",
    "https://www.shiksha.com/college/chts-institute-of-hotel-management-catering-and-tourism-lucknow-21717",
    "https://www.shiksha.com/college/nova-college-of-engineering-and-technology-andhra-pradesh-other-22845",
    "https://www.shiksha.com/college/shaheed-udham-singh-group-of-institutions-mohali-24386",
    "https://www.shiksha.com/college/m-d-group-of-education-agra-25711",
    "https://www.shiksha.com/college/lorra-business-academy-loraa-bommanahalli-bangalore-29999",
    "https://www.shiksha.com/college/merc-institute-of-management-mulshi-pune-30784",
    "https://www.shiksha.com/college/rayat-institute-of-management-s-b-s-nagar-punjab-other-36220",
    "https://www.shiksha.com/college/sarada-institute-of-technology-and-management-krishna-37295",
    "https://www.shiksha.com/college/khader-memorial-college-of-engineering-and-technology-kmcet-nalgonda-43263",
    "https://www.shiksha.com/college/kishan-institute-of-information-technology-kiit-meerut-44714",
    "https://www.shiksha.com/college/royal-school-of-information-and-management-sciences-chittoor-62423",
    "https://www.shiksha.com/college/b-a-and-k-r-mca-college-prakasam-62637",
    "https://www.shiksha.com/college/college-of-management-and-computer-science-yavatmal-64233",
    "https://www.shiksha.com/college/swargiya-shri-laxmanji-motghare-charitable-trust-dr-arun-motghare-college-of-management-maharashtra-other-64627",
    "https://www.shiksha.com/university/the-institute-of-chartered-financial-analysts-of-india-university-meghalaya-meghalaya-other-64947",
    "https://www.shiksha.com/college/asia-pacific-institute-of-information-technology-panipat-65347",
    "https://www.shiksha.com/university/shyam-university-dausa-65449",
    "https://www.shiksha.com/college/devender-singh-institute-of-technology-and-management-ghaziabad-65505",
    "https://www.shiksha.com/college/ferozpur-institute-of-mangagement-68687",
    "https://www.shiksha.com/college/holy-angels-school-of-business-tamil-nadu-other-72189",
    "https://www.shiksha.com/college/kandula-lakshumma-college-of-engineering-for-women-kadapa-72605",
    "https://www.shiksha.com/college/s-v-r-school-of-business-management-ranga-reddy-75267",
    "https://www.shiksha.com/college/shrinathji-institute-of-biotechnology-and-management-rajsamand-76255",
    "https://www.shiksha.com/college/takshila-college-bhopal-77247",
    "https://www.shiksha.com/college/mother-teresa-institute-of-science-and-technology-krishna-99475",
    "https://www.shiksha.com/college/jai-maa-pitambra-college-of-management-datia-157097",
    "https://www.shiksha.com/college/sharadchandra-pawar-institute-of-management-and-research-baramati-pune-179817",
    "https://www.shiksha.com/college/lloyd-school-of-management-studies-noida-180053",
    "https://www.shiksha.com/college/varaha-lakshmi-narasimhaswamy-educational-group-of-institutions-visakhapatnam-188401",
    "https://www.shiksha.com/college/anurag-group-of-institutions-hyderabad-194159",
    "https://www.shiksha.com/college/fort-institute-of-technology-meerut-201903",
    "https://www.shiksha.com/college/shri-dattakripa-shaikshnik-va-krishi-gram-vikas-pratishthans-saikrupa-institute-of-management-science-ahmednagar-202153",
    "https://www.shiksha.com/college/suraj-college-of-engineering-and-technology-mahendragarh-202271",
    "https://www.shiksha.com/college/izee-group-of-institutions-powered-by-sunstone-hennur-main-road-bangalore-213061",
    "https://www.shiksha.com/college/unitech-b-school-tathawade-pune-214485",
    "https://www.shiksha.com/college/shikshan-prasarak-sanstha-s-m-b-a-institute-sangamner-ahmednagar-228505",
    "https://www.shiksha.com/college/acmt-group-of-colleges-uttrakhand-campus-nainital-228777",
    "https://www.shiksha.com/college/shivsamarth-institute-of-management-talmawale-satara-243910",
    "https://www.shiksha.com/college/d-n-r-college-dnrc-andhra-pradesh-andhra-pradesh-other-25060",
    "https://www.shiksha.com/college/tirumala-engineering-college-trml-ranga-reddy-25151",
    "https://www.shiksha.com/college/gyan-bharti-institute-of-technology-meerut-59891",
    "https://www.shiksha.com/college/jayamukhi-institute-of-management-science-warangal-62107",
    "https://www.shiksha.com/college/sree-kavitha-institute-of-management-khammam-62255",
    "https://www.shiksha.com/college/krr-institute-of-information-technology-telangana-other-62349",
    "https://www.shiksha.com/college/dr-agarala-eswara-reddi-mba-college-chittoor-62439",
    "https://www.shiksha.com/college/aryabhatta-college-of-management-ajmer-62583",
    "https://www.shiksha.com/college/sunrise-group-of-institutions-udaipur-66817",
    "https://www.shiksha.com/college/adept-institute-of-management-studies-and-research-dharwad-67305",
    "https://www.shiksha.com/college/lakshmi-narain-college-of-technology-and-science-indore-67677",
    "https://www.shiksha.com/college/gnanamani-institute-of-management-studies-namakkal-68645",
    "https://www.shiksha.com/college/krishnarpit-institute-of-management-and-technology-allahabad-68667",
    "https://www.shiksha.com/college/maa-omwati-institute-of-management-and-technology-haryana-other-68979",
    "https://www.shiksha.com/college/unnati-management-college-mathura-77535",
    "https://www.shiksha.com/college/v-m-v-college-nagpur-77891",
    "https://www.shiksha.com/college/hill-side-institute-of-management-bangalore-115495",
    "https://www.shiksha.com/college/maharashtra-institute-of-information-technology-beed-189987",
    "https://www.shiksha.com/college/vathsalya-institute-of-science-and-technology-nalgonda-194069",
    "https://www.shiksha.com/college/medhavi-institute-of-management-jabalpur-210167",
    "https://www.shiksha.com/college/ilam-zee-himgiri-universty-dehradun-213135",
    "https://www.shiksha.com/college/rajan-mamta-degree-college-aurangabad-bihar-other-242396",
    "https://www.shiksha.com/college/universal-institute-of-hotel-management-uihm-dehradun-242702",
    "https://www.shiksha.com/university/dr-k-n-modi-university-modinagar-244128",
    "https://www.shiksha.com/college/inderprastha-engineering-college-ghaziabad-24096",
    "https://www.shiksha.com/college/srishti-school-of-business-banashankari-bangalore-30000",
    "https://www.shiksha.com/college/uei-global-raipur-36362",
    "https://www.shiksha.com/college/jhunjhunwala-business-school-jbs-faizabad-uttar-pradesh-other-37441",
    "https://www.shiksha.com/college/tiffin-aviation-services-sholinganallur-chennai-41515",
    "https://www.shiksha.com/college/teachers-academy-group-of-institutions-kalyan-nagar-bangalore-41588",
    "https://www.shiksha.com/college/shankara-group-of-institution-shankara-institute-of-technology-jaipur-42326",
    "https://www.shiksha.com/college/vivekanandha-institute-of-engineering-technology-for-women-vivekanandha-educational-institutions-for-women-namakkal-43192",
    "https://www.shiksha.com/college/k-s-jain-institute-of-engineering-and-technology-modinagar-65231",
    "https://www.shiksha.com/college/swami-vivekanad-technical-college-ludhiana-67325",
    "https://www.shiksha.com/college/surabhi-college-of-engineering-and-technology-bhopal-67675",
    "https://www.shiksha.com/college/einstein-post-graduate-college-saroornagar-hyderabad-68397",
    "https://www.shiksha.com/college/shivam-institute-of-management-gujarat-other-69199",
    "https://www.shiksha.com/college/smt-s-a-patel-bed-college-mehsana-69273",
    "https://www.shiksha.com/college/rohitash-institute-of-management-mahendragarh-69333",
    "https://www.shiksha.com/college/shri-atamanand-jain-institute-of-management-and-technology-ambala-69343",
    "https://www.shiksha.com/college/gnanam-school-of-business-thanjavur-71737",
    "https://www.shiksha.com/college/vasavi-vidya-trust-group-of-institutions-salem-77599",
    "https://www.shiksha.com/college/kites-degree-college-visakhapatnam-115841",
    "https://www.shiksha.com/college/cherraan-s-arts-science-college-tirupur-140191",
    "https://www.shiksha.com/college/tellakula-jalayya-polisetty-somasundaram-college-guntur-146263",
    "https://www.shiksha.com/college/vip-college-of-management-bhopal-147127",
    "https://www.shiksha.com/college/iaeer-pibm-s-institute-of-pgdm-pune-147745",
    "https://www.shiksha.com/college/visvesvaraya-technological-university-chickaballapur-chikballpura-201929",
    "https://www.shiksha.com/college/alia-institute-of-management-bhopal-210193",
    "https://www.shiksha.com/college/government-arts-and-science-college-tondairpet-tondiarpet-chennai-228359",
    "https://www.shiksha.com/college/edept-ashok-nagar-bangalore-240296",
    "https://www.shiksha.com/college/friends-union-for-energizing-lives-pune-243932",
    "https://www.shiksha.com/college/daksha-pg-college-mysuru-mysore-244780",
    "https://www.shiksha.com/college/uttaranchal-p-g-college-of-bio-medical-sciences-and-hospital-dehradun-23157",
    "https://www.shiksha.com/college/skyline-educational-institutes-greater-noida-24980",
    "https://www.shiksha.com/college/nidt-professionals-andheri-andheri-west-mumbai-27483",
    "https://www.shiksha.com/college/iet-group-of-institutions-ropar-28995",
    "https://www.shiksha.com/college/sai-ram-institute-of-business-and-management-studies-sribms-mathura-30591",
    "https://www.shiksha.com/college/nutan-maharashtra-institute-of-engineering-and-technology-talegaon-dabhade-pune-34610",
    "https://www.shiksha.com/college/uei-global-faridabad-36356",
    "https://www.shiksha.com/college/sat-kabir-institute-of-technolgy-and-management-bahadurgarh-36383",
    "https://www.shiksha.com/college/asbs-institute-for-management-excellence-and-development-asbs-imex-dhankawadi-pune-38034",
    "https://www.shiksha.com/college/amara-institute-of-engineering-and-technology-andhra-pradesh-other-62635",
    "https://www.shiksha.com/college/pragathi-degree-college-andhra-pradesh-other-68753",
    "https://www.shiksha.com/college/arcot-sri-mahalaalakshmi-women-s-institute-of-management-and-computer-applications-vellore-70703",
    "https://www.shiksha.com/college/institute-of-management-and-planning-and-advance-computer-training-patna-72315",
    "https://www.shiksha.com/college/smt-kumudben-darbar-college-of-commerce-science-and-management-studies-bijapur-72789",
    "https://www.shiksha.com/college/laxmi-narayan-academy-of-management-gwalior-72917",
    "https://www.shiksha.com/college/rama-institute-of-higher-education-uttar-pradesh-other-74901",
    "https://www.shiksha.com/college/shivnagar-education-societys-insitute-of-management-baramati-75927",
    "https://www.shiksha.com/college/saraswati-group-of-colleges-mohali-91751",
    "https://www.shiksha.com/college/dr-z-h-institute-of-technology-and-management-agra-125753",
    "https://www.shiksha.com/college/trivedi-institute-of-management-and-technology-uttar-pradesh-other-125987",
    "https://www.shiksha.com/college/kamla-nehru-college-nagpur-141511",
    "https://www.shiksha.com/college/k-r-academy-dewas-143117",
    "https://www.shiksha.com/college/aadarsh-mahavidhyalaya-madhya-pradesh-other-147499",
    "https://www.shiksha.com/college/swatantrata-sainani-institute-of-business-management-indore-147501",
    "https://www.shiksha.com/college/uei-global-jalandhar-36361",
    "https://www.shiksha.com/college/basudev-institute-of-management-and-technology-lucknow-37968",
    "https://www.shiksha.com/university/maharaj-vinayak-global-university-mvgu-jaipur-42540",
    "https://www.shiksha.com/college/c-b-s-college-of-management-agra-42856",
    "https://www.shiksha.com/college/world-media-academy-lower-parel-mumbai-47497",
    "https://www.shiksha.com/college/acs-college-of-engineering-mysore-road-bangalore-47514",
    "https://www.shiksha.com/college/girijabai-sail-institute-of-technology-karnataka-other-47984",
    "https://www.shiksha.com/college/european-union-nehru-place-delhi-47992",
    "https://www.shiksha.com/college/patel-institute-of-technology-bhopal-53633",
    "https://www.shiksha.com/college/ufly-international-hyderabad-sd-road-57447",
    "https://www.shiksha.com/college/bz-global-education-campus-gujarat-other-60193",
    "https://www.shiksha.com/college/jai-bharath-college-of-management-and-engineering-technology-kerala-other-60423",
    "https://www.shiksha.com/college/shree-institute-of-technical-education-tirupati-60969",
    "https://www.shiksha.com/university/dr-c-v-raman-university-madhya-pradesh-khandwa-61813",
    "https://www.shiksha.com/college/svr-institute-of-management-kurnool-62327",
    "https://www.shiksha.com/college/institute-for-technology-and-management-raigad-147941",
    "https://www.shiksha.com/college/asian-school-of-management-khurda-148041",
    "https://www.shiksha.com/college/mar-thoma-school-of-management-studies-kochi-194689",
    "https://www.shiksha.com/college/wings-college-dhar-210143",
    "https://www.shiksha.com/college/rathinam-school-of-business-coimbatore-228369",
    "https://www.shiksha.com/college/global-bifs-academy-nagpur-242348",
    "https://www.shiksha.com/college/vaisiri-first-grade-college-tumkur-244782",
    "https://www.shiksha.com/college/indian-institute-of-art-and-design-gurgaon-245804",
    "https://www.shiksha.com/college/jsb-jyotirmoy-school-of-business-kolkata-mega-city-kolkata-30539",
    "https://www.shiksha.com/college/institute-of-technology-and-sciences-haryana-other-46928",
    "https://www.shiksha.com/college/shine-college-of-management-lucknow-47993",
    "https://www.shiksha.com/college/picasso-academy-of-event-management-paoem-jaipur-48883",
    "https://www.shiksha.com/college/sagar-institute-of-research-and-technology-indore-56279",
    "https://www.shiksha.com/college/nova-college-of-business-management-krishna-146265",
    "https://www.shiksha.com/college/dr-k-v-subba-reddy-school-of-business-management-kurnool-146319",
    "https://www.shiksha.com/college/maharana-pratap-college-of-technology-gwalior-147103",
    "https://www.shiksha.com/college/shri-baglamukhi-institute-of-management-madhya-pradesh-other-147505",
    "https://www.shiksha.com/college/arihant-institute-of-commerce-and-management-thallagattapura-kanakapura-road-bangalore-150839",
    "https://www.shiksha.com/college/sri-institute-of-management-nayagarh-156363",
    "https://www.shiksha.com/college/vindhya-institute-of-management-and-research-satna-156987",
    "https://www.shiksha.com/college/shree-jee-college-of-management-mandsaur-157087",
    "https://www.shiksha.com/college/dhaneswar-rath-institute-of-engineering-and-management-studies-cuttack-195599",
    "https://www.shiksha.com/college/swami-vivekanand-college-of-engineering-indore-196807",
    "https://www.shiksha.com/college/dr-paul-s-engineering-college-pec-villupuram-tamil-nadu-other-19949",
    "https://www.shiksha.com/college/bcet-bangalore-college-of-engineering-and-technology-hosur-road-22454",
    "https://www.shiksha.com/college/bit-institute-of-technology-anantapur-22479",
    "https://www.shiksha.com/college/siddhi-vinayak-group-of-colleges-alwar-27166",
    "https://www.shiksha.com/college/rajeev-business-school-dange-chawk-pune-30072",
    "https://www.shiksha.com/college/techno-engineering-college-indore-60409",
    "https://www.shiksha.com/college/k-lakshumma-memorial-college-of-engineering-for-women-kadapa-60517",
    "https://www.shiksha.com/college/kakinada-institute-of-technology-sciences-ramachandrapuram-tirupati-60558",
    "https://www.shiksha.com/college/paladugu-parvathi-devi-college-of-engineering-and-technology-vijayawada-60871",
    "https://www.shiksha.com/college/sri-vani-educational-society-group-of-institutions-krishna-60903",
    "https://www.shiksha.com/college/v-r-college-of-management-and-information-technology-warangal-62299",
    "https://www.shiksha.com/college/adithe-satyanarayana-pg-college-east-godavari-62461",
    "https://www.shiksha.com/college/shree-vivekananda-institute-of-science-anantapur-62531",
    "https://www.shiksha.com/college/saastra-college-of-computer-science-nellore-62533",
    "https://www.shiksha.com/college/chaitanya-bharathi-institute-of-technology-pallavolu-andhra-pradesh-other-63501",
    "https://www.shiksha.com/college/vcd-college-of-designing-udaipur-63629",
    "https://www.shiksha.com/college/kigyan-groups-jayanagar-bangalore-64941",
    "https://www.shiksha.com/college/geethanjali-college-of-engineering-and-technology-kurnool-65187",
    "https://www.shiksha.com/college/msn-degree-and-pg-college-vizianagaram-68731",
    "https://www.shiksha.com/college/vasavi-jnanapeeta-first-grade-college-bangalore-69713",

]


def build_urls(BASE_URL):
    return {
        "college_info":BASE_URL,
        "courses": BASE_URL + "/courses",
        "fees": BASE_URL + "/fees",
        "reviews": BASE_URL + "/reviews",
        "admission": BASE_URL + "/admission",
        "placement": BASE_URL + "/placement",
        "cutoff": BASE_URL + "/cutoff",
        "ranking": BASE_URL + "/ranking",
        "gallery": BASE_URL + "/gallery",
        "infrastructure": BASE_URL + "/infrastructure",
        "faculty": BASE_URL + "/faculty",
        "compare": BASE_URL + "/compare",
        "scholarships": BASE_URL + "/scholarships",
        # "qna": "https://ask.shiksha.com/which-is-better-for-mba-iim-ahmedabad-or-jbims-qna-5114413"
    }
# ---------------- DRIVER ----------------
def create_driver():
    options = Options()

    # Mandatory for GitHub Actions
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Optional but good
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    # Important for Ubuntu runner
    options.binary_location = "/usr/bin/chromium"

    service = Service(ChromeDriverManager().install())

    return webdriver.Chrome(
        service=service,
        options=options
    )


# ---------------- UTILITIES ----------------
def scroll_to_bottom(driver, scroll_times=3, pause=1.5):
    for _ in range(scroll_times):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(pause)



def scrape_college_info(driver,URLS):
    import re 
    try:
        driver.get(URLS["college_info"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["college_info"])
    
    wait = WebDriverWait(driver, 40)

    data = {
        "college_info": {
            "college_name": None,
            "rating": None,
            "logo":None,
            "cover_image":None,
            "reviews_count": None,
            "qa_count": None,
            "location": None,
            "city": None,
            "institute_type": None,
            "established_year": None,
            "highlights": {
                "summary": None,
                "table": [],
                "faqs": [],
            },
            "intro": None,
            "courses": [],
            "faqs": []
        }
    }
    college_info = data["college_info"]
    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image
        try:
            top_header_section = driver.find_element(By.ID, "topHeaderCard-top-section")
            cover_img = top_header_section.find_element(By.ID, "topHeaderCard-gallery-image")
            college_info["cover_image"] = cover_img.get_attribute("src")
        except:
            pass 
        
        # Extract logo
        try:
            logo_div = driver.find_element(By.CSS_SELECTOR, ".ca46d2.e014b3")
            logo_img = logo_div.find_element(By.TAG_NAME, "img")
            college_info["logo"] = logo_img.get_attribute("src")
        except:
            pass
        
        # Extract videos and photos count
        try:
            badges_div = driver.find_element(By.CSS_SELECTOR, ".e4df0b.ad160e")
            badges = badges_div.find_elements(By.CSS_SELECTOR, ".dcd631")
            
            for badge in badges:
                text = badge.text.lower()
                if "video" in text:
                    videos_match = re.search(r'(\d+)\s*videos?', text)
                    if videos_match:
                        college_info["videos_count"] = int(videos_match.group(1))
                elif "photo" in text:
                    photos_match = re.search(r'(\d+)\s*photos?', text)
                    if photos_match:
                        college_info["photos_count"] = int(photos_match.group(1))
        except:
            pass
        
        # Rest of your existing header extraction code...
        
    except Exception as e:
        pass
    # ================= COLLEGE NAME =================
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    data["college_info"]["college_name"] = driver.find_element(By.TAG_NAME, "h1").text.strip()

    # ================= LOCATION + CITY =================
    loc = driver.find_element(By.CSS_SELECTOR, "span.f90eb6").text
    if "," in loc:
        l, c = loc.split(",", 1)
        data["college_info"]["location"] = l.strip()
        data["college_info"]["city"] = c.strip()

    # ================= RATING =================
    try:
        rating = driver.find_element(By.CSS_SELECTOR, "span.f1b26c").text
        data["college_info"]["rating"] = re.search(r'([\d.]+)', rating).group(1)
    except:
        pass

    # ================= REVIEWS COUNT =================
    try:
        reviews = driver.find_element(By.XPATH, "//a[contains(text(),'Reviews')]").text
        data["college_info"]["reviews_count"] = int(re.search(r'\d+', reviews).group())
    except:
        pass

    # ================= Q&A COUNT =================
    try:
        qa = driver.find_element(By.XPATH, "//a[contains(text(),'Student Q')]").text.lower()
        val = re.search(r'([\d.]+k?)', qa).group(1)
        data["college_info"]["qa_count"] = int(float(val.replace("k", "")) * 1000) if "k" in val else int(val)
    except:
        pass

    # ================= INSTITUTE TYPE + ESTD =================
    for item in driver.find_elements(By.CSS_SELECTOR, "span.b00d1d"):
        txt = item.text
        if "Institute" in txt:
            data["college_info"]["institute_type"] = txt
        if "Estd" in txt:
            data["college_info"]["established_year"] = re.search(r'\d{4}', txt).group()

    # ================= SECTION WAIT =================

    # ================= HIGHLIGHTS SECTION (JS SAFE) =================
    try:
        highlights = wait.until(
            EC.presence_of_element_located((By.ID, "ovp_section_highlights"))
        )

        # 🔹 SUMMARY (improved to get all text content before table)
        summary = driver.execute_script("""
            // Get the main accordion wrapper
            let el = document.querySelector('.faq__according-wrapper');
            if (!el) return null;
            
            // Get all p tags within the wrapper
            let ps = el.querySelectorAll('p');
            let summaryTexts = [];
            
            ps.forEach(p => {
                // Skip paragraphs that are inside the table
                if (p.closest('table')) return;
                
                let t = p.innerText.trim();
                // Collect meaningful paragraphs (not too short)
                if (t.length > 20 && !t.includes('Check out more')) {
                    summaryTexts.push(t);
                }
            });
            
            // Join with proper spacing
            return summaryTexts.join("\\n\\n");
        """)
        data["college_info"]["highlights"]["summary"] = summary if summary else "Summary not available"

        # 🔹 TABLE (IMPROVED with better data extraction)
        table_data = driver.execute_script("""
            // Find all tables within the highlights section
            let tables = document.querySelectorAll('#EdContent__ovp_section_highlights table');
            if (tables.length === 0) return [];
            
            let result = [];
            
            // Process each table
            tables.forEach(table => {
                let rows = table.querySelectorAll('tr');
                
                // Check if this looks like a highlights table (has "Particulars" header)
                let firstRow = rows[0];
                if (firstRow) {
                    let headerText = firstRow.innerText.toLowerCase();
                    if (headerText.includes('particulars') || headerText.includes('highlight')) {
                        
                        // Process rows starting from index 1 (skip header)
                        for (let i = 1; i < rows.length; i++) {
                            let row = rows[i];
                            let cols = row.querySelectorAll('td, th');
                            
                            if (cols.length >= 2) {
                                let key = cols[0].innerText.trim();
                                let value = cols[1].innerText.trim();
                                
                                // Clean up the key (remove trailing colons, etc.)
                                key = key.replace(/[:|]$/, '').trim();
                                
                                // Check if value contains a link
                                let linkElem = cols[1].querySelector('a');
                                let linkData = null;
                                if (linkElem) {
                                    linkData = {
                                        text: linkElem.innerText.trim(),
                                        href: linkElem.getAttribute('href'),
                                        title: linkElem.getAttribute('title') || ''
                                    };
                                }
                                
                                if (key && value) {
                                    result.push({
                                        particular: key,
                                        details: value,
                                        link: linkData
                                    });
                                }
                            }
                        }
                    }
                }
            });
            
            return result;
        """)
        
        # If table_data is empty, try alternative selector
        if not table_data:
            table_data = driver.execute_script("""
                // Alternative: Look for table directly in the accordion wrapper
                let table = document.querySelector('.faq__according-wrapper table');
                if (!table) return [];
                
                let result = [];
                let rows = table.querySelectorAll('tr');
                
                for (let i = 1; i < rows.length; i++) {
                    let row = rows[i];
                    let cells = row.querySelectorAll('td');
                    
                    if (cells.length >= 2) {
                        let key = cells[0].innerText.trim();
                        let value = cells[1].innerText.trim();
                        
                        // Special handling for rankings (multiple lines)
                        if (key.includes('Rankings')) {
                            let pTags = cells[1].querySelectorAll('p');
                            if (pTags.length > 0) {
                                value = Array.from(pTags).map(p => p.innerText.trim()).join(' | ');
                            }
                        }
                        
                        // Check for links
                        let linkElem = cells[1].querySelector('a');
                        let linkData = null;
                        if (linkElem) {
                            linkData = {
                                text: linkElem.innerText.trim(),
                                href: linkElem.getAttribute('href')
                            };
                        }
                        
                        if (key && value) {
                            result.push({
                                particular: key,
                                details: value,
                                link: linkData
                            });
                        }
                    }
                }
                return result;
            """)
        
        # Format the table data better
        formatted_table = []
        for item in table_data:
            # Clean up the details text
            details = item['details']
            # Remove extra whitespace and newlines
            details = ' '.join(details.split())
            
            formatted_item = {
                "particular": item['particular'],
                "details": details
            }
            
            if item.get('link'):
                formatted_item["link"] = item['link']
                
            formatted_table.append(formatted_item)
        
        data["college_info"]["highlights"]["table"] = formatted_table

    except Exception as e:
        data["college_info"]["highlights"]["summary"] = "Summary not available"
        data["college_info"]["highlights"]["table"] = []


    for item in data["college_info"]["highlights"]["table"]:
        print(f"  - {item['particular']}: {item['details'][:50]}...")

    wait.until(
        EC.presence_of_element_located(
            (By.ID, "ovp_section_popular_courses")
        )
    )

    # ================= INTRO / SUMMARY =================
    data["intro"] = driver.execute_script("""
       let el = document.querySelector('#EdContent__ovp_section_popular_courses');
       if (!el) return null;
   
       let ps = el.querySelectorAll('p');
       let out = [];
   
       ps.forEach(p => {
           let t = p.textContent.replace(/\\s+/g, ' ').trim();
           if (t.length > 20) out.push(t);
       });
   
       return out.join("\\n");
       """)

    # ================= COURSES (FIXED) =================
    courses = driver.execute_script("""
        let result = [];

        document.querySelectorAll('div.base_course_tuple > div[id^="tuple_"]').forEach(tuple => {

            let course = {};

            // name + url
            let h3 = tuple.querySelector('h3');
            course.course_name = h3 ? h3.innerText.trim() : null;
            course.course_url = h3 ? h3.closest('a')?.href : null;

            // duration
            let spans = tuple.querySelectorAll('.edfa span');
            course.duration = spans.length > 1 ? spans[1].innerText.trim() : null;

            // rating + reviews
            let ratingBlock = tuple.querySelector('a[href*="reviews"]');
            if (ratingBlock) {
                course.rating = ratingBlock.querySelector('span')?.innerText.trim() || null;
                let r = ratingBlock.querySelector('.e040');
                course.reviews = r ? r.innerText.replace(/[()]/g, '') : null;
            }

            // ranking
            course.ranking =
                tuple.querySelector('.ba04')?.innerText.trim() || null;

            // ===== EXAMS ACCEPTED (SAFE) =====
            course.exams = [];
            tuple.querySelectorAll('label').forEach(label => {
                if (label.innerText.includes('Exams Accepted')) {
                    let ul = label.parentElement.querySelector('ul');
                    if (ul) {
                        ul.querySelectorAll('a').forEach(a => {
                            course.exams.push(a.innerText.trim());
                        });
                    }
                }
            });

            // ===== FEES =====
            course.fees = null;
            tuple.querySelectorAll('label').forEach(label => {
                if (label.innerText.includes('Total Tuition Fees')) {
                    let div = label.parentElement.querySelector('div');
                    if (div) {
                        course.fees = div.innerText.replace('Get Fee Details', '').trim();
                    }
                }
            });

            // ===== SALARY / PLACEMENT =====
            course.median_salary = null;
            tuple.querySelectorAll('label').forEach(label => {
                if (
                    label.innerText.includes('Median Salary') ||
                    label.innerText.includes('Placement Rating')
                ) {
                    let span = label.parentElement.querySelector('span');
                    if (span) {
                        course.median_salary = span.innerText.trim();
                    }
                }
            });

            result.push(course);
        });

        return result;
    """)
    data["courses"] = courses

    # ================= FAQs =================
    # ================= CLEAN FAQS =================
    try:
        faq_section = driver.find_element(By.ID, "sectional-faqs-0")
        driver.execute_script("arguments[0].scrollIntoView(true);", faq_section)
        time.sleep(2)

        questions = faq_section.find_elements(By.CLASS_NAME, "html-0")

        for q in questions:
            driver.execute_script("arguments[0].click();", q)
            time.sleep(0.5)

            question_text = q.text.replace("Q:", "").strip()

            try:
                ans_block = q.find_element(
                    By.XPATH,
                    "./following-sibling::div//div[contains(@class,'facb5f')]"
                )
                answer_text = clean_text(ans_block.text.replace("A:", "").strip())
            except:
                answer_text = ""

            data["college_info"]["highlights"]["faqs"].append({
                "question": question_text,
                "answer": answer_text
            })
    except:
        pass
    # ================= PLACEMENTS SECTION - FIX FOR DYNAMIC CONTENT =================
    try:
        
        
        # Wait for placements section
        placements_section = wait.until(
            EC.presence_of_element_located((By.ID, "ovp_section_placements"))
        )
        
        # Scroll to make sure everything is visible
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", placements_section)
        time.sleep(1)
        
        # Initialize data
        data["placements"] = {
            "overview": "",
            "course_wise_data": [],
            "top_recruiters": [],
            "student_insights": [],
            "faqs": [],
            "key_statistics": {}
        }
        
        # 🔹 1. OVERVIEW TEXT - Try different selectors
        try:
            # Try multiple selector approaches
            overview_selectors = [
                "#ovp_section_placements .wikiContents p",
                "#ovp_section_placements p",
                ".faq__according-wrapper p"
            ]
            
            overview_texts = []
            for selector in overview_selectors:
                try:
                    paragraphs = driver.find_elements(By.CSS_SELECTOR, selector)
                    for p in paragraphs:
                        text = p.text.strip()
                        if text and len(text) > 30:
                            # Skip video descriptions and links
                            if not any(x in text.lower() for x in ['check out', 'video', 'click here', '→']):
                                overview_texts.append(text)
                except:
                    continue
                
                if overview_texts:
                    break
            
            # Take meaningful paragraphs
            meaningful_paras = []
            for text in overview_texts:
                if any(word in text.lower() for word in ['placement', 'package', 'salary', 'offer', 'student']):
                    meaningful_paras.append(text)
            
            if meaningful_paras:
                data["placements"]["overview"] = "\n\n".join(meaningful_paras[:3])
            elif overview_texts:
                data["placements"]["overview"] = "\n\n".join(overview_texts[:3])
            else:
                data["placements"]["overview"] = "Overview not available"
                
        except Exception as e:
            
            data["placements"]["overview"] = "Overview not available"
        
        # 🔹 2. COURSE-WISE SALARIES - Use JavaScript to extract table data
        try:
            course_data = driver.execute_script("""
                // Find the salary table
                const table = document.querySelector('#ovp_section_placements table.table.f866a4.dc8ace');
                if (!table) return [];
                
                const courses = [];
                // Get all rows except header
                const rows = table.querySelectorAll('tbody tr');
                
                rows.forEach(row => {
                    const cells = row.querySelectorAll('td');
                    if (cells.length >= 2) {
                        const courseName = cells[0].textContent.trim();
                        const salary = cells[1].textContent.trim();
                        
                        if (courseName && salary && courseName !== 'Course') {
                            courses.push({
                                name: courseName,
                                median_salary: salary
                            });
                        }
                    }
                });
                
                return courses;
            """)
            
            data["placements"]["course_wise_data"] = course_data
           
            
        except Exception as e:
        
            data["placements"]["course_wise_data"] = []
        
        # 🔹 3. TOP RECRUITERS - Extract from carousel
        try:
            recruiters = driver.execute_script("""
                // Find recruiters in the carousel
                const recruiters = [];
                
                // Method 1: Look for recruiter buttons
                const recruiterButtons = document.querySelectorAll('#ovp_section_placements .e03a2f.f6be89');
                recruiterButtons.forEach(btn => {
                    const span = btn.querySelector('.cfed48.a183a8');
                    if (span) {
                        const name = span.textContent.trim();
                        if (name && name.length > 2) {
                            recruiters.push(name);
                        }
                    }
                });
                
                // Method 2: Look for all spans with recruiter names
                if (recruiters.length === 0) {
                    const allSpans = document.querySelectorAll('#ovp_section_placements span');
                    allSpans.forEach(span => {
                        const text = span.textContent.trim();
                        // Company names are usually in uppercase or have specific patterns
                        if (text && text.length > 2 && text.length < 50 && 
                            (text === text.toUpperCase() || 
                            text.includes('Group') || 
                            text.includes('Consulting') ||
                            text.includes('Bank'))) {
                            recruiters.push(text);
                        }
                    });
                }
                
                // Remove duplicates
                return [...new Set(recruiters)];
            """)
            
            data["placements"]["top_recruiters"] = recruiters
            
            
        except Exception as e:
          
            data["placements"]["top_recruiters"] = []
        
        # 🔹 4. STUDENT INSIGHTS
        try:
            insights = driver.execute_script("""
                const insights = [];
                
                // Find insights section
                const insightCards = document.querySelectorAll('#ovp_section_placements .cdf9a8');
                
                insightCards.forEach(card => {
                    const titleElem = card.querySelector('h6');
                    const descElem = card.querySelector('p');
                    
                    if (titleElem && descElem) {
                        insights.push({
                            category: titleElem.textContent.trim(),
                            feedback: descElem.textContent.trim()
                        });
                    }
                });
                
                return insights;
            """)
            
            data["placements"]["student_insights"] = insights
           
            
        except Exception as e:
        
            data["placements"]["student_insights"] = []
        
        # 🔹 5. FAQS - Extract from FAQ section
        try:
            faqs = driver.execute_script("""
                const faqs = [];
                
                // Find all questions
                const questionElements = document.querySelectorAll('#ovp_section_placements .ea1844');
                
                questionElements.forEach((qElem, index) => {
                    // Extract question text
                    let question = '';
                    const qSpan = qElem.querySelector('.flx-box span:nth-child(3)');
                    if (qSpan) {
                        question = qSpan.textContent.trim();
                    } else {
                        question = qElem.textContent.replace('Q:', '').trim();
                    }
                    
                    if (question) {
                        // Find corresponding answer
                        const nextSibling = qElem.nextElementSibling;
                        let answer = '';
                        
                        if (nextSibling && nextSibling.classList.contains('f61835')) {
                            const answerDiv = nextSibling.querySelector('.wikkiContents');
                            if (answerDiv) {
                                // Get text content, remove unnecessary parts
                                answer = answerDiv.textContent.trim();
                                // Remove "Not satisfied with answer?" part
                                answer = answer.replace(/Not satisfied with answer.*/i, '').trim();
                            }
                        }
                        
                        if (question && answer) {
                            faqs.push({
                                question: question,
                                answer: answer.substring(0, 500) // Limit answer length
                            });
                        }
                    }
                });
                
                return faqs;
            """)
            
            data["placements"]["faqs"] = faqs
           
            
        except Exception as e:
          
            data["placements"]["faqs"] = []
        
        # 🔹 6. KEY STATISTICS
        try:
            # Get text and extract statistics
            all_text = placements_section.text
            
            stats = {}
            import re
            
            # Extract key numbers
            patterns = [
                (r'(\d+)\s*offers.*?presented', 'offers_made'),
                (r'(\d+)\s*students.*?participated', 'students_participated'),
                (r'highest.*?package.*?(INR\s*[\d.,]+\s*LPA)', 'highest_package'),
                (r'average.*?package.*?(INR\s*[\d.,]+\s*LPA)', 'average_package'),
                (r'(\d+%)\s*placement rate', 'placement_rate'),
                (r'(\d+)\s*companies.*?participated', 'companies_participated')
            ]
            
            for pattern, key in patterns:
                match = re.search(pattern, all_text, re.IGNORECASE)
                if match:
                    stats[key] = match.group(1)
            
            data["placements"]["key_statistics"] = stats
            
            
        except Exception as e:
       
            data["placements"]["key_statistics"] = {}
        
     
        
    except Exception as e:
        pass


    # ================= FEES & ELIGIBILITY SECTION =================
    try:
        print("Extracting fees and eligibility data...")
        
        # Wait for the section
        fees_section = wait.until(
            EC.presence_of_element_located((By.ID, "ovp_section_fees_and_eligibility"))
        )
        
        # Scroll to section
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", fees_section)
        time.sleep(1)
        
        # Initialize data structure
        data["fees_and_eligibility"] = {
            "overview": "",
            "courses_table": [],
            "faqs": [],
            "key_statistics": {}
        }
        
        # 🔹 1. OVERVIEW TEXT
        try:
            overview_wrapper = fees_section.find_element(By.CSS_SELECTOR, ".faq__according-wrapper")
            paragraphs = overview_wrapper.find_elements(By.TAG_NAME, "p")
            
            overview_texts = []
            for p in paragraphs:
                text = p.text.strip()
                if text and len(text) > 30:
                    overview_texts.append(text)
            
            data["fees_and_eligibility"]["overview"] = "\n\n".join(overview_texts[:3])
            
            
        except Exception as e:
           
            data["fees_and_eligibility"]["overview"] = "Overview not available"
        
        # 🔹 2. COURSES TABLE DATA
        try:
            # Find the main table
            table = fees_section.find_element(By.CSS_SELECTOR, "table.table.a82bdd")
            
            courses_data = []
            # Get all rows from table body
            rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
            
            for row in rows:
                try:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if len(cells) >= 3:
                        # Course name and count
                        course_cell = cells[0]
                        course_name_elem = course_cell.find_element(By.TAG_NAME, "a")
                        course_name = course_name_elem.text.strip()
                        
                        # Course count
                        try:
                            course_count_elem = course_cell.find_element(By.CLASS_NAME, "d94f03")
                            course_count_text = course_count_elem.text.strip()
                            # Extract number from text like "(4 courses)"
                            import re
                            course_count_match = re.search(r'(\d+)', course_count_text)
                            course_count = int(course_count_match.group(1)) if course_count_match else None
                        except:
                            course_count = None
                        
                        # Tuition fees
                        fees_cell = cells[1]
                        fees_text = fees_cell.text.strip()
                        # Remove "Get Fee Details" text
                        fees_clean = fees_text.replace("Get Fee Details", "").strip()
                        
                        # Eligibility
                        eligibility_cell = cells[2]
                        eligibility_text = eligibility_cell.text.strip()
                        
                        # Extract detailed eligibility information
                        eligibility_data = {}
                        
                        # Check for graduation percentage
                        if "Graduation" in eligibility_text:
                            grad_match = re.search(r'Graduation.*?(\d+)\s*%', eligibility_text)
                            if grad_match:
                                eligibility_data["graduation_percentage"] = f"{grad_match.group(1)}%"
                        
                        # Extract exams
                        exams = []
                        exam_links = eligibility_cell.find_elements(By.TAG_NAME, "a")
                        for exam_link in exam_links:
                            exam_name = exam_link.text.strip()
                            if exam_name:
                                exams.append(exam_name)
                        
                        if exams:
                            eligibility_data["exams"] = exams
                        
                        # Prepare course data
                        course_info = {
                            "course_name": course_name,
                            "course_count": course_count,
                            "tuition_fees": fees_clean,
                            "eligibility": eligibility_data if eligibility_data else eligibility_text
                        }
                        
                        # Add link if available
                        try:
                            course_link = course_name_elem.get_attribute("href")
                            course_info["link"] = course_link
                        except:
                            pass
                        
                        courses_data.append(course_info)
                        
                except Exception as e:
                    
                    continue
            
            data["fees_and_eligibility"]["courses_table"] = courses_data
           
            
        except Exception as e:
           
            data["fees_and_eligibility"]["courses_table"] = []
        
        # 🔹 3. FAQS - FIXED VERSION
        try:
            # First, make sure FAQ section is visible by scrolling to it
            try:
                faq_section_element = fees_section.find_element(By.CSS_SELECTOR, ".sectional-faqs")
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", faq_section_element)
                time.sleep(1)
            except:
                pass
            
            # Use JavaScript to extract FAQs - more reliable
            faqs_data = driver.execute_script("""
                // Find FAQ section within fees section
                const faqSection = document.querySelector('#ovp_section_fees_and_eligibility .sectional-faqs');
                if (!faqSection) return [];
                
                const faqs = [];
                
                // Get all question elements
                const questionElements = faqSection.querySelectorAll('.ea1844');
                
                questionElements.forEach((qElem, index) => {
                    try {
                        // Extract question text
                        let questionText = '';
                        const qSpan = qElem.querySelector('.flx-box span:nth-child(3)');
                        if (qSpan) {
                            questionText = qSpan.textContent.trim();
                        } else {
                            // Fallback: get all text and remove "Q:"
                            questionText = qElem.textContent.replace('Q:', '').trim();
                        }
                        
                        if (questionText) {
                            // Find corresponding answer
                            let answerText = '';
                            let nextElem = qElem.nextElementSibling;
                            
                            // Look for answer in next sibling elements
                            while (nextElem) {
                                if (nextElem.classList && nextElem.classList.contains('f61835')) {
                                    const answerDiv = nextElem.querySelector('.wikkiContents');
                                    if (answerDiv) {
                                        answerText = answerDiv.textContent.trim();
                                        // Clean up answer text
                                        answerText = answerText.replace(/Not satisfied with answer.*/gi, '')
                                                            .replace(/Ask Shiksha GPT.*/gi, '')
                                                            .trim();
                                    }
                                    break;
                                }
                                nextElem = nextElem.nextElementSibling;
                            }
                            
                            if (questionText && answerText) {
                                faqs.push({
                                    question: questionText,
                                    answer: answerText.substring(0, 1500) // Limit length
                                });
                            }
                        }
                    } catch (e) {
                        console.log('Error parsing FAQ:', e);
                    }
                });
                
                return faqs;
            """)
            
            if faqs_data:
                data["fees_and_eligibility"]["faqs"] = faqs_data
                
            else:
              
                try:
                    faq_section = fees_section.find_element(By.CSS_SELECTOR, ".sectional-faqs")
                    
                    # Get all text and parse manually
                    all_faq_text = faq_section.text
                    lines = all_faq_text.split('\n')
                    
                    faqs_list = []
                    current_q = None
                    current_a = []
                    in_answer = False
                    
                    for line in lines:
                        line = line.strip()
                        if not line:
                            continue
                        
                        # Check if this is a question
                        if line.startswith('Q:') or ('?' in line and len(line) < 200):
                            # Save previous FAQ
                            if current_q and current_a:
                                faqs_list.append({
                                    "question": current_q,
                                    "answer": ' '.join(current_a)
                                })
                            
                            # Start new FAQ
                            current_q = line.replace('Q:', '').strip()
                            current_a = []
                            in_answer = True
                        elif in_answer and current_q:
                            # This is part of answer (skip FAQ navigation text)
                            if not any(x in line for x in ['Not satisfied', 'Ask Shiksha GPT', 'View other answers']):
                                current_a.append(line)
                    
                    # Add last FAQ
                    if current_q and current_a:
                        faqs_list.append({
                            "question": current_q,
                            "answer": ' '.join(current_a)
                        })
                    
                    data["fees_and_eligibility"]["faqs"] = faqs_list
                   
                    
                except Exception as e:
                   
                    data["fees_and_eligibility"]["faqs"] = []
            
        except Exception as e:
           
            data["fees_and_eligibility"]["faqs"] = []
        # 🔹 4. KEY STATISTICS (from overview)
        try:
            stats = {}
            
            # Extract fee range from overview
            overview_text = data["fees_and_eligibility"]["overview"]
            import re
            
            # Fee range pattern
            fee_range_match = re.search(r'range between\s*(INR[^.]*?)\s*to\s*(INR[^.]*?)\.', overview_text)
            if fee_range_match:
                stats["fee_range"] = f"{fee_range_match.group(1)} to {fee_range_match.group(2)}"
            
            # Duration range
            duration_match = re.search(r'duration.*?ranges from\s*(\d+[^.]*?)\s*to\s*(\d+[^.]*?)\.', overview_text)
            if duration_match:
                stats["duration_range"] = f"{duration_match.group(1)} to {duration_match.group(2)}"
            
            # Minimum graduation percentage
            grad_match = re.search(r'minimum.*?(\d+)\s*%', overview_text, re.IGNORECASE)
            if grad_match:
                stats["minimum_graduation_percentage"] = f"{grad_match.group(1)}%"
            
            # Accepted exams
            exams_match = re.search(r'scores of\s*([^.]*?)for admission', overview_text)
            if exams_match:
                stats["accepted_exams"] = exams_match.group(1).strip()
            
            data["fees_and_eligibility"]["key_statistics"] = stats
           
            
        except Exception as e:
          
            data["fees_and_eligibility"]["key_statistics"] = {}
        
       
        
    except Exception as e:
       
        import traceback
        traceback.print_exc()
        data["fees_and_eligibility"] = {
            "overview": "Data not available",
            "courses_table": [],
            "faqs": [],
            "key_statistics": {}
        }

    # ================= STUDENT REVIEWS SECTION =================
    try:
      
        reviews_container = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".a2eb03"))
        )
        
        # Scroll to make all reviews visible
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", reviews_container)
        time.sleep(2)
        
        # Initialize data structure
        data["student_reviews"] = {
            "total_reviews_count": 0,
            "average_rating": 0,
            "reviews_list": [],
            "video_reviews": [],
            "review_summary": {}
        }
        
        # 🔹 1. GET ALL REVIEW CARDS
        try:
            # Find all review cards
            review_cards = reviews_container.find_elements(By.CSS_SELECTOR, ".paper-card[id^='review_']")
        
            reviews_data = []
            
            for card in review_cards:
                try:
                    # Skip video reviews section
                    if "review_mini_clips" in card.get_attribute("id"):
                        continue
                    
                    # Extract review ID
                    review_id = card.get_attribute("id").replace("review_", "")
                    
                    # 🔹 BASIC INFO
                    # Student name and batch
                    try:
                        student_name_elem = card.find_element(By.CSS_SELECTOR, ".f1b51a")
                        student_name = student_name_elem.text.strip()
                    except:
                        student_name = "Anonymous"
                    
                    try:
                        batch_info_elem = card.find_element(By.CSS_SELECTOR, ".b7f142")
                        batch_info = batch_info_elem.text.strip()
                    except:
                        batch_info = "Not specified"
                    
                    # Check if verified
                    try:
                        verified_badge = card.find_element(By.CSS_SELECTOR, ".b2e7fe.c3eef6")
                        is_verified = True
                    except:
                        is_verified = False
                    
                    # 🔹 OVERALL RATING
                    try:
                        rating_elem = card.find_element(By.CSS_SELECTOR, ".f05026 span")
                        overall_rating = rating_elem.text.strip()
                    except:
                        overall_rating = "Not rated"
                    
                    # 🔹 CATEGORY RATINGS
                    category_ratings = []
                    try:
                        category_spans = card.find_elements(By.CSS_SELECTOR, ".d757cc")
                        for cat_span in category_spans:
                            cat_text = cat_span.text.strip()
                            if cat_text:
                                # Parse like "5Placements" → {"category": "Placements", "rating": "5"}
                                import re
                                match = re.match(r'(\d+)(.+)', cat_text)
                                if match:
                                    category_ratings.append({
                                        "category": match.group(2).strip(),
                                        "rating": match.group(1).strip()
                                    })
                    except:
                        category_ratings = []
                    
                    # 🔹 REVIEW TITLE
                    try:
                        title_elem = card.find_element(By.CSS_SELECTOR, ".d7e2f2")
                        review_title = title_elem.text.strip()
                    except:
                        review_title = "Review"
                    
                    # 🔹 REVIEW CONTENT (Detailed sections)
                    review_content = {}
                    try:
                        # Get all review sections
                        content_divs = card.find_elements(By.CSS_SELECTOR, ".dca212 div")
                        
                        for div in content_divs:
                            text = div.text.strip()
                            if text:
                                # Split by ": " to get category and content
                                if ": " in text:
                                    parts = text.split(": ", 1)
                                    if len(parts) == 2:
                                        category = parts[0].replace("strong>", "").replace("<", "").strip()
                                        content = parts[1].strip()
                                        review_content[category] = content
                                else:
                                    # If no category, add as general content
                                    review_content["General"] = text
                    except:
                        review_content = {"General": "Content not available"}
                    
                    # 🔹 REVIEW DATE
                    try:
                        date_elem = card.find_element(By.CSS_SELECTOR, ".f3dfa4")
                        review_date = date_elem.text.replace("Reviewed on", "").strip()
                    except:
                        review_date = "Date not available"
                    
                    # 🔹 HELPFUL COUNT
                    helpful_count = 0
                    try:
                        helpful_text = card.find_element(By.CSS_SELECTOR, ".c34bdf span:last-child").text
                        # Extract number from text like "2 people found this helpful"
                        import re
                        helpful_match = re.search(r'(\d+)', helpful_text)
                        if helpful_match:
                            helpful_count = int(helpful_match.group(1))
                    except:
                        helpful_count = 0
                    
                    # 🔹 CHECK FOR PHOTOS
                    has_photos = False
                    photo_urls = []
                    try:
                        photos_section = card.find_element(By.CSS_SELECTOR, ".d77071")
                        photos = photos_section.find_elements(By.TAG_NAME, "img")
                        if photos:
                            has_photos = True
                            for photo in photos[:3]:  # Limit to first 3 photos
                                photo_url = photo.get_attribute("src")
                                if photo_url:
                                    photo_urls.append(photo_url)
                    except:
                        has_photos = False
                    
                    # Compile review data
                    review_data = {
                        "review_id": review_id,
                        "student_name": student_name,
                        "batch_info": batch_info,
                        "is_verified": is_verified,
                        "overall_rating": overall_rating,
                        "category_ratings": category_ratings,
                        "review_title": review_title,
                        "review_content": review_content,
                        "review_date": review_date,
                        "helpful_count": helpful_count,
                        "has_photos": has_photos,
                        "photo_urls": photo_urls if has_photos else []
                    }
                    
                    reviews_data.append(review_data)
                    
                except Exception as e:
                    print(f"Error parsing review card: ")
                    continue
            
            data["student_reviews"]["reviews_list"] = reviews_data
            data["student_reviews"]["total_reviews_count"] = len(reviews_data)
            
            
        except Exception as e:
            
            data["student_reviews"]["reviews_list"] = []
        
        # 🔹 2. VIDEO REVIEWS (Mini Clips)
        try:
            video_reviews = []
            
            # Find video reviews section
            video_section = reviews_container.find_element(By.ID, "review_mini_clips")
            
            # Get all video items
            video_items = video_section.find_elements(By.CSS_SELECTOR, ".d87173")
            
            for video_item in video_items:
                try:
                    # Video title/category
                    category = video_item.get_attribute("data-corouselkeyname") or "Video Review"
                    
                    # Thumbnail image
                    thumbnail_elem = video_item.find_element(By.CSS_SELECTOR, ".f69743")
                    thumbnail_url = thumbnail_elem.get_attribute("src")
                    
                    # Video description
                    try:
                        desc_elem = video_item.find_element(By.CSS_SELECTOR, ".ada2b9")
                        description = desc_elem.text.strip()
                    except:
                        description = f"{category} video"
                    
                    # Check if it's a YouTube embed
                    try:
                        iframe = video_item.find_element(By.TAG_NAME, "iframe")
                        video_url = iframe.get_attribute("src")
                        is_embedded = True
                    except:
                        video_url = None
                        is_embedded = False
                    
                    video_reviews.append({
                        "category": category,
                        "description": description,
                        "thumbnail_url": thumbnail_url,
                        "video_url": video_url,
                        "is_embedded": is_embedded
                    })
                    
                except Exception as e:
                    
                    continue
            
            data["student_reviews"]["video_reviews"] = video_reviews
            
            
        except Exception as e:
        
            data["student_reviews"]["video_reviews"] = []
        
        # 🔹 3. TOTAL REVIEWS COUNT FROM "VIEW ALL" BUTTON
        try:
            # Look for "View All X Reviews" button
            view_all_btn = reviews_container.find_element(By.CSS_SELECTOR, ".ea87ef")
            btn_text = view_all_btn.text.strip()
            
            # Extract number from text like "View All 111 Reviews"
            import re
            count_match = re.search(r'(\d+)', btn_text)
            if count_match:
                total_reviews = int(count_match.group(1))
                data["student_reviews"]["total_reviews_count"] = total_reviews
          
                
        except Exception as e:
            # Use count from extracted reviews if available
            if data["student_reviews"]["total_reviews_count"] == 0:
                data["student_reviews"]["total_reviews_count"] = len(data["student_reviews"]["reviews_list"])
        
        # 🔹 4. CALCULATE AVERAGE RATING AND SUMMARY
        try:
            if data["student_reviews"]["reviews_list"]:
                total_rating = 0
                rating_count = 0
                category_totals = {}
                category_counts = {}
                
                for review in data["student_reviews"]["reviews_list"]:
                    # Overall rating
                    try:
                        rating = float(review["overall_rating"])
                        total_rating += rating
                        rating_count += 1
                    except:
                        pass
                    
                    # Category ratings
                    for cat_rating in review.get("category_ratings", []):
                        category = cat_rating["category"]
                        rating = cat_rating["rating"]
                        
                        try:
                            rating_val = float(rating)
                            if category not in category_totals:
                                category_totals[category] = 0
                                category_counts[category] = 0
                            
                            category_totals[category] += rating_val
                            category_counts[category] += 1
                        except:
                            pass
                
                # Calculate averages
                if rating_count > 0:
                    data["student_reviews"]["average_rating"] = round(total_rating / rating_count, 1)
                
                # Calculate category averages
                category_averages = {}
                for category in category_totals:
                    if category_counts[category] > 0:
                        category_averages[category] = round(category_totals[category] / category_counts[category], 1)
                
                # Create summary
                data["student_reviews"]["review_summary"] = {
                    "average_overall_rating": data["student_reviews"]["average_rating"],
                    "total_reviews_analyzed": rating_count,
                    "category_averages": category_averages,
                    "verified_reviews_count": sum(1 for r in data["student_reviews"]["reviews_list"] if r["is_verified"]),
                    "reviews_with_photos": sum(1 for r in data["student_reviews"]["reviews_list"] if r["has_photos"])
                }
                
                print(f"✓ Calculated average rating: {data['student_reviews']['average_rating']}")
                
        except Exception as e:
            
            data["student_reviews"]["review_summary"] = {}
        
      
        
    except Exception as e:
        
        import traceback
        traceback.print_exc()
        
        data["student_reviews"] = {
            "total_reviews_count": 0,
            "average_rating": 0,
            "reviews_list": [],
            "video_reviews": [],
            "review_summary": {}
        }


    return data 
def clean_text(text):
    remove_words = [
        "Upvote",
        "Not satisfied with answer?",
        "Ask Shiksha GPT",
        "Get Placement Report",
        "Get Admission Info"
    ]
    for w in remove_words:
        text = text.replace(w, "")
    return re.sub(r'\n+', '\n', text).strip()

def scrape_courses(driver, URLS):
    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
    }
    try:
        driver.get(URLS["courses"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["courses"])
    
    wait = WebDriverWait(driver, 20)
    
    # Wait for page to load completely
    time.sleep(2)
    
    # ---------- LOGO AND HEADER INFO ----------
    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image
        try:
            top_header_section = driver.find_element(By.ID, "topHeaderCard-top-section")
            cover_img = top_header_section.find_element(By.ID, "topHeaderCard-gallery-image")
            college_info["cover_image"] = cover_img.get_attribute("src")
           
        except:
            pass
        
        # Extract logo
        try:
            logo_div = driver.find_element(By.CSS_SELECTOR, ".ca46d2.e014b3")
            logo_img = logo_div.find_element(By.TAG_NAME, "img")
            college_info["logo"] = logo_img.get_attribute("src")
            pass
        except:
           pass
        
        # Extract videos and photos count
        try:
            badges_div = driver.find_element(By.CSS_SELECTOR, ".e4df0b.ad160e")
            badges = badges_div.find_elements(By.CSS_SELECTOR, ".dcd631")
            
            for badge in badges:
                text = badge.text.lower()
                if "video" in text:
                    videos_match = re.search(r'(\d+)\s*videos?', text)
                    if videos_match:
                        college_info["videos_count"] = int(videos_match.group(1))
                elif "photo" in text:
                    photos_match = re.search(r'(\d+)\s*photos?', text)
                    if photos_match:
                        college_info["photos_count"] = int(photos_match.group(1))
        except:
            pass
        
        # Rest of your existing header extraction code...
        
    except Exception as e:
        print("⚠️ Error in college header section:")
    
    # ---------- COLLEGE NAME ----------
    try:
        name_elem = driver.find_element(By.CSS_SELECTOR, ".cc5e8d")
        college_info["college_name"] = name_elem.text.strip()
    except Exception as e:
        pass
    
    # ---------- LOCATION ----------
    try:
        location_elem = driver.find_element(By.CSS_SELECTOR, ".f90eb6.a73e41")
        location_text = location_elem.text.strip()
        if "," in location_text:
            location_parts = location_text.split(",")
            college_info["location"] = location_parts[0].strip()
            college_info["city"] = location_parts[1].strip() if len(location_parts) > 1 else ""
        else:
            college_info["location"] = location_text
    except Exception as e:
        print("Location error:")
    
    # ---------- RATING AND REVIEWS ----------
    try:
        # Rating
        rating_elem = driver.find_element(By.CSS_SELECTOR, ".f1b26c")
        rating_text = rating_elem.text.strip()
        if "/" in rating_text:
            rating_parts = rating_text.split("/")
            college_info["rating"] = rating_parts[0].strip()
    except Exception as e:
        print("Rating error:")
    
    try:
        # Reviews count
        reviews_elem = driver.find_element(By.CSS_SELECTOR, 'a[href*="reviews"]')
        reviews_text = reviews_elem.text.strip()
        reviews_match = re.search(r'\((\d+)\s*Reviews\)', reviews_text)
        if reviews_match:
            college_info["reviews_count"] = int(reviews_match.group(1))
    except Exception as e:
        print("Reviews error")
    
    # ---------- Q&A COUNT ----------
    try:
        qa_elem = driver.find_element(By.CSS_SELECTOR, 'a[href*="questions"]')
        qa_text = qa_elem.text.strip()
        qa_match = re.search(r'([\d.]+k?)', qa_text)
        if qa_match:
            qa_value = qa_match.group(1)
            if 'k' in qa_value.lower():
                college_info["qa_count"] = int(float(qa_value.lower().replace('k', '')) * 1000)
            else:
                college_info["qa_count"] = int(qa_value)
    except Exception as e:
        print("Q&A error:")
    
    # ---------- INSTITUTE TYPE AND ESTABLISHED YEAR ----------
    try:
        list_items = driver.find_elements(By.CSS_SELECTOR, ".ff9e36 li .f1b26c .b00d1d")
        for item in list_items:
            text = item.text.strip().lower()
            if "institute" in text or "public" in text or "government" in text:
                college_info["institute_type"] = item.text.strip()
            elif "estd" in text or "est." in text:
                year_match = re.search(r'\d{4}', item.text)
                if year_match:
                    college_info["established_year"] = int(year_match.group())
    except Exception as e:
        print("Institute info error")
    
    # ---------- FEE STRUCTURE HEADING AND OVERVIEW ----------
    fee_heading = ""
    fee_overview = ""
    
    try:
        # Try to find fee structure heading
        fee_heading_elems = driver.find_elements(By.CSS_SELECTOR, ".ab2e01 .ae88c4, .c5d378 .ae88c4, .h2 .ae88c4")
        for elem in fee_heading_elems:
            text = elem.text.strip()
            if "Fee Structure" in text or "fee" in text.lower():
                fee_heading = text
                break
        
        # Try to find fee structure overview/description
        overview_elems = driver.find_elements(By.CSS_SELECTOR, ".wikiContents p, .faq__according-wrapper p, .dfbe34 p")
        for elem in overview_elems:
            text = elem.text.strip()
            if text and len(text) > 50:
                # Check if it's related to fees
                if "fee" in text.lower() or "payment" in text.lower() or "tuition" in text.lower():
                    fee_overview = text
                    break
        
     
        
    except Exception as e:
        print("Fee heading/overview error:")
    
    # ---------- FEE STRUCTURE TABLE DATA (IMPROVED WITH CLEANING) ----------
    fee_structure = []
    
    try:
        # Try to find fee structure section using multiple selectors
        fee_sections = driver.find_elements(By.CSS_SELECTOR, "#acp_section_fees, [id*='fee'], .paper-card")
        
        for fee_section in fee_sections:
            try:
                section_text = fee_section.text.lower()
                if "fee" in section_text or "tuition" in section_text:
                  
                    
                    # Extract fee structure table
                    try:
                        fee_tables = fee_section.find_elements(By.TAG_NAME, "table")
                        for table in enumerate(fee_tables):
                            
                            
                            # Get all rows
                            rows = table.find_elements(By.TAG_NAME, "tr")
                            if not rows:
                                continue
                            
                            # Extract table headers
                            headers = []
                            header_cells = rows[0].find_elements(By.TAG_NAME, "th")
                            
                            for cell in header_cells:
                                try:
                                    # Try to get text from font tag first
                                    font_tag = cell.find_element(By.TAG_NAME, "font")
                                    header_text = font_tag.text.strip()
                                except:
                                    header_text = cell.text.strip()
                                
                                if header_text:
                                    headers.append(header_text)
                            
                            # If no headers found in th, try first row as headers
                            if not headers and rows:
                                first_row_cells = rows[0].find_elements(By.TAG_NAME, "td")
                                if first_row_cells:
                                    for cell in first_row_cells:
                                        headers.append(cell.text.strip())
                                    # Skip first row as it's now headers
                                    rows = rows[1:]
                            
                         
                            
                            # Extract table rows
                            for row_idx, row in enumerate(rows):
                                try:
                                    cells = row.find_elements(By.TAG_NAME, "td")
                                    if not cells:
                                        continue
                                    
                                    fee_item = {}
                                    is_empty_row = True
                                    
                                    for idx, cell in enumerate(cells):
                                        if idx >= len(headers):
                                            continue
                                            
                                        cell_text = cell.text.strip()
                                        if cell_text:
                                            is_empty_row = False
                                        
                                        # Get header name (clean it)
                                        header_name = headers[idx].lower().replace(" ", "_").replace("-", "_")
                                        if header_name == "":
                                            header_name = f"column_{idx}"
                                        
                                        # Clean the cell text - remove newlines and extra spaces
                                        cleaned_text = re.sub(r'\s*\n\s*', ' ', cell_text)  # Replace newlines with space
                                        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Remove extra spaces
                                        
                                        # Check if cell contains link
                                        try:
                                            link = cell.find_element(By.TAG_NAME, "a")
                                            link_href = link.get_attribute("href")
                                            link_text = link.text.strip()
                                            cleaned_link_text = re.sub(r'\s*\n\s*', ' ', link_text)
                                            cleaned_link_text = re.sub(r'\s+', ' ', cleaned_link_text).strip()
                                            
                                            # If cell has both text and link
                                            if cleaned_text and cleaned_text != cleaned_link_text:
                                                fee_item[header_name] = {
                                                    "text": cleaned_text,
                                                    "link": link_href if link_href else None
                                                }
                                            else:
                                                # If only link text
                                                fee_item[header_name] = {
                                                    "text": cleaned_link_text,
                                                    "link": link_href if link_href else None
                                                }
                                        except:
                                            # No link found, just store cleaned text
                                            if cleaned_text:
                                                fee_item[header_name] = cleaned_text
                                    
                                    # Skip empty rows
                                    if is_empty_row:
                                        continue
                                    
                                    # Also check for any main course links in the row
                                    try:
                                        main_links = row.find_elements(By.CSS_SELECTOR, "a[href*='courses']")
                                        if main_links:
                                            fee_item["course_link"] = main_links[0].get_attribute("href")
                                    except:
                                        pass
                                    
                                    if fee_item:
                                        # Additional cleaning of the fee item
                                        cleaned_fee_item = {}
                                        for key, value in fee_item.items():
                                            if isinstance(value, dict):
                                                # Clean text in dictionary values
                                                cleaned_value = value.copy()
                                                if "text" in cleaned_value:
                                                    cleaned_value["text"] = re.sub(r'\s*\n\s*', ' ', cleaned_value["text"])
                                                    cleaned_value["text"] = re.sub(r'\s+', ' ', cleaned_value["text"]).strip()
                                                cleaned_fee_item[key] = cleaned_value
                                            elif isinstance(value, str):
                                                # Clean string values
                                                cleaned_text = re.sub(r'\s*\n\s*', ' ', value)
                                                cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
                                                cleaned_fee_item[key] = cleaned_text
                                            else:
                                                cleaned_fee_item[key] = value
                                        
                                        fee_structure.append(cleaned_fee_item)
                                       
                                    
                                except Exception as e:
                                   
                                    continue
                    
                    except Exception as e:
                        print("Error extracting fee table:")
                    
                    break  # Stop after first valid fee section
                    
            except Exception as e:
                print("Error processing fee section:")
                continue
        
        # Clean empty items from fee_structure
        fee_structure = [item for item in fee_structure if item and not all(value == "" or value == {} for value in item.values())]
        
        # If we have fee structure but headers are generic, rename them
        if fee_structure:
            # Check if we need to rename keys
            first_item = fee_structure[0]
            keys_to_rename = {}
            
            for key in first_item.keys():
                if key.startswith("column_") or key == "":
                    # Try to determine what this column represents
                    if "course" in str(first_item.get(key, "")).lower():
                        keys_to_rename[key] = "course_name"
                    elif "fee" in str(first_item.get(key, "")).lower() or "l" in str(first_item.get(key, "")) or "inr" in str(first_item.get(key, "")).lower():
                        keys_to_rename[key] = "tuition_fee"
                    elif "eligibility" in str(first_item.get(key, "")).lower() or "graduation" in str(first_item.get(key, "")).lower():
                        keys_to_rename[key] = "eligibility"
                    elif "one_time" in str(first_item.get(key, "")).lower():
                        keys_to_rename[key] = "one_time_fee"
                    elif "hostel" in str(first_item.get(key, "")).lower():
                        keys_to_rename[key] = "hostel_fee"
            
            # Rename keys in all items
            if keys_to_rename:
                for item in fee_structure:
                    for old_key, new_key in keys_to_rename.items():
                        if old_key in item:
                            item[new_key] = item.pop(old_key)
        

        
    except Exception as e:
        print("Fee structure error:")
    
    # ---------- COURSES OVERVIEW TEXT ----------
    overview_text = ""
    try:
        # Look for the overview section with heading
        overview_section = driver.find_element(By.ID, "acp_section_fees_and_eligibility")
        
        # Get the heading
        try:
            heading_elem = overview_section.find_element(By.CSS_SELECTOR, ".ae88c4")
            overview_text = heading_elem.text.strip() + "\n\n"
        except:
            pass
        
        # Get the overview paragraph text
        try:
            overview_para = overview_section.find_element(By.CSS_SELECTOR, ".faq__according-wrapper p")
            overview_text += overview_para.text.strip()
        except:
            # Try alternative selector
            try:
                wiki_content = overview_section.find_element(By.CSS_SELECTOR, ".wikiContents")
                overview_text += wiki_content.text.split("Read more")[0].strip()
            except:
                pass
        
        # Clean overview text
        if overview_text:
            overview_text = re.sub(r'\s*\n\s*', ' ', overview_text)
            overview_text = re.sub(r'\s+', ' ', overview_text).strip()
        
        
    except Exception as e:
        print("Courses overview error")
    
    # ---------- COURSES TABLE DATA ----------
    courses = []
    
    try:
        # Wait for courses table
        table = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table.table.a82bdd"))
        )
        
        # Get all rows from table body
        rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
        
        for row in rows:
            try:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 3:
                    # Course name and count
                    course_cell = cells[0]
                    try:
                        course_link = course_cell.find_element(By.TAG_NAME, "a")
                        course_name = course_link.text.strip()
                    except:
                        course_name = course_cell.text.strip()
                    
                    # Clean course name
                    course_name = re.sub(r'\s*\n\s*', ' ', course_name)
                    course_name = re.sub(r'\s+', ' ', course_name).strip()
                    
                    # Extract course count if available
                    course_count = None
                    try:
                        count_span = course_cell.find_element(By.CLASS_NAME, "d94f03")
                        count_text = count_span.text.strip()
                        count_match = re.search(r'\((\d+)\s*course', count_text)
                        if count_match:
                            course_count = int(count_match.group(1))
                    except:
                        pass
                    
                    # Tuition fees
                    fees_cell = cells[1]
                    fees_text = fees_cell.text.strip()
                    # Remove "Get Fee Details" text and clean
                    fees_clean = fees_text.replace("Get Fee Details", "").strip()
                    fees_clean = re.sub(r'\s*\n\s*', ' ', fees_clean)
                    fees_clean = re.sub(r'\s+', ' ', fees_clean).strip()
                    
                    # Eligibility
                    eligibility_cell = cells[2]
                    eligibility_text = eligibility_cell.text.strip()
                    eligibility_text = re.sub(r'\s*\n\s*', ' ', eligibility_text)
                    eligibility_text = re.sub(r'\s+', ' ', eligibility_text).strip()
                    
                    # Extract detailed eligibility information
                    eligibility_data = {}
                    
                    # Check for graduation percentage
                    if "Graduation" in eligibility_text:
                        grad_match = re.search(r'Graduation.*?(\d+)\s*%', eligibility_text)
                        if grad_match:
                            eligibility_data["graduation_percentage"] = f"{grad_match.group(1)}%"
                    
                    # Extract exams
                    exams = []
                    try:
                        exam_links = eligibility_cell.find_elements(By.TAG_NAME, "a")
                        for exam_link in exam_links:
                            exam_name = exam_link.text.strip()
                            exam_name = re.sub(r'\s*\n\s*', ' ', exam_name)
                            exam_name = re.sub(r'\s+', ' ', exam_name).strip()
                            if exam_name and exam_name not in ["+2 More", "+1 More", "More"]:
                                exams.append(exam_name)
                    except:
                        pass
                    
                    if exams:
                        eligibility_data["exams"] = exams
                    
                    # If no structured data found, store the raw text
                    if not eligibility_data and eligibility_text and eligibility_text != "– / –":
                        eligibility_data = eligibility_text
                    elif eligibility_text == "– / –":
                        eligibility_data = "Not specified"
                    
                    # Create course object
                    course_obj = {
                        "course_name": course_name,
                        "course_count": course_count,
                        "fees": fees_clean,
                        "eligibility": eligibility_data
                    }
                    
                    # Add course link if available
                    try:
                        course_link = course_cell.find_element(By.TAG_NAME, "a")
                        course_obj["link"] = course_link.get_attribute("href")
                    except:
                        pass
                    
                    courses.append(course_obj)
                    
            except Exception as e:
            
                continue
        
 
        
    except Exception as e:
        print("Error extracting courses table:")
        courses = []
    
    # ---------- FAQS DATA - IMPROVED CLEANING ----------
    faqs = []
    
    try:
        # First, check if FAQ section exists and is visible
        faq_section = driver.find_element(By.CSS_SELECTOR, ".sectional-faqs")
        
        # Scroll to FAQ section to ensure it's in view
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", faq_section)
        time.sleep(1)
        
        # Use JavaScript to extract FAQs with better cleaning
        faqs_data = driver.execute_script("""
            const faqs = [];
            const faqSection = document.querySelector('.sectional-faqs');
            
            if (faqSection) {
                // Get all question elements
                const questionElements = faqSection.querySelectorAll('.ea1844');
                
                questionElements.forEach((qElem, index) => {
                    try {
                        // Extract question
                        let question = '';
                        
                        // Try multiple ways to get question
                        const qSpans = qElem.querySelectorAll('.flx-box span');
                        if (qSpans.length >= 3) {
                            question = qSpans[2].textContent.trim();
                        } else {
                            // Fallback: get all text and remove Q:
                            question = qElem.textContent.replace(/^Q:?\s*/i, '').trim();
                        }
                        
                        // Clean question text
                        question = question.replace(/\\s*\\n\\s*/g, ' ').replace(/\\s+/g, ' ').trim();
                        
                        if (question) {
                            // Find corresponding answer
                            let answer = '';
                            let nextElem = qElem.nextElementSibling;
                            
                            // Look for answer in next sibling elements
                            while (nextElem) {
                                if (nextElem.classList && nextElem.classList.contains('f61835')) {
                                    const answerDiv = nextElem.querySelector('.wikkiContents');
                                    if (answerDiv) {
                                        answer = answerDiv.textContent.trim();
                                        
                                        // Clean up answer text more aggressively
                                        answer = answer
                                            .replace(/Not satisfied with answer.*/gi, '')
                                            .replace(/Ask Shiksha GPT.*/gi, '')
                                            .replace(/\\s*\\n\\s*/g, ' ')  // Replace newlines with space
                                            .replace(/\\s+/g, ' ')  // Replace multiple spaces with single space
                                            .replace(/^A:\\s*/, '')  // Remove starting "A:"
                                            .replace(/^A&nbsp;\\s*/, '')  // Remove starting "A&nbsp;"
                                            .trim();
                                    }
                                    break;
                                }
                                nextElem = nextElem.nextElementSibling;
                            }
                            
                            if (question && answer) {
                                faqs.push({
                                    question: question,
                                    answer: answer.substring(0, 2000) // Limit length
                                });
                            }
                        }
                    } catch (e) {
                        console.log('Error parsing FAQ:', e);
                    }
                });
            }
            
            return faqs;
        """)
        
        if faqs_data:
            faqs = faqs_data
           
        else:
            # Fallback to Python method

            try:
                # Get all question elements
                question_elements = faq_section.find_elements(By.CSS_SELECTOR, ".ea1844")
                
                for i, q_elem in enumerate(question_elements):
                    try:
                        # Extract question
                        question = ""
                        try:
                            q_spans = q_elem.find_elements(By.CSS_SELECTOR, ".flx-box span")
                            if len(q_spans) >= 3:
                                question = q_spans[2].text.strip()
                            else:
                                question = q_elem.text.replace("Q:", "").replace("Q :", "").strip()
                        except:
                            question = q_elem.text.replace("Q:", "").strip()
                        
                        # Clean question
                        question = re.sub(r'\s*\n\s*', ' ', question)
                        question = re.sub(r'\s+', ' ', question).strip()
                        
                        # Find answer
                        answer = ""
                        try:
                            answer_elem = driver.execute_script("""
                                var elem = arguments[0];
                                var next = elem.nextElementSibling;
                                while (next) {
                                    if (next.classList.contains('f61835')) {
                                        return next;
                                    }
                                    next = next.nextElementSibling;
                                }
                                return null;
                            """, q_elem)
                            
                            if answer_elem:
                                answer_div = answer_elem.find_element(By.CSS_SELECTOR, ".wikkiContents")
                                answer_text = answer_div.text.strip()
                                
                                # Clean answer text
                                answer_text = re.sub(r'Not satisfied with answer.*', '', answer_text, flags=re.IGNORECASE)
                                answer_text = re.sub(r'Ask Shiksha GPT.*', '', answer_text, flags=re.IGNORECASE)
                                answer_text = re.sub(r'^\s*A:?\s*', '', answer_text)  # Remove starting "A:"
                                answer_text = re.sub(r'^\s*A&nbsp;\s*', '', answer_text)  # Remove starting "A&nbsp;"
                                answer_text = re.sub(r'\s*\n\s*', ' ', answer_text)  # Replace newlines with space
                                answer_text = re.sub(r'\s+', ' ', answer_text).strip()  # Normalize whitespace
                                
                                answer = answer_text
                        except:
                            pass
                        
                        if question and answer:
                            faqs.append({
                                "question": question,
                                "answer": answer[:1500] + "..." if len(answer) > 1500 else answer
                            })
                            
                    except Exception as e:
                
                        continue
                
           
                
            except Exception as e:
                print("Python FAQ extraction also failed:")
                faqs = []
        
        # Additional cleaning of FAQ answers
        for faq in faqs:
            faq["question"] = re.sub(r'\s+', ' ', faq["question"]).strip()
            faq["answer"] = re.sub(r'\s+', ' ', faq["answer"]).strip()
        
    except Exception as e:
        print("FAQ section error:")
        faqs = []
    
    # Create final response structure with organized fee structure
    result = {
        "college_info": college_info,
        "overview": overview_text,
        "courses": courses,
        "fee_structure": {
            "heading": fee_heading,
            "overview": fee_overview,
            "data": fee_structure  # Clean data only
        },
        "faqs": faqs
    }

    all_data = scrape_all_programs_and_courses(driver)
    faqs_section_data = scrape_faqs_section(driver)
    result.update(all_data)
    result.update(faqs_section_data)
    return result

def scrape_all_programs_and_courses(driver):

    all_programs_data = []
    all_courses_data = []
    
    # Wait for page to load completely
    time.sleep(2)
    

    
    # ---------- ALL PROGRAMS DATA ----------
    try:
       
        # Find all program tuples
        program_tuples = driver.find_elements(By.CSS_SELECTOR, ".acp_base_course_tuple .d15c8a.fb6321.a25c93")
        
        for program_tuple in program_tuples:
            try:
                program_data = {}
                
                # Extract program name
                try:
                    program_name_elem = program_tuple.find_element(By.CSS_SELECTOR, ".c42a97 .f443c7")
                    program_data["program_name"] = program_name_elem.text.strip()
                except:
                    program_data["program_name"] = "N/A"
                
                # Extract program details
                try:
                    details_elem = program_tuple.find_element(By.CSS_SELECTOR, ".ae8f7e")
                    details_text = details_elem.text.strip()
                    
                    # Parse course count
                    course_count_match = re.search(r'(\d+)\s*Course', details_text)
                    if course_count_match:
                        program_data["course_count"] = int(course_count_match.group(1))
                    
                    # Parse duration
                    duration_match = re.search(r'(\d+\s*(?:months?|years?|\s*-\s*\d+\s*(?:months?|years?)))', details_text)
                    if duration_match:
                        program_data["duration"] = duration_match.group(1).strip()
                    
                    # Parse rating
                    rating_match = re.search(r'(\d+\.\d+)', details_text)
                    if rating_match:
                        program_data["rating"] = float(rating_match.group(1))
                    
                    # Parse reviews count
                    reviews_match = re.search(r'\((\d+)\)', details_text)
                    if reviews_match:
                        program_data["reviews_count"] = int(reviews_match.group(1))
                    
                    # Parse ranking
                    ranking_match = re.search(r'#(\d+)\s+(\w+)', details_text)
                    if ranking_match:
                        program_data["ranking"] = {
                            "rank": ranking_match.group(1),
                            "source": ranking_match.group(2)
                        }
                        
                except Exception as e:
                    print("Error extracting program details:")
                
                # Extract exams accepted
                try:
                    exams_elem = program_tuple.find_element(By.CSS_SELECTOR, ".b93ff8:nth-child(1) .c8c9ee")
                    exams_text = exams_elem.text.strip()
                    if exams_text and exams_text != "– / –":
                        # Check if there's a list of exams
                        exam_links = exams_elem.find_elements(By.TAG_NAME, "a")
                        if exam_links:
                            program_data["exams_accepted"] = [link.text.strip() for link in exam_links if link.text.strip()]
                        else:
                            program_data["exams_accepted"] = exams_text
                    else:
                        program_data["exams_accepted"] = "Not specified"
                except:
                    program_data["exams_accepted"] = "Not specified"
                
                # Extract median salary
                try:
                    salary_elem = program_tuple.find_element(By.CSS_SELECTOR, ".b93ff8:nth-child(2) .c8c9ee")
                    salary_text = salary_elem.text.strip()
                    if salary_text and salary_text != "– / –":
                        program_data["median_salary"] = salary_text
                    else:
                        program_data["median_salary"] = "Not available"
                except:
                    program_data["median_salary"] = "Not available"
                
                # Extract total tuition fees
                try:
                    fees_elem = program_tuple.find_element(By.CSS_SELECTOR, ".b93ff8:nth-child(3) .c8c9ee")
                    fees_text = fees_elem.text.strip()
                    # Clean fees text
                    if fees_text and fees_text != "– / –":
                        fees_clean = re.sub(r'Get Fee Details.*', '', fees_text).strip()
                        program_data["total_tuition_fees"] = fees_clean
                    else:
                        program_data["total_tuition_fees"] = "Not available"
                except:
                    program_data["total_tuition_fees"] = "Not available"
                
                # Extract program link
                try:
                    program_link_elem = program_tuple.find_element(By.CSS_SELECTOR, ".c42a97 a")
                    program_data["program_link"] = program_link_elem.get_attribute("href")
                except:
                    program_data["program_link"] = None
                
                all_programs_data.append(program_data)
                
            except Exception as e:
                
                continue
        
       
        
    except Exception as e:
        print("Error extracting all programs: ")
    
    # ---------- ALL COURSES DATA ----------
    try:
        print("\nExtracting 'All Courses' data...")
        
        # Find all course tuples
        course_tuples = driver.find_elements(By.CSS_SELECTOR, ".acp_course_tuple .d15c8a.fb6321.a25c93")
        
        for course_tuple in course_tuples:
            try:
                course_data = {}
                
                # Extract course name
                try:
                    course_name_elem = course_tuple.find_element(By.CSS_SELECTOR, ".c42a97 .f443c7")
                    course_data["course_name"] = course_name_elem.text.strip()
                except:
                    course_data["course_name"] = "N/A"
                
                # Extract course details
                try:
                    details_elem = course_tuple.find_element(By.CSS_SELECTOR, ".ae8f7e")
                    details_text = details_elem.text.strip()
                    
                    # Parse rating
                    rating_match = re.search(r'(\d+\.\d+)', details_text)
                    if rating_match:
                        course_data["rating"] = float(rating_match.group(1))
                    
                    # Parse duration
                    duration_match = re.search(r'(\d+\s*(?:days?|months?|years?|\s*-\s*\d+\s*(?:days?|months?|years?)))', details_text)
                    if duration_match:
                        course_data["duration"] = duration_match.group(1).strip()
                    
                    # Parse ranking
                    ranking_match = re.search(r'#(\d+)\s+(\w+)', details_text)
                    if ranking_match:
                        course_data["ranking"] = {
                            "rank": ranking_match.group(1),
                            "source": ranking_match.group(2)
                        }
                    
                    # Check for degree type
                    if "Diploma" in details_text:
                        course_data["degree_type"] = "Diploma"
                    elif "Certificate" in details_text:
                        course_data["degree_type"] = "Certificate"
                    elif "Degree" in details_text:
                        course_data["degree_type"] = "Degree"
                        
                except Exception as e:
                    print("Error extracting course details:")
                
                # Extract seats offered
                try:
                    seats_elem = course_tuple.find_element(By.CSS_SELECTOR, ".b93ff8:nth-child(1) .c8c9ee")
                    seats_text = seats_elem.text.strip()
                    if seats_text and seats_text != "– / –":
                        # Try to parse as number
                        try:
                            course_data["seats_offered"] = int(seats_text)
                        except:
                            course_data["seats_offered"] = seats_text
                    else:
                        course_data["seats_offered"] = "Not specified"
                except:
                    course_data["seats_offered"] = "Not specified"
                
                # Extract exams accepted
                try:
                    exams_elem = course_tuple.find_element(By.CSS_SELECTOR, ".b93ff8:nth-child(2) .c8c9ee")
                    exams_text = exams_elem.text.strip()
                    if exams_text and exams_text != "– / –":
                        # Check if there's a list of exams
                        exam_links = exams_elem.find_elements(By.TAG_NAME, "a")
                        if exam_links:
                            course_data["exams_accepted"] = [link.text.strip() for link in exam_links if link.text.strip()]
                        else:
                            course_data["exams_accepted"] = exams_text
                    else:
                        course_data["exams_accepted"] = "Not specified"
                except:
                    course_data["exams_accepted"] = "Not specified"
                
                # Extract median salary
                try:
                    salary_elem = course_tuple.find_element(By.CSS_SELECTOR, ".b93ff8:nth-child(3) .c8c9ee")
                    salary_text = salary_elem.text.strip()
                    if salary_text and salary_text != "– / –":
                        course_data["median_salary"] = salary_text
                    else:
                        course_data["median_salary"] = "Not available"
                except:
                    course_data["median_salary"] = "Not available"
                
                # Extract total tuition fees
                try:
                    fees_elem = course_tuple.find_element(By.CSS_SELECTOR, ".b93ff8:nth-child(4) .c8c9ee")
                    fees_text = fees_elem.text.strip()
                    # Clean fees text
                    if fees_text and fees_text != "– / –":
                        fees_clean = re.sub(r'Get Fee Details.*', '', fees_text).strip()
                        course_data["total_tuition_fees"] = fees_clean
                    else:
                        course_data["total_tuition_fees"] = "Not available"
                except:
                    course_data["total_tuition_fees"] = "Not available"
                
                # For online/blended courses, check for different structure
                if "e8c4fd" in course_tuple.get_attribute("class"):
                    try:
                        # Try to extract total fees for online courses
                        total_fees_elem = course_tuple.find_element(By.CSS_SELECTOR, ".b93ff8:nth-child(1) .c8c9ee")
                        total_fees = total_fees_elem.text.strip()
                        if total_fees and total_fees != "– / –":
                            course_data["total_fees"] = total_fees
                    except:
                        pass
                    
                    try:
                        # Try to extract duration
                        duration_elem = course_tuple.find_element(By.CSS_SELECTOR, ".b93ff8:nth-child(2) .c8c9ee")
                        duration = duration_elem.text.strip()
                        if duration and duration != "– / –":
                            course_data["duration"] = duration
                    except:
                        pass
                    
                    try:
                        # Try to extract skills
                        skills_elem = course_tuple.find_elements(By.CSS_SELECTOR, ".d000d4 .a68029 a")
                        if skills_elem:
                            course_data["skills"] = [skill.text.strip() for skill in skills_elem if skill.text.strip()]
                    except:
                        pass
                
                # Extract course link
                try:
                    course_link_elem = course_tuple.find_element(By.CSS_SELECTOR, ".c42a97 a")
                    course_data["course_link"] = course_link_elem.get_attribute("href")
                except:
                    course_data["course_link"] = None
                
                all_courses_data.append(course_data)
                
            except Exception as e:
                print("Error processing course tuple:")
                continue
       
        
    except Exception as e:
        print("Error extracting all courses:")
    
    # Create final result structure
    result = {
        "all_programs": all_programs_data,
        "all_courses": all_courses_data
    }
    
    return result

def scrape_faqs_section(driver):

    faqs_data = []
    
 
    try:
        # Wait for FAQ section to load
        wait = WebDriverWait(driver, 15)
        
        # Wait for FAQ section to be present - try multiple selectors
        faq_section = None
        section_selectors = [
            (By.ID, "acp_section_fAQs"),
            (By.CSS_SELECTOR, "[data-section-id='fAQs']"),
            (By.CSS_SELECTOR, ".faq__according-wrapper"),
            (By.XPATH, "//*[contains(text(), 'FAQs')]")
        ]
        
        for selector_type, selector in section_selectors:
            try:
                faq_section = wait.until(
                    EC.presence_of_element_located((selector_type, selector))
                )
             
                break
            except:
                continue
        
        if not faq_section:
            return {"faq_section": None}
        
        # Extract section heading
        section_heading = ""
        try:
            heading_selectors = [
                ".ae88c4",
                "h2",
                "h3",
                ".section-heading",
                "[class*='heading']"
            ]
            for selector in heading_selectors:
                try:
                    heading_elem = faq_section.find_element(By.CSS_SELECTOR, selector)
                    if heading_elem.text.strip():
                        section_heading = heading_elem.text.strip()
                        break
                except:
                    continue
        except:
            pass
        

        # Extract introduction text
        intro_text = ""
        try:
            intro_selectors = [
                ".faq__according-wrapper p",
                "p",
                ".intro-text",
                "[class*='description']",
                "[class*='intro']"
            ]
            for selector in intro_selectors:
                try:
                    intro_elem = faq_section.find_element(By.CSS_SELECTOR, selector)
                    text = intro_elem.text.strip()
                    if text and len(text) > 10:  # Avoid short/irrelevant text
                        intro_text = text
                        break
                except:
                    continue
        except:
            pass
        
        
        time.sleep(3)  # Wait for JavaScript to load content
        
       
        js_faqs = driver.execute_script("""
            const faqs = [];
            
            // Find FAQ section - try multiple selectors
            let faqSection = document.querySelector('#acp_section_fAQs');
            if (!faqSection) {
                faqSection = document.querySelector('[data-section-id="fAQs"]');
            }
            if (!faqSection) {
                // Look for any element containing FAQs
                const elements = document.querySelectorAll('*');
                for (const elem of elements) {
                    if (elem.textContent.includes('FAQ') && 
                        elem.textContent.includes('Q:')) {
                        faqSection = elem;
                        break;
                    }
                }
            }
            
            if (!faqSection) {
                console.log('FAQ section not found');
                return faqs;
            }
            
            console.log('FAQ section found:', faqSection);
            
            // Find all question elements - multiple class patterns
            const questionSelectors = [
                '.html-0.ea1844.listener',
                '.ea1844',
                '.listener',
                '[class*="faq"] .question',
                '[class*="accordion"] .question',
                '[class*="accordion__item"]',
                '.flx-box'
            ];
            
            let questionElements = [];
            for (const selector of questionSelectors) {
                const elements = faqSection.querySelectorAll(selector);
                if (elements.length > 0) {
                    console.log(`Found ${elements.length} elements with selector: ${selector}`);
                    questionElements = Array.from(elements);
                    break;
                }
            }
            
            // If no elements found, try a broader search
            if (questionElements.length === 0) {
                console.log('No specific question elements found, trying broader search...');
                const allElements = faqSection.querySelectorAll('*');
                questionElements = Array.from(allElements).filter(el => {
                    const text = el.textContent.trim();
                    return text.startsWith('Q:') || 
                           text.startsWith('Q ') ||
                           (el.classList && 
                            (el.classList.contains('html-0') || 
                             el.classList.contains('listener')));
                });
            }
            
            console.log(`Found ${questionElements.length} question elements`);
            
            questionElements.forEach((qElem, index) => {
                try {
                    // Extract question
                    let question = '';
                    const fullText = qElem.textContent.trim();
                    
                    // Clean question extraction
                    if (fullText.startsWith('Q:')) {
                        question = fullText.substring(2).trim();
                    } else if (fullText.startsWith('Q ')) {
                        question = fullText.substring(1).trim();
                    } else {
                        // Try to find question in spans
                        const questionSpans = qElem.querySelectorAll('span');
                        if (questionSpans.length > 0) {
                            // Get the last span (usually contains the question)
                            const lastSpan = questionSpans[questionSpans.length - 1];
                            question = lastSpan.textContent.trim();
                        } else {
                            question = fullText;
                        }
                    }
                    
                    // Clean question text
                    question = question.replace(/\\s*\\n\\s*/g, ' ').replace(/\\s+/g, ' ').trim();
                    
                    if (!question || question.length < 5) {
                        console.log(`Skipping FAQ ${index} - no valid question`);
                        return;
                    }
                    
                    console.log(`Processing FAQ ${index + 1}: ${question.substring(0, 50)}...`);
                    
                    // Find corresponding answer
                    let answer = '';
                    let tables = [];
                    let images = [];
                    let lists = [];
                    
                    // Look for answer - expand the search
                    let currentElement = qElem;
                    let attempts = 0;
                    const maxAttempts = 5;
                    
                    while (currentElement && attempts < maxAttempts) {
                        attempts++;
                        currentElement = currentElement.nextElementSibling;
                        
                        if (!currentElement) break;
                        
                        // Check if this element could contain an answer
                        const elementClass = currentElement.className || '';
                        const elementId = currentElement.id || '';
                        
                        // Multiple indicators of answer content
                        const isAnswerElement = 
                            elementClass.includes('f61835') ||
                            elementClass.includes('answer') ||
                            elementClass.includes('accordion__content') ||
                            elementClass.includes('faq-answer') ||
                            elementClass.includes('wiki') ||
                            elementId.includes('answer');
                        
                        if (isAnswerElement) {
                            // Look for answer content
                            const contentSelectors = [
                                '.wikkiContents',
                                '.answer-content',
                                '.faq-answer',
                                'p',
                                'div'
                            ];
                            
                            for (const selector of contentSelectors) {
                                const contentElement = currentElement.querySelector(selector);
                                if (contentElement && contentElement.textContent.trim()) {
                                    // Clone to avoid modifying original
                                    const answerClone = contentElement.cloneNode(true);
                                    
                                    // Clean the clone
                                    const unwantedSelectors = [
                                        '.a4bbdd', '.cf05b5', '.eee715',
                                        '.ask-gpt', '.feedback',
                                        '.advertisement', '.ads'
                                    ];
                                    
                                    unwantedSelectors.forEach(unwanted => {
                                        const elements = answerClone.querySelectorAll(unwanted);
                                        elements.forEach(el => el.remove());
                                    });
                                    
                                    // Get cleaned text
                                    answer = answerClone.textContent.trim();
                                    
                                    // Clean answer text
                                    answer = answer.replace(/^A:?\\s*/i, '');
                                    answer = answer.replace(/^Ans:?\\s*/i, '');
                                    answer = answer.replace(/Not satisfied with answer.*/gi, '');
                                    answer = answer.replace(/Ask Shiksha GPT.*/gi, '');
                                    answer = answer.replace(/\\s*\\n\\s*/g, ' ');
                                    answer = answer.replace(/\\s+/g, ' ').trim();
                                    
                                    // Extract tables if present
                                    const tableElements = contentElement.querySelectorAll('table');
                                    tableElements.forEach(table => {
                                        try {
                                            const tableData = {
                                                headers: [],
                                                rows: []
                                            };
                                            
                                            // Extract headers
                                            const thElements = table.querySelectorAll('th');
                                            if (thElements.length > 0) {
                                                thElements.forEach(th => {
                                                    tableData.headers.push(th.textContent.trim());
                                                });
                                            }
                                            
                                            // Extract rows
                                            const trElements = table.querySelectorAll('tr');
                                            trElements.forEach(tr => {
                                                // Skip header rows already captured
                                                if (tr.querySelector('th')) return;
                                                
                                                const rowData = [];
                                                const tdElements = tr.querySelectorAll('td');
                                                tdElements.forEach(td => {
                                                    rowData.push(td.textContent.trim());
                                                });
                                                
                                                if (rowData.length > 0) {
                                                    tableData.rows.push(rowData);
                                                }
                                            });
                                            
                                            if (tableData.headers.length > 0 || tableData.rows.length > 0) {
                                                tables.push(tableData);
                                            }
                                        } catch (e) {
                                            console.log('Error extracting table:', e);
                                        }
                                    });
                                    
                                    // Extract images
                                    const imgElements = contentElement.querySelectorAll('img');
                                    imgElements.forEach(img => {
                                        if (img.src) {
                                            images.push({
                                                src: img.src,
                                                alt: img.alt || '',
                                                width: img.width || 0,
                                                height: img.height || 0
                                            });
                                        }
                                    });
                                    
                                    // Extract lists
                                    const listElements = contentElement.querySelectorAll('ul, ol');
                                    listElements.forEach(list => {
                                        const listItems = [];
                                        const items = list.querySelectorAll('li');
                                        items.forEach(item => {
                                            listItems.push(item.textContent.trim());
                                        });
                                        if (listItems.length > 0) {
                                            lists.push(listItems);
                                        }
                                    });
                                    
                                    break;
                                }
                            }
                            
                            if (answer) break;
                        }
                    }
                    
                    if (answer) {
                        faqs.push({
                            faq_number: index + 1,
                            question: question,
                            answer: {
                                text: answer.substring(0, 3000),
                                has_table: tables.length > 0,
                                has_image: images.length > 0,
                                has_list: lists.length > 0
                            },
                            tables: tables.length > 0 ? tables : undefined,
                            images: images.length > 0 ? images : undefined,
                            lists: lists.length > 0 ? lists : undefined
                        });
                        console.log(`✓ Added FAQ ${index + 1}`);
                    } else {
                        console.log(`✗ No answer found for FAQ ${index + 1}`);
                    }
                } catch (e) {
                    console.log(`Error processing FAQ ${index}:`, e);
                }
            });
            
            console.log(`Total FAQs extracted: ${faqs.length}`);
            return faqs;
        """)
        
        if js_faqs and len(js_faqs) > 0:
            faqs_data = js_faqs
           
        else:
         
            
            # Alternative: Try to find FAQ items using various patterns
            try:
                print("Looking for FAQ patterns...")
                
                # Try to find any text containing Q: pattern
                page_text = driver.page_source
                import re
                
                # Look for Q: pattern in the page
                q_patterns = [
                    r'Q:\s*([^<]+?)<',
                    r'<[^>]*>Q[:\s]+([^<]+?)<',
                    r'question[^>]*>([^<]+?)<',
                    r'<div[^>]*class="[^"]*(?:question|faq)[^"]*"[^>]*>([^<]+?)<'
                ]
                
                all_questions = []
                for pattern in q_patterns:
                    matches = re.findall(pattern, page_text, re.IGNORECASE)
                    if matches:
                        all_questions.extend(matches)
                
                if all_questions:
                    print(f"Found {len(all_questions)} potential questions via regex")
                    
                    for i, question in enumerate(set(all_questions[:10]), 1):  # Limit to 10 unique
                        if len(question.strip()) > 10:  # Valid question
                            faqs_data.append({
                                "faq_number": i,
                                "question": question.strip()[:500],
                                "answer": {
                                    "text": "Answer not found (dynamic content)",
                                    "has_table": False,
                                    "has_image": False,
                                    "has_list": False
                                }
                            })
                
            except Exception as e:
                print("Manual extraction failed:")
        
    except Exception as e:
        print("Error extracting FAQ section: ")
        import traceback
        traceback.print_exc()
    
    # Create final result structure
    result = {
        "faq_section": {
            "heading": section_heading or "FAQs",
            "introduction": intro_text,
            "total_faqs": len(faqs_data),
            "faqs": faqs_data
        }
    }
    
    return result
# ---------------- FEES ----------------
def scrape_fees(driver, URLS):
    try:
        driver.get(URLS["fees"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["fees"])
    
    wait = WebDriverWait(driver, 20)
    
    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
    }
    
    fees_data = []
    course_details = []
    faqs_data = []
    overview_description = ""

    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image
        try:
            top_header_section = driver.find_element(By.ID, "topHeaderCard-top-section")
            cover_img = top_header_section.find_element(By.ID, "topHeaderCard-gallery-image")
            college_info["cover_image"] = cover_img.get_attribute("src")

        except:
            pass
        
        # Extract logo
        try:
            logo_div = driver.find_element(By.CSS_SELECTOR, ".ca46d2.e014b3")
            logo_img = logo_div.find_element(By.TAG_NAME, "img")
            college_info["logo"] = logo_img.get_attribute("src")
            
        except:
           pass
        
        # Extract videos and photos count
        try:
            badges_div = driver.find_element(By.CSS_SELECTOR, ".e4df0b.ad160e")
            badges = badges_div.find_elements(By.CSS_SELECTOR, ".dcd631")
            
            for badge in badges:
                text = badge.text.lower()
                if "video" in text:
                    videos_match = re.search(r'(\d+)\s*videos?', text)
                    if videos_match:
                        college_info["videos_count"] = int(videos_match.group(1))
                elif "photo" in text:
                    photos_match = re.search(r'(\d+)\s*photos?', text)
                    if photos_match:
                        college_info["photos_count"] = int(photos_match.group(1))
        except:
            pass
        
        # Rest of your existing header extraction code...
        
    except Exception as e:
        print("⚠️ Error in college header section:")
    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Try to find college name from various selectors
        try:
            h1_elements = driver.find_elements(By.TAG_NAME, "h1")
            for h1 in h1_elements:
                if h1.text and ("Fees" in h1.text or "IIM" in h1.text):
                    college_info["college_name"] = h1.text.replace(" Fees", "").replace(" - Indian Institute of Management", "").strip()
                    break
        except:
            pass

        # Extract from the provided HTML structure
        try:
            header_section = driver.find_element(By.CSS_SELECTOR, ".a655da.aadf9d")
            
            # College name
            try:
                name_elem = header_section.find_element(By.CSS_SELECTOR, "h1.cc5e8d")
                college_info["college_name"] = name_elem.text.strip()
            except:
                pass
            
            # Location
            try:
                location_div = header_section.find_element(By.CSS_SELECTOR, ".de89cf")
                location_text = location_div.text.strip()
                if "," in location_text:
                    parts = [p.strip() for p in location_text.split(",", 1)]
                    college_info["location"] = parts[0].replace(",", "").strip()
                    college_info["city"] = parts[1] if len(parts) > 1 else ""
            except:
                pass
            
            # Rating and reviews
            try:
                rating_div = header_section.find_element(By.CSS_SELECTOR, ".e6f71f")
                rating_text = rating_div.text.strip()
                rating_match = re.search(r"(\d+\.\d+)\s*/\s*5", rating_text)
                if rating_match:
                    college_info["rating"] = rating_match.group(1)
                
                reviews_match = re.search(r"\((\d+)\s*Reviews", rating_text)
                if reviews_match:
                    college_info["reviews_count"] = int(reviews_match.group(1))
            except:
                pass
            
            # Q&A count
            try:
                qa_link = header_section.find_element(By.XPATH, ".//a[contains(text(), 'Student Q&A')]")
                qa_text = qa_link.text.strip()
                qa_match = re.search(r"(\d+(?:\.\d+)?)\s*(k|K)?", qa_text)
                if qa_match:
                    count = float(qa_match.group(1))
                    if qa_match.group(2):
                        count = int(count * 1000)
                    college_info["qa_count"] = int(count)
            except:
                pass
            
            # Institute type and established year
            try:
                list_items = header_section.find_elements(By.CSS_SELECTOR, ".ff9e36 li")
                for li in list_items:
                    text = li.text.strip().lower()
                    if "institute" in text:
                        college_info["institute_type"] = li.text.strip()
                    elif "estd" in text:
                        year_match = re.search(r"\b(\d{4})\b", li.text)
                        if year_match:
                            college_info["established_year"] = year_match.group(1)
            except:
                pass
                
        except Exception as e:
            print("⚠️ Error extracting header info:")

    except Exception as e:
        print("⚠️ Error in college header section:")

    # ---------- FEES OVERVIEW TABLE ----------

    
    try:
        # Look for fees overview table
        fees_section = wait.until(
            EC.presence_of_element_located((By.ID, "fees_section_overview"))
        )
        
        # Extract overview table
        try:
            table = fees_section.find_element(By.CSS_SELECTOR, "table.table")
            rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
            
            for row in rows:
                try:
                    # Extract course name
                    course_elem = row.find_element(By.CSS_SELECTOR, "td:first-child a")
                    course_name = course_elem.text.strip()
                    
                    # Extract fees
                    fees_elem = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)")
                    fees_text = fees_elem.text.strip().replace("Get Fee Details", "").strip()
                    
                    # Clean up course name
                    if "Courses" in course_name:
                        course_name = course_name.split("(")[0].strip()
                    
                    fees_data.append({
                        "course": course_name,
                        "total_tuition_fees": fees_text
                    })
                    
                except Exception as e:
                    continue
                    
        except Exception as e:
            print("⚠️ Error extracting overview table: ")

        try:
            overview_desc = fees_section.find_element(By.CSS_SELECTOR, ".wikiContents .faq__according-wrapper p")
            overview_description = clean_text(overview_desc.text)
           
        except Exception as e:
            print("⚠️ Could not extract overview description: ")
            # Fallback: Try with BeautifulSoup
            try:
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                fees_section_soup = soup.find('section', {'id': 'fees_section_overview'})
                if fees_section_soup:
                    overview_div = fees_section_soup.find('div', {'class': 'wikiContents'})
                    if overview_div:
                        overview_para = overview_div.find('p')
                        if overview_para:
                            overview_description = clean_text(overview_para.text)
                            print(f"\nOverview (fallback): {overview_description[:200]}...")
            except:
                pass
    except Exception as e:
        print("⚠️ Fees overview section not found:")

    # ---------- DETAILED COURSE FEES ----------

    
    try:
        # Find all course fee sections
        course_sections = driver.find_elements(By.CSS_SELECTOR, "[id^='fees_section_about_baseCourse_']")
        
        print(f"Found {len(course_sections)} detailed course sections")
        
        for section in course_sections:
            try:
                # Extract course name
                course_name = ""
                try:
                    course_name_elem = section.find_element(By.CSS_SELECTOR, ".ae88c4")
                    course_name = course_name_elem.text.strip()
                except:
                    pass
                
                if not course_name:
                    continue
                
                # Extract course description
                course_desc = ""
                try:
                    desc_elem = section.find_element(By.CSS_SELECTOR, ".wikiContents .faq__according-wrapper p")
                    course_desc = desc_elem.text.strip()[:300]
                except:
                    pass
                
                # Extract fee components table
                fee_components = []
                try:
                    fee_table = section.find_element(By.CSS_SELECTOR, "table.table.f866a4")
                    rows = fee_table.find_elements(By.CSS_SELECTOR, "tbody tr")
                    
                    for row in rows:
                        try:
                            component_elem = row.find_element(By.CSS_SELECTOR, "td:first-child")
                            amount_elem = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)")
                            
                            component = component_elem.text.strip()
                            amount = amount_elem.text.strip()
                            
                            # Extract detailed description if available
                            component_desc = ""
                            try:
                                desc_div = component_elem.find_element(By.CSS_SELECTOR, ".c3bd41")
                                component_desc = desc_div.text.strip()
                            except:
                                pass
                            
                            fee_components.append({
                                "component": component,
                                "amount": amount,
                                "description": component_desc
                            })
                            
                        except:
                            continue
                except:
                    pass
                
                # Extract comparison data if available
                comparison_data = []
                try:
                    comparison_section = section.find_element(By.ID, "fees_section_fees_comparison")
                    comp_table = comparison_section.find_element(By.CSS_SELECTOR, "table.table.f6a6c1")
                    comp_rows = comp_table.find_elements(By.CSS_SELECTOR, "tbody tr")
                    
                    for row in comp_rows[:3]:  # Limit to top 3
                        try:
                            college_elem = row.find_element(By.CSS_SELECTOR, "td:first-child a")
                            tuition_elem = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)")
                            hostel_elem = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)")
                            
                            comparison_data.append({
                                "college": college_elem.text.strip(),
                                "tuition_fees": tuition_elem.text.strip(),
                                "hostel_fees": hostel_elem.text.strip()
                            })
                        except:
                            continue
                except:
                    pass
                
                # Extract course-specific FAQs
                course_faqs = []
                try:
                    faq_section = section.find_element(By.CSS_SELECTOR, ".a5ea4c.sectional-faqs")
                    faq_items = faq_section.find_elements(By.CSS_SELECTOR, ".html-0.ea1844.listener")
                    
                    for i, faq_item in enumerate(faq_items[:5], 1):  # Limit to 5
                        try:
                            question = ""
                            answer = ""
                            
                            # Extract question
                            try:
                                question_spans = faq_item.find_elements(By.CSS_SELECTOR, ".flx-box span")
                                if len(question_spans) >= 3:
                                    question = question_spans[2].text.strip()
                                else:
                                    question = faq_item.text.replace("Q:", "").strip()
                            except:
                                question = faq_item.text.strip()
                            
                            # Try to find answer
                            try:
                                # Find next sibling with answer class
                                answer_div = driver.execute_script("""
                                    var elem = arguments[0];
                                    var next = elem.nextElementSibling;
                                    while (next) {
                                        if (next.classList && next.classList.contains('f61835')) {
                                            var answerContent = next.querySelector('.wikkiContents');
                                            if (answerContent) {
                                                return answerContent.textContent.trim();
                                            }
                                        }
                                        next = next.nextElementSibling;
                                    }
                                    return '';
                                """, faq_item)
                                
                                if answer_div:
                                    answer = answer_div.replace("A:", "").strip()
                                    answer = re.sub(r'Not satisfied with answer.*', '', answer, flags=re.IGNORECASE)
                                    answer = re.sub(r'Ask Shiksha GPT.*', '', answer, flags=re.IGNORECASE)
                                    answer = re.sub(r'\s+', ' ', answer).strip()
                            except:
                                pass
                            
                            if question and answer:
                                course_faqs.append({
                                    "faq_number": i,
                                    "question": question,
                                    "answer": answer[:500]
                                })
                                
                        except:
                            continue
                except:
                    pass
                
                # Add to course details
                course_details.append({
                    "course_name": course_name,
                    "course_description": course_desc,
                    "fee_components": fee_components,
                    "comparison_colleges": comparison_data,
                    "course_faqs": course_faqs
                })
                
            
                
            except Exception as e:
                print("  ⚠️ Error processing course section:")
                continue
        
    except Exception as e:
        print("⚠️ Error extracting detailed course fees:")


    
    try:
        # Look for FAQ section in fees overview
        faq_container = driver.find_element(By.CSS_SELECTOR, ".a5ea4c.sectional-faqs")
        faq_items = faq_container.find_elements(By.CSS_SELECTOR, ".html-0.ea1844.listener")
        
        print("Found {len(faq_items)} FAQ items in overview")
        
        for i, faq_item in enumerate(faq_items, 1):
            try:
                question = ""
                answer = ""
                
                # Extract question
                try:
                    question_spans = faq_item.find_elements(By.CSS_SELECTOR, ".flx-box span")
                    if len(question_spans) >= 3:
                        question = question_spans[2].text.strip()
                    else:
                        question = faq_item.text.replace("Q:", "").strip()
                except:
                    question = faq_item.text.strip()
                
                # Extract answer using JavaScript
                try:
                    answer_div = driver.execute_script("""
                        var elem = arguments[0];
                        var next = elem.nextElementSibling;
                        while (next) {
                            if (next.classList && next.classList.contains('f61835')) {
                                var answerContent = next.querySelector('.wikkiContents');
                                if (answerContent) {
                                    // Clone and clean the content
                                    var clone = answerContent.cloneNode(true);
                                    var unwanted = clone.querySelectorAll('.a4bbdd, .cf05b5, .eee715');
                                    unwanted.forEach(function(el) {
                                        el.remove();
                                    });
                                    return clone.textContent.trim();
                                }
                            }
                            next = next.nextElementSibling;
                        }
                        return '';
                    """, faq_item)
                    
                    if answer_div:
                        answer = answer_div.replace("A:", "").strip()
                        answer = re.sub(r'Not satisfied with answer.*', '', answer, flags=re.IGNORECASE)
                        answer = re.sub(r'Ask Shiksha GPT.*', '', answer, flags=re.IGNORECASE)
                        answer = re.sub(r'\s+', ' ', answer).strip()
                except:
                    pass
                
                if question and answer:
                    # Check if answer has tables
                    has_table = "table" in answer_div.lower() if answer_div else False
                    
                    faqs_data.append({
                        "faq_number": i,
                        "question": question,
                        "answer": answer[:1000],
                        "has_table": has_table,
                        "section": "Fees Overview"
                    })
                    
                  
                    
            except Exception as e:
              
                continue
                
    except Exception as e:
        print("⚠️ FAQ section not found: ")

    # ---------- FINAL RESULT ----------
    result = {
        "college_info": college_info,
        "fees_overview": {
            "description":overview_description,
            "summary_table": fees_data,
            "total_courses": len(fees_data)
            
        },
        "course_details": course_details,
        "faqs": {
            "overview_faqs": faqs_data,
            "total_faqs": len(faqs_data) + sum(len(course.get("course_faqs", [])) for course in course_details)
        }
    }

    return result

def scrape_review_summary(driver, URLS):
    try:
        driver.get(URLS["reviews"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["reviews"])
    wait = WebDriverWait(driver, 20)
    
    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
        "review_summary": {},  # Added for review summary data
        "review_videos": [],   # Added for review videos
        "individual_reviews": []  # Added for individual reviews
    }
    


    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image
        try:
            top_header_section = driver.find_element(By.ID, "topHeaderCard-top-section")
            cover_img = top_header_section.find_element(By.ID, "topHeaderCard-gallery-image")
            college_info["cover_image"] = cover_img.get_attribute("src")
        except:
           pass
        
        # Extract logo
        try:
            logo_div = driver.find_element(By.CSS_SELECTOR, ".ca46d2.e014b3")
            logo_img = logo_div.find_element(By.TAG_NAME, "img")
            college_info["logo"] = logo_img.get_attribute("src")
    
        except:
            pass
        
        # Extract videos and photos count
        try:
            badges_div = driver.find_element(By.CSS_SELECTOR, ".e4df0b.ad160e")
            badges = badges_div.find_elements(By.CSS_SELECTOR, ".dcd631")
            
            for badge in badges:
                text = badge.text.lower()
                if "video" in text:
                    videos_match = re.search(r'(\d+)\s*videos?', text)
                    if videos_match:
                        college_info["videos_count"] = int(videos_match.group(1))
                elif "photo" in text:
                    photos_match = re.search(r'(\d+)\s*photos?', text)
                    if photos_match:
                        college_info["photos_count"] = int(photos_match.group(1))
        except:
            print("⚠️ Videos/Photos count not found")
        
        # Rest of your existing header extraction code...
        
    except Exception as e:
        print("⚠️ Error in college header section:")
    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Try to find college name from various selectors
        try:
            h1_elements = driver.find_elements(By.TAG_NAME, "h1")
            for h1 in h1_elements:
                if h1.text and ("Fees" in h1.text or "IIM" in h1.text):
                    college_info["college_name"] = h1.text.replace(" Fees", "").replace(" - Indian Institute of Management", "").strip()
                    break
        except:
            pass

        # Extract from the provided HTML structure
        try:
            header_section = driver.find_element(By.CSS_SELECTOR, ".a655da.aadf9d")
            
            # College name
            try:
                name_elem = header_section.find_element(By.CSS_SELECTOR, "h1.cc5e8d")
                college_info["college_name"] = name_elem.text.strip()
            except:
                pass
            
            # Location
            try:
                location_div = header_section.find_element(By.CSS_SELECTOR, ".de89cf")
                location_text = location_div.text.strip()
                if "," in location_text:
                    parts = [p.strip() for p in location_text.split(",", 1)]
                    college_info["location"] = parts[0].replace(",", "").strip()
                    college_info["city"] = parts[1] if len(parts) > 1 else ""
            except:
                pass
            
            # Rating and reviews
            try:
                rating_div = header_section.find_element(By.CSS_SELECTOR, ".e6f71f")
                rating_text = rating_div.text.strip()
                rating_match = re.search(r"(\d+\.\d+)\s*/\s*5", rating_text)
                if rating_match:
                    college_info["rating"] = rating_match.group(1)
                
                reviews_match = re.search(r"\((\d+)\s*Reviews", rating_text)
                if reviews_match:
                    college_info["reviews_count"] = int(reviews_match.group(1))
            except:
                pass
            
            # Q&A count
            try:
                qa_link = header_section.find_element(By.XPATH, ".//a[contains(text(), 'Student Q&A')]")
                qa_text = qa_link.text.strip()
                qa_match = re.search(r"(\d+(?:\.\d+)?)\s*(k|K)?", qa_text)
                if qa_match:
                    count = float(qa_match.group(1))
                    if qa_match.group(2):
                        count = int(count * 1000)
                    college_info["qa_count"] = int(count)
            except:
                pass
            
            # Institute type and established year
            try:
                list_items = header_section.find_elements(By.CSS_SELECTOR, ".ff9e36 li")
                for li in list_items:
                    text = li.text.strip().lower()
                    if "institute" in text:
                        college_info["institute_type"] = li.text.strip()
                    elif "estd" in text:
                        year_match = re.search(r"\b(\d{4})\b", li.text)
                        if year_match:
                            college_info["established_year"] = year_match.group(1)
            except:
                pass
                
        except Exception as e:
            print("⚠️ Error extracting header info:")

    except Exception as e:
        print("⚠️ Error in college header section:")
    
    # ---------- REVIEW SUMMARY SECTION ----------
    try:
      
        review_summary_section = driver.find_element(By.ID, "review_section_ratings_summary")
        
        # Extract overall rating
        try:
            rating_element = review_summary_section.find_element(By.CSS_SELECTOR, ".fd70d3")
            rating_text = rating_element.text.strip()
            rating_match = re.search(r'(\d+\.\d+)', rating_text)
            if rating_match:
                college_info["review_summary"]["overall_rating"] = rating_match.group(1)

        except Exception as e:
            print("⚠️ Overall rating not found in review summary:")
        
        # Extract verified reviews count
        try:
            verified_element = review_summary_section.find_element(By.CSS_SELECTOR, ".f62eee")
            verified_text = verified_element.text.strip()
            verified_match = re.search(r'(\d+)\s*Verified Reviews', verified_text)
            if verified_match:
                college_info["review_summary"]["verified_reviews_count"] = int(verified_match.group(1))

        except Exception as e:
            print("⚠️ Verified reviews count not found:")
        
        # Extract rating distribution
        try:
            rating_distribution = []
            rating_items = review_summary_section.find_elements(By.CSS_SELECTOR, ".a728a1 li")
            
            for item in rating_items:
                rating_range = item.find_element(By.CSS_SELECTOR, ".f81c43").text.strip()
                rating_count = item.find_element(By.CSS_SELECTOR, ".f65eaf").text.strip()
                
                # Extract percentage from style attribute
                percentage_element = item.find_element(By.CSS_SELECTOR, ".b5c9f3")
                style_attr = percentage_element.get_attribute("style")
                percentage_match = re.search(r'width:\s*(\d+)%', style_attr)
                percentage = percentage_match.group(1) + "%" if percentage_match else "0%"
                
                rating_distribution.append({
                    "range": rating_range,
                    "count": rating_count,
                    "percentage": percentage
                })
            
            college_info["review_summary"]["rating_distribution"] = rating_distribution
            
        except Exception as e:
            print("⚠️ Rating distribution not found:")
        
        # Extract category ratings
        try:
            category_ratings = []
            category_cards = review_summary_section.find_elements(By.CSS_SELECTOR, ".paper-card.boxShadow.d32700")
            
            for card in category_cards:
                category_name = card.find_element(By.CSS_SELECTOR, ".d7f853").text.strip()
                category_rating = card.find_element(By.CSS_SELECTOR, ".bfc017 span").text.strip()
                
                category_ratings.append({
                    "category": category_name,
                    "rating": category_rating
                })
            
            college_info["review_summary"]["category_ratings"] = category_ratings
      
        except Exception as e:
            print("⚠️ Category ratings not found:")
            
    except Exception as e:
        print("⚠️ Error scraping review summary section:")
    
    # ---------- REVIEW VIDEOS SECTION ----------
    try:
        
        # Find review videos section
        review_videos_section = driver.find_element(By.ID, "review_section_mini_clips")
        
        # Extract video title
        try:
            video_title = review_videos_section.find_element(By.CSS_SELECTOR, ".e2ac30").text.strip()
            
        except Exception as e:
            print("⚠️ Video section title not found:")
        
        # Extract video items
        try:
            video_items = review_videos_section.find_elements(By.CSS_SELECTOR, ".d87173.thumbnailListener")
            print(f"✓ Found {len(video_items)} video items")
            
            for video_item in video_items:
                video_data = {}
                
                # Extract video metadata
                try:
                    video_data["keyname"] = video_item.get_attribute("data-corouselkeyname")
                    video_data["keyid"] = video_item.get_attribute("data-corouselkeyid")
                    video_data["index"] = video_item.get_attribute("data-index")
                except:
                    pass
                
                # Extract YouTube video ID
                try:
                    iframe = video_item.find_element(By.TAG_NAME, "iframe")
                    src = iframe.get_attribute("src")
                    youtube_match = re.search(r'youtube\.com/embed/([a-zA-Z0-9_-]+)', src)
                    if youtube_match:
                        video_data["youtube_id"] = youtube_match.group(1)
                        video_data["type"] = "embedded_video"
                    else:
                        # Check for thumbnail image
                        img = video_item.find_element(By.TAG_NAME, "img")
                        src = img.get_attribute("src")
                        youtube_match = re.search(r'youtube\.com/vi/([a-zA-Z0-9_-]+)', src)
                        if youtube_match:
                            video_data["youtube_id"] = youtube_match.group(1)
                            video_data["type"] = "thumbnail"
                            video_data["thumbnail_url"] = src
                except:
                    pass
                
                # Extract video title/description
                try:
                    title_element = video_item.find_element(By.CSS_SELECTOR, ".ada2b9")
                    video_data["title"] = title_element.text.strip()
                except:
                    try:
                        # Alternative selector for title
                        alt_title = video_item.find_element(By.CSS_SELECTOR, ".e6852b")
                        video_data["title"] = alt_title.text.strip()
                    except:
                        pass
                
                if video_data:  # Only add if we have data
                    college_info["review_videos"].append(video_data)
                    
        except Exception as e:
            print("⚠️ Error extracting video items: ")
            
       
        
    except Exception as e:
        print("⚠️ Error scraping review videos section:")
    
    # ---------- INDIVIDUAL REVIEWS ----------
    try:
 
        review_cards = driver.find_elements(By.CSS_SELECTOR, ".paper-card[id^='review_']")
        
        
        for review_card in review_cards[:5]:  # Limit to first 5 reviews for efficiency
            try:
                review_data = {}
                
                # Extract review ID
                review_id = review_card.get_attribute("id")
                if review_id:
                    review_data["review_id"] = review_id.replace("review_", "")
                
                # Extract user information
                try:
                    user_name = review_card.find_element(By.CSS_SELECTOR, ".f1b51a").text.strip()
                    review_data["user_name"] = user_name
                    
                    # Check if verified
                    verified_badge = review_card.find_element(By.CSS_SELECTOR, "img[alt='Verified Icon']")
                    review_data["verified"] = True if verified_badge else False
                except:
                    pass
                
                # Extract user course/batch
                try:
                    course_element = review_card.find_element(By.CSS_SELECTOR, ".b7f142")
                    course_text = course_element.text.strip()
                    review_data["course"] = course_text
                except:
                    pass
                
                # Extract overall rating
                try:
                    overall_rating = review_card.find_element(By.CSS_SELECTOR, ".f05026 span")
                    review_data["overall_rating"] = overall_rating.text.strip()
                except:
                    pass
                
                # Extract category ratings
                try:
                    category_spans = review_card.find_elements(By.CSS_SELECTOR, ".d757cc")
                    category_ratings = {}
                    
                    for span in category_spans:
                        text = span.text.strip()
                        # Extract rating and category name
                        parts = text.split()
                        if len(parts) >= 2:
                            rating = parts[0]
                            category = " ".join(parts[1:])
                            category_ratings[category] = rating
                    
                    review_data["category_ratings"] = category_ratings
                except:
                    pass
                
                # Extract review title
                try:
                    review_title = review_card.find_element(By.CSS_SELECTOR, ".d7e2f2").text.strip()
                    review_data["title"] = review_title
                except:
                    pass
                
                # Extract review content sections
                try:
                    content_divs = review_card.find_elements(By.CSS_SELECTOR, ".dca212 > div")
                    review_content = {}
                    
                    for div in content_divs:
                        text = div.text.strip()
                        if ":" in text:
                            parts = text.split(":", 1)
                            category = parts[0].replace("<strong>", "").replace("</strong>", "").strip()
                            content = parts[1].strip()
                            review_content[category] = content
                    
                    review_data["content"] = review_content
                except:
                    pass
                
                # Extract review date
                try:
                    date_element = review_card.find_element(By.CSS_SELECTOR, ".f3dfa4")
                    date_text = date_element.text.strip()
                    review_data["review_date"] = date_text.replace("Reviewed on", "").strip()
                except:
                    pass
                
                # Only add review if we have some data
                if review_data:
                    college_info["individual_reviews"].append(review_data)
                    
            except Exception as e:
                print("⚠️ Error processing individual review:")
 
    except Exception as e:
        print("⚠️ Error scraping individual reviews:")
    
    return college_info


def scrape_admission_overview(driver, URLS):
    try:
        driver.get(URLS["admission"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["admission"])
    
    wait = WebDriverWait(driver, 30)
    
    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
        "admission_overview": {
            "title": "",
            "description": "",
            "key_points": [],
            "faqs": []
        },
        "eligibility_selection": {
            "title": "",
            "description": "",
            "courses_table": [],
            "faqs": []
        }
    }
    
    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image
        try:
            top_header_section = driver.find_element(By.ID, "topHeaderCard-top-section")
            cover_img = top_header_section.find_element(By.ID, "topHeaderCard-gallery-image")
            college_info["cover_image"] = cover_img.get_attribute("src")
           
        except:
            pass
        
        # Extract logo
        try:
            logo_div = driver.find_element(By.CSS_SELECTOR, ".ca46d2.e014b3")
            logo_img = logo_div.find_element(By.TAG_NAME, "img")
            college_info["logo"] = logo_img.get_attribute("src")
            
        except:
            pass
        
        # Extract videos and photos count
        try:
            badges_div = driver.find_element(By.CSS_SELECTOR, ".e4df0b.ad160e")
            badges = badges_div.find_elements(By.CSS_SELECTOR, ".dcd631")
            
            for badge in badges:
                text = badge.text.lower()
                if "video" in text:
                    videos_match = re.search(r'(\d+)\s*videos?', text)
                    if videos_match:
                        college_info["videos_count"] = int(videos_match.group(1))
                elif "photo" in text:
                    photos_match = re.search(r'(\d+)\s*photos?', text)
                    if photos_match:
                        college_info["photos_count"] = int(photos_match.group(1))
        except:
            print("⚠️ Videos/Photos count not found")
        
        # Rest of your existing header extraction code...
        
    except Exception as e:
        print("⚠️ Error in college header section:")
    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Try to find college name from various selectors
        try:
            h1_elements = driver.find_elements(By.TAG_NAME, "h1")
            for h1 in h1_elements:
                if h1.text and ("Fees" in h1.text or "IIM" in h1.text):
                    college_info["college_name"] = h1.text.replace(" Fees", "").replace(" - Indian Institute of Management", "").strip()
                    break
        except:
            pass

        # Extract from the provided HTML structure
        try:
            header_section = driver.find_element(By.CSS_SELECTOR, ".a655da.aadf9d")
            
            # College name
            try:
                name_elem = header_section.find_element(By.CSS_SELECTOR, "h1.cc5e8d")
                college_info["college_name"] = name_elem.text.strip()
            except:
                pass
            
            # Location
            try:
                location_div = header_section.find_element(By.CSS_SELECTOR, ".de89cf")
                location_text = location_div.text.strip()
                if "," in location_text:
                    parts = [p.strip() for p in location_text.split(",", 1)]
                    college_info["location"] = parts[0].replace(",", "").strip()
                    college_info["city"] = parts[1] if len(parts) > 1 else ""
            except:
                pass
            
            # Rating and reviews
            try:
                rating_div = header_section.find_element(By.CSS_SELECTOR, ".e6f71f")
                rating_text = rating_div.text.strip()
                rating_match = re.search(r"(\d+\.\d+)\s*/\s*5", rating_text)
                if rating_match:
                    college_info["rating"] = rating_match.group(1)
                
                reviews_match = re.search(r"\((\d+)\s*Reviews", rating_text)
                if reviews_match:
                    college_info["reviews_count"] = int(reviews_match.group(1))
            except:
                pass
            
            # Q&A count
            try:
                qa_link = header_section.find_element(By.XPATH, ".//a[contains(text(), 'Student Q&A')]")
                qa_text = qa_link.text.strip()
                qa_match = re.search(r"(\d+(?:\.\d+)?)\s*(k|K)?", qa_text)
                if qa_match:
                    count = float(qa_match.group(1))
                    if qa_match.group(2):
                        count = int(count * 1000)
                    college_info["qa_count"] = int(count)
            except:
                pass
            
            # Institute type and established year
            try:
                list_items = header_section.find_elements(By.CSS_SELECTOR, ".ff9e36 li")
                for li in list_items:
                    text = li.text.strip().lower()
                    if "institute" in text:
                        college_info["institute_type"] = li.text.strip()
                    elif "estd" in text:
                        year_match = re.search(r"\b(\d{4})\b", li.text)
                        if year_match:
                            college_info["established_year"] = year_match.group(1)
            except:
                pass
                
        except Exception as e:
            print("⚠️ Error extracting header info:")

    except Exception as e:
        print("⚠️ Error in college header section:")
    try:
       
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        
        for i in range(0, 2000, 300):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.5)
        
     
        
        try:
            overview_section = wait.until(
                EC.presence_of_element_located((By.ID, "admission_section_admission_overview"))
            )
            
            # Extract title
            try:
                title_div = overview_section.find_element(By.CSS_SELECTOR, ".ae88c4")
                college_info["admission_overview"]["title"] = title_div.text.strip()

            except:
                pass
            
            # Extract description
            try:
                wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#EdContent__admission_section_admission_overview")
                ))
                
                content_div = driver.find_element(By.CSS_SELECTOR, "#EdContent__admission_section_admission_overview")
                paragraphs = content_div.find_elements(By.TAG_NAME, "p")
                
                description_text = ""
                for p in paragraphs:
                    try:
                        text = p.text.strip()
                        if text and len(text) > 20:
                            description_text += text + " "
                    except:
                        continue
                
                college_info["admission_overview"]["description"] = description_text.strip()

                
            except Exception as e:
                print("⚠️ Error extracting admission overview description:")
            
            # Extract FAQs from admission overview
            try:
               
                faq_items = wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, "#admission_section_admission_overview .html-0.ea1844.listener")
                    )
                )
                
                for faq_item in faq_items:
                    try:
                        # Extract question
                        question_elem = faq_item.find_element(By.CSS_SELECTOR, "strong.flx-box")
                        question_text = question_elem.text.strip()
                        
                        # Clean question
                        if "Q:" in question_text:
                            question_text = question_text.split("Q:", 1)[1].strip()
                        elif "Q." in question_text:
                            question_text = question_text.split("Q.", 1)[1].strip()
                        
                        # Get answer
                        answer_text = ""
                        try:
                            # Get next sibling using XPath
                            answer_container = faq_item.find_element(By.XPATH, "following-sibling::div[1]")
                            answer_div = answer_container.find_element(By.CSS_SELECTOR, ".facb5f")
                            answer_text = answer_div.text.strip()
                            
                            # Clean answer
                            if "A:" in answer_text:
                                answer_text = answer_text.split("A:", 1)[1].strip()
                            elif "A." in answer_text:
                                answer_text = answer_text.split("A.", 1)[1].strip()
                            
                            # Remove GPT reference
                            if "Not satisfied with answer?" in answer_text:
                                answer_text = answer_text.split("Not satisfied with answer?")[0].strip()
                                
                        except:
                            continue
                        
                        if question_text and answer_text:
                            college_info["admission_overview"]["faqs"].append({
                                "question": question_text,
                                "answer": answer_text[:500]
                            })
                            
                    except Exception as e:
                        
                        continue
                
         
            except Exception as e:
                print("⚠️ Error extracting admission overview FAQs:")
                
        except Exception as e:
            print("⚠️ Admission overview section not found:")
        
        try:
            # Scroll to eligibility section
            driver.execute_script("window.scrollTo(0, 2000);")
            time.sleep(2)
            
            eligibility_section = wait.until(
                EC.presence_of_element_located((By.ID, "admission_section_eligibility_selection"))
            )
            
            # Extract title
            try:
                title_div = eligibility_section.find_element(By.CSS_SELECTOR, ".ae88c4")
                college_info["eligibility_selection"]["title"] = title_div.text.strip()
             
            except:
                pass
            
            # Extract description
            try:
                content_div = driver.find_element(By.CSS_SELECTOR, "#EdContent__admission_section_eligibility_selection")
                
                # Get description
                try:
                    description_div = content_div.find_element(By.CSS_SELECTOR, ".photo-widget-full")
                    description_text = description_div.text.strip()
                    
                    if "The table below" in description_text:
                        description_text = description_text.split("The table below")[0].strip()
                    
                    college_info["eligibility_selection"]["description"] = description_text
                    
                except:
                    # Fallback
                    paragraphs = content_div.find_elements(By.TAG_NAME, "p")
                    description_text = ""
                    for p in paragraphs[:2]:
                        text = p.text.strip()
                        if text:
                            description_text += text + " "
                    college_info["eligibility_selection"]["description"] = description_text.strip()
                
            except Exception as e:
                print("⚠️ Error extracting eligibility description:")
            
            # SIMPLIFIED TABLE EXTRACTION
            try:
                # Use JavaScript to extract table data
                table_script = """
                function extractCoursesTable() {
                    const allTables = document.querySelectorAll('#admission_section_eligibility_selection table');
                    const courses = [];
                    
                    for (const table of allTables) {
                        const rows = table.querySelectorAll('tr');
                        if (rows.length < 2) continue;
                        
                        // Check first row for headers
                        const firstRow = rows[0];
                        const headerCells = firstRow.querySelectorAll('th, td');
                        const headerText = Array.from(headerCells).map(cell => 
                            cell.textContent.toLowerCase().trim()
                        ).join(' ');
                        
                        // Check if this looks like a courses table
                        if (headerText.includes('course') && headerText.includes('eligibility') && 
                            (headerText.includes('selection') || headerText.includes('criteria'))) {
                            
                            console.log('Found courses table with', rows.length, 'rows');
                            
                            // Process data rows
                            for (let i = 1; i < rows.length; i++) {
                                const row = rows[i];
                                const cells = row.querySelectorAll('td');
                                
                                if (cells.length >= 3) {
                                    const courseCell = cells[0];
                                    const courseLink = courseCell.querySelector('a');
                                    const courseName = courseLink ? 
                                        courseLink.textContent.trim() : 
                                        courseCell.textContent.trim();
                                    
                                    const eligibility = cells[1].textContent.trim();
                                    const selection = cells[2].textContent.trim();
                                    
                                    // Clean the text
                                    const cleanCourse = courseName.replace(/\\s+/g, ' ').trim();
                                    const cleanEligibility = eligibility.replace(/\\s+/g, ' ').trim();
                                    const cleanSelection = selection.replace(/\\s+/g, ' ').trim();
                                    
                                    if (cleanCourse && cleanCourse.length > 2) {
                                        courses.push({
                                            course: cleanCourse,
                                            eligibility: cleanEligibility,
                                            selection_criteria: cleanSelection
                                        });
                                    }
                                }
                            }
                            break; // Stop after finding first valid table
                        }
                    }
                    return courses;
                }
                
                return extractCoursesTable();
                """
                
                courses_data = driver.execute_script(table_script)
                
                if courses_data and len(courses_data) > 0:
                    college_info["eligibility_selection"]["courses_table"] = courses_data
                    
                else:
               
                    try:
                        tables = eligibility_section.find_elements(By.TAG_NAME, "table")
                        print(f"Found {len(tables)} tables total")
                        
                        for table_idx, table in enumerate(tables):
                            try:
                                rows = table.find_elements(By.TAG_NAME, "tr")
                                if len(rows) > 1:
                                    # Check header
                                    header_cells = rows[0].find_elements(By.TAG_NAME, "th, td")
                                    if len(header_cells) >= 3:
                                        header_text = " ".join([cell.text.lower() for cell in header_cells])
                                        if "course" in header_text and "eligibility" in header_text:
                                            print(f"Table {table_idx + 1} looks like courses table")
                                            
                                            for i in range(1, len(rows)):
                                                try:
                                                    cells = rows[i].find_elements(By.TAG_NAME, "td")
                                                    if len(cells) >= 3:
                                                        course_name = cells[0].text.strip()
                                                        eligibility = cells[1].text.strip()
                                                        selection = cells[2].text.strip()
                                                        
                                                        if course_name:
                                                            college_info["eligibility_selection"]["courses_table"].append({
                                                                "course": course_name,
                                                                "eligibility": eligibility,
                                                                "selection_criteria": selection
                                                            })
                                                except:
                                                    continue
                                            break
                            except:
                                continue
                                
                    
                    except Exception as e:
                        print("Manual extraction failed: ")
                        
            except Exception as e:
                print("⚠️ Error extracting courses table: ")
            
      
            
            try:
                # Scroll to FAQ area
                driver.execute_script("window.scrollTo(0, 2500);")
                time.sleep(1)
                
                # Wait for FAQ section
                faq_section = wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "#admission_section_eligibility_selection .sectional-faqs")
                    )
                )
                
                # Get FAQ items
                faq_items = faq_section.find_elements(By.CSS_SELECTOR, ".html-0.ea1844")
                
                # SIMPLIFIED FAQ EXTRACTION WITHOUT JAVASCRIPT ERRORS
                for faq_item in faq_items:
                    try:
                        # Extract question
                        question_elem = faq_item.find_element(By.CSS_SELECTOR, "strong.flx-box")
                        question_text = question_elem.text.strip()
                        
                        # Clean question
                        question_text = re.sub(r'^Q[:.]\s*', '', question_text).strip()
                        
                        # Get answer using Python/Selenium only (no JavaScript)
                        answer_text = ""
                        try:
                            # Find next sibling div
                            answer_container = faq_item.find_element(By.XPATH, "following-sibling::div[1]")
                            
                            # Try to find answer text
                            try:
                                answer_elem = answer_container.find_element(By.CSS_SELECTOR, ".facb5f")
                                answer_text = answer_elem.text.strip()
                            except:
                                try:
                                    answer_elem = answer_container.find_element(By.CSS_SELECTOR, ".wikkiContents")
                                    answer_text = answer_elem.text.strip()
                                except:
                                    # Last resort: get all text
                                    answer_text = answer_container.text.strip()
                            
                            # Clean answer
                            answer_text = re.sub(r'^A[:.]\s*', '', answer_text).strip()
                            
                            # Remove GPT reference if present
                            if "Not satisfied with answer?" in answer_text:
                                answer_text = answer_text.split("Not satisfied with answer?")[0].strip()
                                
                        except Exception as e:
                           
                            continue
                        
                        if question_text and answer_text and len(question_text) > 10:
                            college_info["eligibility_selection"]["faqs"].append({
                                "question": question_text,
                                "answer": answer_text[:500]
                            })
                           
                    except Exception as e:
                        continue
                
                # If no FAQs found, try JavaScript approach (fixed)
                if len(college_info["eligibility_selection"]["faqs"]) == 0:
                  
                    try:
                        faq_js_script = """
                        var faqs = [];
                        var faqItems = document.querySelectorAll('#admission_section_eligibility_selection .html-0.ea1844');
                        
                        faqItems.forEach(function(item) {
                            try {
                                // Get question
                                var questionElem = item.querySelector('strong.flx-box');
                                if (!questionElem) return;
                                
                                var question = questionElem.textContent.trim();
                                question = question.replace(/^Q[:.]\\s*/, '').trim();
                                
                                // Get answer
                                var answer = '';
                                var nextSibling = item.nextElementSibling;
                                
                                if (nextSibling && nextSibling.classList.contains('f61835')) {
                                    var answerElem = nextSibling.querySelector('.facb5f') || nextSibling.querySelector('.wikkiContents');
                                    if (answerElem) {
                                        answer = answerElem.textContent.trim();
                                        answer = answer.replace(/^A[:.]\\s*/, '').trim();
                                        
                                        // Remove GPT reference
                                        if (answer.includes('Not satisfied with answer?')) {
                                            answer = answer.split('Not satisfied with answer?')[0].trim();
                                        }
                                    }
                                }
                                
                                if (question && answer && question.length > 10) {
                                    faqs.push({
                                        question: question,
                                        answer: answer
                                    });
                                }
                            } catch (e) {
                                console.error('Error processing FAQ:', e);
                            }
                        });
                        
                        return faqs;
                        """
                        
                        js_faqs = driver.execute_script(faq_js_script)
                        if js_faqs:
                            college_info["eligibility_selection"]["faqs"] = js_faqs
                         
                    except Exception as e:
                        print("JavaScript FAQ extraction failed: ")
                        
            except Exception as e:
                print("⚠️ Error extracting eligibility FAQs: ")
                
        except Exception as e:
            print("⚠️ Eligibility section not found: ")
        
    except Exception as e:
        print("⚠️ Main error in scraping: ")
        import traceback
        traceback.print_exc()

    try:
        # Wait for admission process section
        admission_process_section = wait.until(
            EC.presence_of_element_located((By.ID, "admission_section_admission_process"))
        )
        
        # Get the entire HTML of the section
        section_html = admission_process_section.get_attribute('outerHTML')
        
        # Use BeautifulSoup to parse and extract all text
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(section_html, 'html.parser')
        
        # Initialize admission process data structure
        admission_data = {
            "title": "",
            "full_content": {},
            "fees_table": [],
            "seats_table": [],
            "courses_data": [],
            "faqs": [],
            "videos": []
        }
        
        # 1. Extract Title
        title_elem = soup.find('div', class_='ae88c4')
        if title_elem:
            admission_data["title"] = title_elem.get_text(strip=True)
       
        # 2. Extract ALL Content - COMPLETE METHOD
        content_div = soup.find('div', id='EdContent__admission_section_admission_process')
        
        if content_div:
            # Initialize content structure
            admission_data["full_content"] = {
                "paragraphs": [],
                "headings": [],
                "lists": [],
                "tables": [],
                "key_points": []
            }
            
            # Extract all paragraphs
            paragraphs = content_div.find_all('p')
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text and len(text) > 10:
                    admission_data["full_content"]["paragraphs"].append(text)
            
            # Extract all headings (h1-h6)
            headings = content_div.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            for heading in headings:
                text = heading.get_text(strip=True)
                if text:
                    admission_data["full_content"]["headings"].append({
                        "tag": heading.name,
                        "text": text
                    })
            
            # Extract all lists
            lists = content_div.find_all(['ul', 'ol'])
            for list_elem in lists:
                list_items = list_elem.find_all('li')
                if list_items:
                    items_text = [li.get_text(strip=True) for li in list_items if li.get_text(strip=True)]
                    admission_data["full_content"]["lists"].append(items_text)
            
            # Extract key points from story-responsive
            story_div = content_div.find('div', class_='story-responsive')
            if story_div:
                figures = story_div.find_all('div', class_='figure')
                for figure in figures:
                    text = figure.get_text(strip=True)
                    if text:
                        admission_data["full_content"]["key_points"].append(text)
        
        # 3. Extract Fees Table - SIMPLIFIED
        fees_table = soup.find('table', style=lambda x: x and '620px' in str(x))
        if fees_table:
            rows = fees_table.find_all('tr')
            for row in rows[1:]:  # Skip header
                cols = row.find_all('td')
                if len(cols) >= 3:
                    admission_data["fees_table"].append({
                        "course": cols[0].get_text(strip=True),
                        "tuition_fee": cols[1].get_text(strip=True),
                        "average_package": cols[2].get_text(strip=True)
                    })
       
        # 4. Extract Seats Table - SIMPLIFIED
        seats_table = soup.find('table', class_='table _1708 d00e d8b0')
        if seats_table:
            rows = seats_table.find_all('tr')
            for row in rows[1:]:  # Skip header
                cols = row.find_all('td')
                if len(cols) >= 2:
                    admission_data["seats_table"].append({
                        "course": cols[0].get_text(strip=True),
                        "seats": cols[1].get_text(strip=True)
                    })
                # 5. Extract ALL Courses Data - COMPLETE METHOD
        course_sections = soup.find_all('div', id=lambda x: x and 'admission_section_admission_process_bac_' in x)
        
        for course_section in course_sections:
            course_info = {}
            
            # Course name and basic info
            header_div = course_section.find('div', class_='b2aeb1')
            if header_div:
                # Course name
                name_div = header_div.find('div', class_='ca2baa')
                if name_div:
                    course_info["name"] = name_div.get_text(strip=True)
                
                # Course stats
                stats_div = header_div.find('div', class_='e32f97')
                if stats_div:
                    stats_text = stats_div.get_text(strip=True)
                    course_info["stats"] = stats_text
            
            # Extract seat intake and fees from e88036
            stats_container = course_section.find('div', class_='e88036')
            if stats_container:
                stats_items = stats_container.find_all('div', class_='b4aebe')
                for item in stats_items:
                    label = item.find('label', class_='a8edfb')
                    value = item.find('span', class_='ee1018')
                    if label and value:
                        label_text = label.get_text(strip=True).lower().replace(' ', '_')
                        course_info[label_text] = value.get_text(strip=True)
            
            # Extract eligibility criteria
            eligibility_section = course_section.find('h3', class_='fa6426')
            if eligibility_section:
                # Get eligibility text
                eligibility_span = eligibility_section.find('span', class_='ded1b4')
                if eligibility_span and "Eligibility" in eligibility_span.get_text():
                    # Find the UL after this h3
                    ul_element = eligibility_section.find_next('ul', class_='de5ef8')
                    if ul_element:
                        items = ul_element.find_all('li')
                        eligibility_items = []
                        for item in items:
                            item_text = item.get_text(strip=True)
                            if item_text:
                                eligibility_items.append(item_text)
                        course_info["eligibility"] = eligibility_items
            
            # Extract cut-off tables if present
            cutoff_section = course_section.find('div', class_='d38e84')
            if cutoff_section:
                cutoff_tables = cutoff_section.find_all('table')
                course_info["cutoff_tables"] = []
                for table in cutoff_tables:
                    table_data = []
                    rows = table.find_all('tr')
                    for row in rows:
                        cells = row.find_all(['th', 'td'])
                        row_data = [cell.get_text(strip=True) for cell in cells]
                        table_data.append(row_data)
                    course_info["cutoff_tables"].append(table_data)
            
            # Extract course description from c7f019
            desc_div = course_section.find('div', class_='c7f019')
            if desc_div:
                wiki_div = desc_div.find('div', class_='wikiContents')
                if wiki_div:
                    # Get all paragraphs from description
                    desc_paragraphs = wiki_div.find_all('p')
                    description_text = []
                    for p in desc_paragraphs:
                        text = p.get_text(strip=True)
                        if text:
                            description_text.append(text)
                    course_info["description"] = " ".join(description_text)
            
            # Extract FAQs specific to this course
            faq_container = course_section.find('div', class_='ed0bed')
            if faq_container:
                faq_items = faq_container.find_all('div', class_='html-0')
                course_faqs = []
                for faq_item in faq_items:
                    question_elem = faq_item.find('strong', class_='flx-box')
                    if question_elem:
                        question_text = question_elem.get_text(strip=True)
                        # Clean question
                        question_text = re.sub(r'^Q[:.]\s*', '', question_text).strip()
                        
                        # Find answer
                        answer_text = ""
                        answer_div = faq_item.find_next('div', class_='f61835')
                        if answer_div:
                            answer_elem = answer_div.find('div', class_='facb5f')
                            if answer_elem:
                                answer_text = answer_elem.get_text(strip=True)
                                answer_text = re.sub(r'^A[:.]\s*', '', answer_text).strip()
                        
                        if question_text and answer_text:
                            course_faqs.append({
                                "question": question_text,
                                "answer": answer_text[:500]
                            })
                
                if course_faqs:
                    course_info["faqs"] = course_faqs
            
            if course_info:
                admission_data["courses_data"].append(course_info)
        
 
        # 6. Extract FAQs from the main FAQ section - COMPLETE METHOD
        faq_section = soup.find('div', id='sectional-faqs-0')
        if faq_section:
            faq_items = faq_section.find_all('div', class_='html-0')
            for faq_item in faq_items:
                try:
                    # Question
                    question_elem = faq_item.find('strong', class_='flx-box')
                    if question_elem:
                        question_text = question_elem.get_text(strip=True)
                        question_text = re.sub(r'^Q[:.]\s*', '', question_text).strip()
                        
                        # Answer
                        answer_text = ""
                        answer_container = faq_item.find_next('div', class_='f61835')
                        if answer_container:
                            answer_elem = answer_container.find('div', class_='facb5f')
                            if answer_elem:
                                answer_text = answer_elem.get_text(strip=True)
                                answer_text = re.sub(r'^A[:.]\s*', '', answer_text).strip()
                        
                        if question_text and answer_text:
                            admission_data["faqs"].append({
                                "question": question_text,
                                "answer": answer_text[:1000]  # Longer limit for complete answers
                            })
                except Exception as e:
                    continue
            
   
        # 7. Extract Videos
        video_widget = soup.find('div', id='reelsWidget')
        if video_widget:
            video_items = video_widget.find_all('li', class_='d87173')
            for video in video_items:
                try:
                    title_p = video.find('div', class_='ce64f8').find('p')
                    if title_p:
                        title = title_p.get_text(strip=True)
                        
                        # Duration
                        duration_p = title_p.find_next('p')
                        duration = duration_p.get_text(strip=True) if duration_p else ""
                        
                        admission_data["videos"].append({
                            "title": title,
                            "duration": duration
                        })
                except Exception as e:
                    continue
            
     
        # 8. Extract Additional Content - links, notes, etc.
        additional_content = {}
        
        # Extract all links
        links = content_div.find_all('a') if content_div else []
        additional_content["links"] = []
        for link in links[:10]:  # Limit to first 10 links
            link_text = link.get_text(strip=True)
            link_href = link.get('href', '')
            if link_text and link_href:
                additional_content["links"].append({
                    "text": link_text,
                    "url": link_href
                })
        
        # Extract notes and disclaimers
        notes = []
        if content_div:
            em_elements = content_div.find_all('em')
            for em in em_elements:
                text = em.get_text(strip=True)
                if text and ("Disclaimer" in text or "Note" in text):
                    notes.append(text)
        
        additional_content["notes"] = notes
        admission_data["additional_content"] = additional_content
        
        # Add to college_info
        college_info["admission_process"] = admission_data
        
   
    except Exception as e:
        import traceback
        traceback.print_exc()
        # Add empty structure anyway
        college_info["admission_process"] = {
            "title": "",
            "full_content": {},
            "fees_table": [],
            "seats_table": [],
            "courses_data": [],
            "faqs": [],
            "videos": []
        }
    
    return college_info
    

def scrape_placement_report(driver,URLS):
    try:
        driver.get(URLS["placement"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["placement"])
    
    wait = WebDriverWait(driver, 15)
    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
        "placement_data": {}
    }
    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image
        try:
            top_header_section = driver.find_element(By.ID, "topHeaderCard-top-section")
            cover_img = top_header_section.find_element(By.ID, "topHeaderCard-gallery-image")
            college_info["cover_image"] = cover_img.get_attribute("src")
            
        except:
            pass
        
        # Extract logo
        try:
            logo_div = driver.find_element(By.CSS_SELECTOR, ".ca46d2.e014b3")
            logo_img = logo_div.find_element(By.TAG_NAME, "img")
            college_info["logo"] = logo_img.get_attribute("src")
            
        except:
            pass
        
        # Extract videos and photos count
        try:
            badges_div = driver.find_element(By.CSS_SELECTOR, ".e4df0b.ad160e")
            badges = badges_div.find_elements(By.CSS_SELECTOR, ".dcd631")
            
            for badge in badges:
                text = badge.text.lower()
                if "video" in text:
                    videos_match = re.search(r'(\d+)\s*videos?', text)
                    if videos_match:
                        college_info["videos_count"] = int(videos_match.group(1))
                elif "photo" in text:
                    photos_match = re.search(r'(\d+)\s*photos?', text)
                    if photos_match:
                        college_info["photos_count"] = int(photos_match.group(1))
        except:
            print("⚠️ Videos/Photos count not found")
        
        # Rest of your existing header extraction code...
        
    except Exception as e:
        print("⚠️ Error in college header section: ")
    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Try to find college name from various selectors
        try:
            h1_elements = driver.find_elements(By.TAG_NAME, "h1")
            for h1 in h1_elements:
                if h1.text and ("Fees" in h1.text or "IIM" in h1.text):
                    college_info["college_name"] = h1.text.replace(" Fees", "").replace(" - Indian Institute of Management", "").strip()
                    break
        except:
            pass

        # Extract from the provided HTML structure
        try:
            header_section = driver.find_element(By.CSS_SELECTOR, ".a655da.aadf9d")
            
            # College name
            try:
                name_elem = header_section.find_element(By.CSS_SELECTOR, "h1.cc5e8d")
                college_info["college_name"] = name_elem.text.strip()
            except:
                pass
            
            # Location
            try:
                location_div = header_section.find_element(By.CSS_SELECTOR, ".de89cf")
                location_text = location_div.text.strip()
                if "," in location_text:
                    parts = [p.strip() for p in location_text.split(",", 1)]
                    college_info["location"] = parts[0].replace(",", "").strip()
                    college_info["city"] = parts[1] if len(parts) > 1 else ""
            except:
                pass
            
            # Rating and reviews
            try:
                rating_div = header_section.find_element(By.CSS_SELECTOR, ".e6f71f")
                rating_text = rating_div.text.strip()
                rating_match = re.search(r"(\d+\.\d+)\s*/\s*5", rating_text)
                if rating_match:
                    college_info["rating"] = rating_match.group(1)
                
                reviews_match = re.search(r"\((\d+)\s*Reviews", rating_text)
                if reviews_match:
                    college_info["reviews_count"] = int(reviews_match.group(1))
            except:
                pass
            
            # Q&A count
            try:
                qa_link = header_section.find_element(By.XPATH, ".//a[contains(text(), 'Student Q&A')]")
                qa_text = qa_link.text.strip()
                qa_match = re.search(r"(\d+(?:\.\d+)?)\s*(k|K)?", qa_text)
                if qa_match:
                    count = float(qa_match.group(1))
                    if qa_match.group(2):
                        count = int(count * 1000)
                    college_info["qa_count"] = int(count)
            except:
                pass
            
            # Institute type and established year
            try:
                list_items = header_section.find_elements(By.CSS_SELECTOR, ".ff9e36 li")
                for li in list_items:
                    text = li.text.strip().lower()
                    if "institute" in text:
                        college_info["institute_type"] = li.text.strip()
                    elif "estd" in text:
                        year_match = re.search(r"\b(\d{4})\b", li.text)
                        if year_match:
                            college_info["established_year"] = year_match.group(1)
            except:
                pass
                
        except Exception as e:
            print("⚠️ Error extracting header info: ")

    except Exception as e:
        print("⚠️ Error in college header section: ")
    try:
        # Wait for placement section to load
        wait.until(EC.presence_of_element_located((By.ID, "placement_section_overview")))
        
        # Scroll to placement section
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)
      
        try:
            # Look for "Read more" or "Read less" button
            read_more_buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'Read more') or contains(text(), 'Read less')]")
            
            if read_more_buttons:
            
                # Click the first one that's visible
                for button in read_more_buttons:
                    try:
                        if button.is_displayed():
                          
                            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
                            time.sleep(1)
                            
                            # Use JavaScript click to avoid interception
                            driver.execute_script("arguments[0].click();", button)
                           
                            time.sleep(3)  # Wait for content to expand
                            break
                    except:
                        continue
            else:
                pass
        except Exception as e:
            print("⚠️ Error clicking read more button: ")
        time.sleep(3)
        
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)
        
        # Now get the COMPLETE updated HTML
        placement_section = driver.find_element(By.ID, "placement_section_overview")
        
        # Get the complete HTML with JavaScript execution
        section_html = driver.execute_script("""
            var section = arguments[0];
            
            // Force all content to render
            var allElements = section.querySelectorAll('*');
            allElements.forEach(function(el) {
                // Force style computation
                var style = window.getComputedStyle(el);
            });
            
            // Return complete HTML
            return section.outerHTML;
        """, placement_section)
        
    
        soup = BeautifulSoup(section_html, 'html.parser')
        
        # Initialize placement data structure
        placement_data = {
            "title": "",
            "paragraphs": [],  # Main paragraphs
            "tables": [],     # All tables (including those in FAQs)
            "faqs": [],       # FAQ questions and answers
            "rating": "",
            "rating_details": "",
            "links": [],
            "user_feedback": "",
            "video_content": False,
            "stats_summary": {},
            "complete_content": ""  # Complete text content
        }
        
        # Extract title
        title_elem = soup.find('div', class_='ae88c4')
        if title_elem:
            placement_data["title"] = title_elem.get_text(strip=True)

        # Get the main content container
        content_div = soup.find('div', id='EdContent__placement_section_overview')
        
        if content_div:
        
            # Get complete text content
            complete_text = content_div.get_text(separator='\n', strip=True)
            placement_data["complete_content"] = complete_text
            paragraphs = []
            
            # First, try to find the main content wrapper
            content_wrapper = content_div.find('div', class_='faq__according-wrapper')
            if not content_wrapper:
                content_wrapper = content_div
            
            # Get all paragraphs
            p_tags = content_wrapper.find_all('p')
            for p in p_tags:
                text = p.get_text(separator=' ', strip=True)
                if text and len(text) > 20:  # Filter out very short text
                    text = ' '.join(text.split())
                    paragraphs.append(text)
            
            placement_data["paragraphs"] = paragraphs
           
            # Extract all tables from the entire section
            all_tables = []
            
            # Get tables from main content
            main_tables = content_div.find_all('table')
        
            for i, table in enumerate(main_tables):
                table_data = []
                rows = table.find_all('tr')
                
                for row in rows:
                    cells = row.find_all(['th', 'td'])
                    row_data = []
                    
                    for cell in cells:
                        cell_text = cell.get_text(separator=' ', strip=True)
                        cell_text = ' '.join(cell_text.split())
                        row_data.append(cell_text)
                    
                    if row_data:
                        table_data.append(row_data)
                
                if table_data:
                    all_tables.append({
                        "id": f"main_table_{i+1}",
                        "location": "main_content",
                        "data": table_data,
                        "rows": len(table_data),
                        "columns": len(table_data[0]) if table_data else 0
                    })
        
        # Now extract FAQs separately (you already have this working)
        faq_section = soup.find('div', id='sectional-faqs-0')
        if faq_section:
            faqs = []
            
            # Find all FAQ items
            faq_items = faq_section.find_all('div', class_='html-0')
            
            for faq_item in faq_items:
                try:
                    # Get question
                    question_elem = faq_item.find('strong', class_='flx-box')
                    if question_elem:
                        question_text = question_elem.get_text(strip=True)
                        # Clean question
                        import re
                        question_text = re.sub(r'^Q[:.]\s*', '', question_text).strip()
                        question_text = ' '.join(question_text.split())
                        
                        # Get answer
                        answer_container = faq_item.find_next('div', class_='f61835')
                        if answer_container:
                            # Try different selectors for answer
                            answer_div = answer_container.find('div', class_='wikkiContents')
                            if not answer_div:
                                answer_div = answer_container.find('div', class_='facb5f')
                            
                            if answer_div:
                                answer_text = answer_div.get_text(separator=' ', strip=True)
                                answer_text = re.sub(r'^A[:.]\s*', '', answer_text).strip()
                                answer_text = ' '.join(answer_text.split())
                                
                                # Also extract tables from FAQ answers
                                faq_tables = answer_div.find_all('table')
                                if faq_tables:
                                    for j, table in enumerate(faq_tables):
                                        table_data = []
                                        rows = table.find_all('tr')
                                        
                                        for row in rows:
                                            cells = row.find_all(['th', 'td'])
                                            row_data = [cell.get_text(separator=' ', strip=True) for cell in cells]
                                            row_data = [' '.join(cell.split()) for cell in row_data]
                                            if row_data:
                                                table_data.append(row_data)
                                        
                                        if table_data:
                                            all_tables.append({
                                                "id": f"faq_table_{len(all_tables)+1}",
                                                "location": f"faq_{len(faqs)+1}",
                                                "context": question_text[:50],
                                                "data": table_data,
                                                "rows": len(table_data),
                                                "columns": len(table_data[0]) if table_data else 0
                                            })
                                
                                if question_text and answer_text:
                                    faqs.append({
                                        "question": question_text,
                                        "answer": answer_text[:2000]  # Limit length
                                    })
                except Exception as e:
                  
                    continue
            
            placement_data["faqs"] = faqs
           
        
        # Add all tables to placement_data
        placement_data["tables"] = all_tables
        
        # Extract rating
        rating_div = soup.find('div', class_='c5d199')
        if rating_div:
            rating_text = rating_div.get_text(separator=' ', strip=True)
            rating_text = ' '.join(rating_text.split())
            placement_data["rating_details"] = rating_text
            
            import re
            rating_match = re.search(r'(\d+\.?\d*)', rating_text)
            if rating_match:
                placement_data["rating"] = rating_match.group(1)
        
        # Extract download links
        download_links = soup.find_all('a', class_='smce-docs')
        for link in download_links:
            link_text = link.get_text(separator=' ', strip=True)
            link_text = ' '.join(link_text.split())
            if link_text:
                placement_data["links"].append(link_text)
        
        # Extract user feedback
        feedback_div = soup.find('div', class_='d79b7a')
        if feedback_div:
            feedback_text = feedback_div.get_text(separator=' ', strip=True)
            feedback_text = ' '.join(feedback_text.split())
            placement_data["user_feedback"] = feedback_text
        
        # Check for video
        video_div = soup.find('div', class_='vcmsEmbed')
        if video_div:
            placement_data["video_content"] = True
        
        # Add to college_info
        college_info["placement_data"] = placement_data
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        
        # Minimal fallback
        college_info["placement_data"] = {
            "title": "IIM Ahmedabad Placement Overview 2025",
            "paragraphs": [],
            "tables": [],
            "faqs": [],
            "rating": "",
            "rating_details": "",
            "links": [],
            "user_feedback": "",
            "video_content": False,
            "error": str(e)
        }
    try:
        # Wait for average package section to load
        wait.until(EC.presence_of_element_located((By.ID, "placement_section_average_package")))
        
        # Scroll to the section
        driver.execute_script("window.scrollTo(0, 1500);")
        time.sleep(2)
        

        try:
            read_buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'Read more') or contains(text(), 'Read less')]")
            for button in read_buttons:
                try:
                    if button.is_displayed() and button.is_enabled():
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", button)
                        print("✓ Clicked read more/less button")
                        time.sleep(2)
                        break
                except:
                    continue
        except:
            pass
        
        # Get the section HTML
        avg_package_section = driver.find_element(By.ID, "placement_section_average_package")
        section_html = driver.execute_script("""
            var section = arguments[0];
            return section.outerHTML;
        """, avg_package_section)
    
   
        soup = BeautifulSoup(section_html, 'html.parser')
        
        # Initialize data structure
        avg_package_data = {
            "title": "",
            "main_table": [],
            "top_recruiters": [],
            "insights": [],
            "faqs": [],
            "graph_image": "",
            "source_info": "",
            "complete_content": ""
        }
        
        # Extract title
        title_elem = soup.find('div', class_='ae88c4')
        if title_elem:
            avg_package_data["title"] = title_elem.get_text(strip=True)

        # Get the main content container
        content_div = soup.find('div', id='EdContent__placement_section_average_package')
        
        if content_div:
            # Get complete text content
            complete_text = content_div.get_text(separator='\n', strip=True)
            avg_package_data["complete_content"] = complete_text
            
            # Extract main table
            main_table = content_div.find('table')
            if main_table:
                table_data = []
                rows = main_table.find_all('tr')
                
                for row in rows:
                    cells = row.find_all(['th', 'td'])
                    row_data = []
                    
                    for cell in cells:
                        cell_text = cell.get_text(separator=' ', strip=True)
                        cell_text = ' '.join(cell_text.split())
                        row_data.append(cell_text)
                    
                    if row_data:
                        table_data.append(row_data)
                
                avg_package_data["main_table"] = table_data
          
            # Extract introductory paragraph
            intro_paragraph = content_div.find('p')
            if intro_paragraph:
                intro_text = intro_paragraph.get_text(strip=True)
                intro_text = ' '.join(intro_text.split())
                avg_package_data["intro_text"] = intro_text
      
        # Find the Top Recruiters section
        recruiters_section = soup.find('div', class_='ca08b1')
        if recruiters_section:
            # Get the heading
            recruiters_heading = recruiters_section.find('p')
            if recruiters_heading:
                avg_package_data["recruiters_heading"] = recruiters_heading.get_text(strip=True)
            
            # Extract all recruiter names
            recruiters = []
            recruiter_spans = recruiters_section.find_all('span', class_='c4af72')
            for span in recruiter_spans:
                recruiter_name = span.get_text(strip=True)
                if recruiter_name:
                    recruiters.append(recruiter_name)
            
            avg_package_data["top_recruiters"] = recruiters
   
            # Sample recruiters
            if recruiters:
                print(f"  Sample: {recruiters[:5]}")
        
        # Extract Insights on Placements

        insights_section = soup.find('div', class_='b811f8')
        if insights_section:
            # Get insights heading
            insights_heading = insights_section.find('h4')
            if insights_heading:
                avg_package_data["insights_heading"] = insights_heading.get_text(strip=True)
            
            # Get student responses count
            responses_span = insights_section.find('span', class_='ede34e')
            if responses_span:
                avg_package_data["responses_count"] = responses_span.get_text(strip=True)
        
        # Extract individual insights
        insights = []
        insight_items = soup.find_all('div', class_='cdf9a8')
        
        for item in insight_items:
            try:
                # Get insight title
                title_elem = item.find('h6')
                if title_elem:
                    title = title_elem.get_text(strip=True)
                    
                    # Get insight description
                    desc_elem = item.find('p')
                    if desc_elem:
                        description = desc_elem.get_text(strip=True)
                        
                        insights.append({
                            "title": title,
                            "description": description
                        })
            except:
                continue
        
        avg_package_data["insights"] = insights
       
        # Extract graph image
        graph_img = soup.find('img', alt=lambda x: x and 'Average Package graph' in x)
        if graph_img:
            graph_src = graph_img.get('src', '')
            if graph_src:
                avg_package_data["graph_image"] = graph_src
             
        # Extract source information
        source_div = soup.find('div', class_='d4160c')
        if source_div:
            source_text = source_div.get_text(separator=' ', strip=True)
            source_text = ' '.join(source_text.split())
            avg_package_data["source_info"] = source_text
 
        faq_section = soup.find('div', id='sectional-faqs-0')
        if faq_section:
            faqs = []
            
            # Find all FAQ items
            faq_items = faq_section.find_all('div', class_='html-0')
            
            for faq_item in faq_items:
                try:
                    # Get question
                    question_elem = faq_item.find('strong', class_='flx-box')
                    if question_elem:
                        question_text = question_elem.get_text(strip=True)
                        # Clean question
                        import re
                        question_text = re.sub(r'^Q[:.]\s*', '', question_text).strip()
                        question_text = ' '.join(question_text.split())
                        
                        # Get answer
                        answer_container = faq_item.find_next('div', class_='f61835')
                        if answer_container:
                            # Try to find answer in wikkiContents
                            answer_div = answer_container.find('div', class_='wikkiContents')
                            if not answer_div:
                                answer_div = answer_container.find('div', class_='facb5f')
                            
                            if answer_div:
                                answer_text = answer_div.get_text(separator=' ', strip=True)
                                answer_text = re.sub(r'^A[:.]\s*', '', answer_text).strip()
                                answer_text = ' '.join(answer_text.split())
                                
                                # Extract tables from FAQ answers
                                faq_tables = []
                                tables_in_answer = answer_div.find_all('table')
                                
                                for table in tables_in_answer:
                                    table_data = []
                                    rows = table.find_all('tr')
                                    
                                    for row in rows:
                                        cells = row.find_all(['th', 'td'])
                                        row_data = [cell.get_text(separator=' ', strip=True) for cell in cells]
                                        row_data = [' '.join(cell.split()) for cell in row_data]
                                        if row_data:
                                            table_data.append(row_data)
                                    
                                    if table_data:
                                        faq_tables.append(table_data)
                                
                                if question_text and answer_text:
                                    faqs.append({
                                        "question": question_text,
                                        "answer": answer_text[:2000],  # Limit length
                                        "tables": faq_tables
                                    })
                except Exception as e:
                    
                    continue
            
            avg_package_data["faqs"] = faqs
            
        
        # Extract user feedback
        feedback_div = soup.find('div', class_='d79b7a')
        if feedback_div:
            feedback_text = feedback_div.get_text(separator=' ', strip=True)
            feedback_text = ' '.join(feedback_text.split())
            avg_package_data["user_feedback"] = feedback_text
        
        # Add to college_info (as a separate section)
        if "placement_sections" not in college_info:
            college_info["placement_sections"] = {}
        
        college_info["placement_sections"]["average_package"] = avg_package_data
        
        # Also add to main placement_data for backward compatibility
        if "placement_data" not in college_info:
            college_info["placement_data"] = {}
        
        # Add average package table to main placement_data
        if avg_package_data.get("main_table"):
            if "tables" not in college_info["placement_data"]:
                college_info["placement_data"]["tables"] = []
            
            college_info["placement_data"]["tables"].append({
                "title": "Average Package 2023-2025",
                "data": avg_package_data["main_table"]
            })
        
        # Add recruiters to main placement_data
        if avg_package_data.get("top_recruiters"):
            college_info["placement_data"]["top_recruiters"] = avg_package_data["top_recruiters"]
        
        # Add insights to main placement_data
        if avg_package_data.get("insights"):
            college_info["placement_data"]["insights"] = avg_package_data["insights"]
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        
        # Add empty section to avoid errors
        if "placement_sections" not in college_info:
            college_info["placement_sections"] = {}
        
        college_info["placement_sections"]["average_package"] = {
            "title": "IIM Ahmedabad Average Package 2025",
            "main_table": [],
            "top_recruiters": [],
            "insights": [],
            "faqs": [],
            "graph_image": "",
            "source_info": "",
            "complete_content": "",
            "error": str(e)
        }
    try:
        # Wait for PGP placements section to load
        wait.until(EC.presence_of_element_located((By.ID, "placement_section_about_baseCourse_101")))
        
        # Scroll to the section
        driver.execute_script("window.scrollTo(0, 2000);")
        time.sleep(2)
        
        # Click "Read more" if exists in this section
        try:
            section_element = driver.find_element(By.ID, "placement_section_about_baseCourse_101")
            read_buttons = section_element.find_elements(By.XPATH, ".//*[contains(text(), 'Read more') or contains(text(), 'Read less')]")
            for button in read_buttons:
                try:
                    if button.is_displayed():
                        driver.execute_script("arguments[0].click();", button)
                        print("✓ Clicked read more/less in PGP section")
                        time.sleep(2)
                        break
                except:
                    continue
        except:
            pass
        
        # Also try to expand the PGP FABM accordion if present
        try:
            fabm_accordion = driver.find_element(By.ID, "placement_section_class_profile")
            fabm_header = fabm_accordion.find_element(By.CLASS_NAME, "ca7e28")
            if fabm_header:
                driver.execute_script("arguments[0].click();", fabm_header)
                
                time.sleep(2)
        except:
            pass
        
        # Get the section HTML
        pgp_section = driver.find_element(By.ID, "placement_section_about_baseCourse_101")
        section_html = driver.execute_script("""
            var section = arguments[0];
            return section.outerHTML;
        """, pgp_section)
        
        soup = BeautifulSoup(section_html, 'html.parser')
        
        # Initialize data structure
        pgp_placements_data = {
            "title": "",
            "intro_text": "",
            "main_table": [],
            "placement_comparison": [],
            "pgp_fabm_data": {},
            "faqs": [],
            "placement_rating": "",
            "source_info": "",
            "complete_content": ""
        }
        
        # Extract title
        title_elem = soup.find('div', class_='ae88c4')
        if title_elem:
            pgp_placements_data["title"] = title_elem.get_text(strip=True)

        content_div = soup.find('div', id='EdContent_')
        if content_div:
            intro_text = content_div.get_text(separator='\n', strip=True)
            pgp_placements_data["complete_content"] = intro_text
            
            # Get paragraphs
            paragraphs = content_div.find_all('p')
            if paragraphs:
                intro_para = paragraphs[0].get_text(strip=True) if len(paragraphs) > 0 else ""
                key_para = paragraphs[1].get_text(strip=True) if len(paragraphs) > 1 else ""
                
                pgp_placements_data["intro_text"] = intro_para
                pgp_placements_data["key_points_text"] = key_para
          
        
        main_table = soup.find('table', class_='table d7ad5f f866a4 dc8ace')
        if main_table:
            table_data = []
            
            # Extract headers
            headers = []
            header_row = main_table.find('thead').find('tr')
            if header_row:
                th_cells = header_row.find_all('th')
                headers = [th.get_text(strip=True) for th in th_cells]
                if headers:
                    table_data.append(headers)
            
            # Extract data rows
            tbody = main_table.find('tbody')
            if tbody:
                rows = tbody.find_all('tr')
                for row in rows:
                    cells = row.find_all('td')
                    row_data = []
                    
                    for cell in cells:
                        # Get main text
                        cell_text = cell.get_text(separator=' ', strip=True)
                        cell_text = ' '.join(cell_text.split())
                        
                        # Check for info icon (might have additional info)
                        info_div = cell.find('div', class_='f6ee63')
                        if info_div:
                            cell_text = cell_text.replace(info_div.get_text(strip=True), '').strip()
                        
                        row_data.append(cell_text)
                    
                    if row_data:
                        table_data.append(row_data)
            
            pgp_placements_data["main_table"] = table_data
       
            # Show sample
            if len(table_data) > 1:
                print(f"  Sample row: {table_data[1]}")
        
        # Extract source information
        source_div = soup.find('div', class_='d4160c')
        if source_div:
            source_text = source_div.get_text(separator=' ', strip=True)
            source_text = ' '.join(source_text.split())
            pgp_placements_data["source_info"] = source_text
        
        comparison_div = soup.find('div', id='placement_section_placement_comparison')
        if comparison_div:
            comparison_table = comparison_div.find('table', class_='table f6a6c1 f866a4 dc8ace')
            if comparison_table:
                comparison_data = []
                
                # Extract headers
                comp_headers = []
                comp_header_row = comparison_table.find('thead').find('tr')
                if comp_header_row:
                    th_cells = comp_header_row.find_all('th')
                    comp_headers = [th.get_text(strip=True) for th in th_cells]
                    if comp_headers:
                        comparison_data.append(comp_headers)
                
                # Extract data rows
                comp_tbody = comparison_table.find('tbody')
                if comp_tbody:
                    rows = comp_tbody.find_all('tr')
                    for row in rows:
                        cells = row.find_all('td')
                        row_data = []
                        
                        for cell in cells:
                            cell_text = cell.get_text(separator=' ', strip=True)
                            cell_text = ' '.join(cell_text.split())
                            row_data.append(cell_text)
                        
                        if row_data:
                            comparison_data.append(row_data)
                
                pgp_placements_data["placement_comparison"] = comparison_data
               
                # Extract source note
                source_note = comparison_div.find('i', class_='da39de')
                if source_note:
                    pgp_placements_data["comparison_note"] = source_note.get_text(strip=True)
        
       
        fabm_section = soup.find('div', id='placement_section_class_profile')
        if fabm_section:
            fabm_data = {
                "title": "",
                "content": "",
                "table": []
            }
            
            # Extract FABM title
            fabm_title = fabm_section.find('div', class_='ae88c4')
            if fabm_title:
                fabm_data["title"] = fabm_title.get_text(strip=True)
            
            # Extract FABM content
            fabm_content = fabm_section.find('div', id='EdContent__placement_section_class_profile')
            if fabm_content:
                fabm_text = fabm_content.get_text(separator='\n', strip=True)
                fabm_data["content"] = fabm_text
                
                # Extract FABM table
                fabm_table = fabm_content.find('table')
                if fabm_table:
                    fabm_table_data = []
                    rows = fabm_table.find_all('tr')
                    
                    for row in rows:
                        cells = row.find_all(['th', 'td'])
                        row_data = [cell.get_text(separator=' ', strip=True) for cell in cells]
                        row_data = [' '.join(cell.split()) for cell in row_data]
                        if row_data:
                            fabm_table_data.append(row_data)
                    
                    fabm_data["table"] = fabm_table_data
            
            pgp_placements_data["pgp_fabm_data"] = fabm_data
          
        # Extract Placement rating
        rating_div = soup.find('div', class_='bdb2d9')
        if rating_div:
            rating_text = rating_div.get_text(strip=True)
            pgp_placements_data["placement_rating"] = rating_text
            
      
        faq_section = soup.find('div', id='sectional-faqs-0')
        if faq_section:
            faqs = []
            
            # Find all FAQ items
            faq_items = faq_section.find_all('div', class_='html-0')
            
            for faq_item in faq_items:
                try:
                    # Get question
                    question_elem = faq_item.find('strong', class_='flx-box')
                    if question_elem:
                        question_text = question_elem.get_text(strip=True)
                        # Clean question
                        import re
                        question_text = re.sub(r'^Q[:.]\s*', '', question_text).strip()
                        question_text = ' '.join(question_text.split())
                        
                        # Get answer
                        answer_container = faq_item.find_next('div', class_='f61835')
                        if answer_container:
                            # Try to find answer in wikkiContents
                            answer_div = answer_container.find('div', class_='wikkiContents')
                            if not answer_div:
                                answer_div = answer_container.find('div', class_='facb5f')
                            
                            if answer_div:
                                answer_text = answer_div.get_text(separator=' ', strip=True)
                                answer_text = re.sub(r'^A[:.]\s*', '', answer_text).strip()
                                answer_text = ' '.join(answer_text.split())
                                
                                # Extract tables from FAQ answers
                                faq_tables = []
                                tables_in_answer = answer_div.find_all('table')
                                
                                for table in tables_in_answer:
                                    table_data = []
                                    rows = table.find_all('tr')
                                    
                                    for row in rows:
                                        cells = row.find_all(['th', 'td'])
                                        row_data = [cell.get_text(separator=' ', strip=True) for cell in cells]
                                        row_data = [' '.join(cell.split()) for cell in row_data]
                                        if row_data:
                                            table_data.append(row_data)
                                    
                                    if table_data:
                                        faq_tables.append({
                                            "rows": len(table_data),
                                            "columns": len(table_data[0]) if table_data else 0,
                                            "data": table_data
                                        })
                                
                                if question_text and answer_text:
                                    faqs.append({
                                        "question": question_text,
                                        "answer": answer_text[:3000],  # Limit length
                                        "tables": faq_tables,
                                        "table_count": len(faq_tables)
                                    })
                except Exception as e:
                   
                    continue
            
            pgp_placements_data["faqs"] = faqs
         
        # Extract user feedback
        feedback_div = soup.find('div', class_='d79b7a')
        if feedback_div:
            feedback_text = feedback_div.get_text(separator=' ', strip=True)
            pgp_placements_data["user_feedback"] = feedback_text
        
        # Add to college_info
        if "placement_sections" not in college_info:
            college_info["placement_sections"] = {}
        
        college_info["placement_sections"]["pgp_placements"] = pgp_placements_data
        
        # Also add to main placement_data for backward compatibility
        if "placement_data" not in college_info:
            college_info["placement_data"] = {}
        
        # Add PGP table to main placement_data
        if pgp_placements_data.get("main_table"):
            if "tables" not in college_info["placement_data"]:
                college_info["placement_data"]["tables"] = []
            
            college_info["placement_data"]["tables"].append({
                "title": "PGP Placement Statistics 2023-2025",
                "data": pgp_placements_data["main_table"]
            })
        
        # Add FAQs to main placement_data
        if pgp_placements_data.get("faqs"):
            if "faqs" not in college_info["placement_data"]:
                college_info["placement_data"]["faqs"] = []
            
            college_info["placement_data"]["faqs"].extend(pgp_placements_data["faqs"])
    except Exception as e:
        
        import traceback
        traceback.print_exc()
        
        # Add empty section to avoid errors
        if "placement_sections" not in college_info:
            college_info["placement_sections"] = {}
        
        college_info["placement_sections"]["pgp_placements"] = {
            "title": "IIM Ahmedabad PGP Placements 2025",
            "intro_text": "",
            "main_table": [],
            "placement_comparison": [],
            "pgp_fabm_data": {},
            "faqs": [],
            "placement_rating": "",
            "source_info": "",
            "complete_content": "",
            "error": str(e)
        }

    return college_info

    


def scrape_cutoff(driver, URLS):
    try:
        driver.get(URLS["cutoff"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["cutoff"])

    wait = WebDriverWait(driver, 20)
    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
        "placement_data": {},
        "cutoff_data": {
            "qualifying_cutoff": {},
            "year_wise_cutoff": {},
            "college_comparison": [],
            "faqs": [],
            "description": []
        }
    }
    
    # ---------- COLLEGE HEADER ----------
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image
        try:
            top_header_section = driver.find_element(By.ID, "topHeaderCard-top-section")
            cover_img = top_header_section.find_element(By.ID, "topHeaderCard-gallery-image")
            college_info["cover_image"] = cover_img.get_attribute("src")
            
        except:
            pass
        
        # Extract logo
        try:
            logo_div = driver.find_element(By.CSS_SELECTOR, ".ca46d2.e014b3")
            logo_img = logo_div.find_element(By.TAG_NAME, "img")
            college_info["logo"] = logo_img.get_attribute("src")
         
        except:
            pass
        
        # Extract videos and photos count
        try:
            badges_div = driver.find_element(By.CSS_SELECTOR, ".e4df0b.ad160e")
            badges = badges_div.find_elements(By.CSS_SELECTOR, ".dcd631")
            
            for badge in badges:
                text = badge.text.lower()
                if "video" in text:
                    videos_match = re.search(r'(\d+)\s*videos?', text)
                    if videos_match:
                        college_info["videos_count"] = int(videos_match.group(1))
                elif "photo" in text:
                    photos_match = re.search(r'(\d+)\s*photos?', text)
                    if photos_match:
                        college_info["photos_count"] = int(photos_match.group(1))
        except:
            print("⚠️ Videos/Photos count not found")
        
        # Try to find college name from various selectors
        try:
            h1_elements = driver.find_elements(By.TAG_NAME, "h1")
            for h1 in h1_elements:
                if h1.text and ("Fees" in h1.text or "IIM" in h1.text):
                    college_info["college_name"] = h1.text.replace(" Fees", "").replace(" - Indian Institute of Management", "").strip()
                    break
        except:
            pass

        # Extract from the provided HTML structure
        try:
            header_section = driver.find_element(By.CSS_SELECTOR, ".a655da.aadf9d")
            
            # College name
            try:
                name_elem = header_section.find_element(By.CSS_SELECTOR, "h1.cc5e8d")
                college_info["college_name"] = name_elem.text.strip()
            except:
                pass
            
            # Location
            try:
                location_div = header_section.find_element(By.CSS_SELECTOR, ".de89cf")
                location_text = location_div.text.strip()
                if "," in location_text:
                    parts = [p.strip() for p in location_text.split(",", 1)]
                    college_info["location"] = parts[0].replace(",", "").strip()
                    college_info["city"] = parts[1] if len(parts) > 1 else ""
            except:
                pass
            
            # Rating and reviews
            try:
                rating_div = header_section.find_element(By.CSS_SELECTOR, ".e6f71f")
                rating_text = rating_div.text.strip()
                rating_match = re.search(r"(\d+\.\d+)\s*/\s*5", rating_text)
                if rating_match:
                    college_info["rating"] = rating_match.group(1)
                
                reviews_match = re.search(r"\((\d+)\s*Reviews", rating_text)
                if reviews_match:
                    college_info["reviews_count"] = int(reviews_match.group(1))
            except:
                pass
            
            # Q&A count
            try:
                qa_link = header_section.find_element(By.XPATH, ".//a[contains(text(), 'Student Q&A')]")
                qa_text = qa_link.text.strip()
                qa_match = re.search(r"(\d+(?:\.\d+)?)\s*(k|K)?", qa_text)
                if qa_match:
                    count = float(qa_match.group(1))
                    if qa_match.group(2):
                        count = int(count * 1000)
                    college_info["qa_count"] = int(count)
            except:
                pass
            
            # Institute type and established year
            try:
                list_items = header_section.find_elements(By.CSS_SELECTOR, ".ff9e36 li")
                for li in list_items:
                    text = li.text.strip().lower()
                    if "institute" in text:
                        college_info["institute_type"] = li.text.strip()
                    elif "estd" in text:
                        year_match = re.search(r"\b(\d{4})\b", li.text)
                        if year_match:
                            college_info["established_year"] = year_match.group(1)
            except:
                pass
                
        except Exception as e:
            print("⚠️ Error extracting header info: ")

    except Exception as e:
        print("⚠️ Error in college header section: ")
    
    # ---------- CUTOFF DATA SCRAPING ----------
    try:

        try:
            cutoff_section = wait.until(
                EC.presence_of_element_located((By.ID, "icop_section_exams"))
            )
            # Scroll into view to trigger JavaScript loading
            driver.execute_script("arguments[0].scrollIntoView(true);", cutoff_section)
            time.sleep(2)  # Wait for lazy loading
            
        except Exception as e:
            print("⚠️ Could not find cutoff section: ")
            return college_info
        
        
        try:
            # Wait for table to load with dynamic content
            time.sleep(3)
            
            # Try multiple strategies to find the qualifying cutoff table
            qualifying_table = None
            
            # Strategy 1: Look for table with specific class/id
            try:
                qualifying_table = driver.find_element(By.CSS_SELECTOR, "table.iima-table-id-7902")
               
            except:
                # Strategy 2: Look for table containing specific headers
                qualifying_tables = driver.find_elements(By.XPATH, "//table[.//th[contains(text(), 'VARC')] and .//th[contains(text(), 'DILR')] and .//th[contains(text(), 'QA')]]")
                if qualifying_tables:
                    qualifying_table = qualifying_tables[0]
                   
                else:
                    # Strategy 3: Look in the expanded qualifying cutoff section
                    try:
                        qualifying_section = driver.find_element(By.ID, "icop_section_latest_round_cutoff_327")
                        driver.execute_script("arguments[0].scrollIntoView(true);", qualifying_section)
                        time.sleep(2)
                        qualifying_tables = qualifying_section.find_elements(By.TAG_NAME, "table")
                        if qualifying_tables:
                            qualifying_table = qualifying_tables[0]
                           
                    except:
                        pass
            
            if qualifying_table:
                rows = qualifying_table.find_elements(By.TAG_NAME, "tr")
                
                # Skip header row
                for row in rows[1:]:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if len(cells) >= 5:
                        category = cells[0].text.strip()
                        if category:  # Only add if category is not empty
                            college_info["cutoff_data"]["qualifying_cutoff"][category] = {
                                "VARC": cells[1].text.strip(),
                                "DILR": cells[2].text.strip(),
                                "QA": cells[3].text.strip(),
                                "Overall": cells[4].text.strip()
                            }
                
    
            else:
                pass
               
        
        except Exception as e:
           
            import traceback
            traceback.print_exc()
        
        # 2. Scrape Year-wise Cutoff Tables
        try:
            # Scroll to trigger loading of year-wise tables
            year_wise_section = driver.find_element(By.ID, "icop_section_previous_year_cutoff_327")
            driver.execute_script("arguments[0].scrollIntoView(true);", year_wise_section)
            time.sleep(2)
            
            # Find all year-wise cutoff tables
            cutoff_tables = driver.find_elements(By.CSS_SELECTOR, ".table.a82bdd.f866a4.dc8ace")
          
            for table_index, table in enumerate(cutoff_tables):
                try:
                    # Get table headers to determine table type
                    thead = table.find_element(By.TAG_NAME, "thead")
                    header_row = thead.find_element(By.TAG_NAME, "tr")
                    headers = [th.text.strip() for th in header_row.find_elements(By.TAG_NAME, "th")]
                    
                    # Check if this is a year-wise cutoff table (has years as headers)
                    is_year_table = any(header.isdigit() and len(header) == 4 for header in headers)
                    
                    if is_year_table:
                        # Try to get the course name from the previous h5 element
                        try:
                            course_header = driver.execute_script("""
                                var table = arguments[0];
                                var prev = table.previousElementSibling;
                                while (prev && prev.tagName !== 'H5') {
                                    prev = prev.previousElementSibling;
                                }
                                return prev ? prev.textContent : '';
                            """, table)
                            course_name = course_header.strip()
                            # Clean up the course name
                            if "IIM Ahmedabad" in course_name:
                                course_name = course_name.split(" - IIM Ahmedabad")[0].strip()
                            if "CAT percentile Cutoff" in course_name:
                                course_name = course_name.split(": CAT percentile Cutoff")[0].strip()
                            if not course_name:
                                course_name = f"Course_{table_index + 1}"
                        except:
                            course_name = f"Course_{table_index + 1}"
                        
                        # Extract table data
                        rows_data = []
                        tbody = table.find_element(By.TAG_NAME, "tbody")
                        data_rows = tbody.find_elements(By.TAG_NAME, "tr")
                        
                        for row in data_rows:
                            cells = row.find_elements(By.TAG_NAME, "td")
                            if len(cells) > 0:
                                row_data = {
                                    "section": cells[0].text.strip(),
                                    "scores": {}
                                }
                                
                                # Map scores to years based on headers
                                for i in range(1, min(len(cells), len(headers))):
                                    year = headers[i]
                                    score = cells[i].text.strip()
                                    row_data["scores"][year] = score
                                
                                rows_data.append(row_data)
                        
                        if rows_data:
                            college_info["cutoff_data"]["year_wise_cutoff"][course_name] = {
                                "headers": headers,
                                "data": rows_data
                            }
                            print(f"  Added year-wise cutoff for: {course_name}")
                
                except Exception as e:
                    
                    continue
            
          
        except Exception as e:
            print("⚠️ Error scraping year-wise cutoff: ")
        
        # 3. Scrape College Comparison Table
        try:
            # Scroll to college comparison section
            comparison_section = driver.find_element(By.ID, "icop_section_college_comparison_327")
            driver.execute_script("arguments[0].scrollIntoView(true);", comparison_section)
            time.sleep(2)
            
            # Find college comparison table by looking for specific headers
            comparison_tables = driver.find_elements(By.XPATH, "//table[.//th[contains(text(), 'Colleges')] and .//th[contains(text(), 'Specialization')]]")
            
            if comparison_tables:
                comparison_table = comparison_tables[0]
                
                # Get table rows
                tbody = comparison_table.find_element(By.TAG_NAME, "tbody")
                data_rows = tbody.find_elements(By.TAG_NAME, "tr")
                
                for row in data_rows:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if len(cells) >= 3:
                        # Extract college name and link
                        college_cell = cells[0]
                        
                        # Find college name (look for link with blackLink class or f0581e class)
                        college_name = ""
                        college_link = ""
                        
                        try:
                            college_link_elem = college_cell.find_element(By.CSS_SELECTOR, "a.f0581e.blackLink")
                            college_name = college_link_elem.text.strip()
                            college_link = college_link_elem.get_attribute("href")
                        except:
                            try:
                                # Try other selectors
                                links = college_cell.find_elements(By.TAG_NAME, "a")
                                for link in links:
                                    if link.text.strip() and "compare" not in link.text.lower():
                                        college_name = link.text.strip()
                                        college_link = link.get_attribute("href")
                                        break
                            except:
                                # If no link, get text from the cell
                                college_name = college_cell.text.strip()
                                # Remove "Compare" text if present
                                if "\n" in college_name:
                                    college_name = college_name.split("\n")[0].strip()
                        
                        # Extract specialization
                        specialization = cells[1].text.strip() if len(cells) > 1 else ""
                        
                        # Extract cutoff (clean up the text)
                        cutoff_text = cells[2].text.strip() if len(cells) > 2 else ""
                        # Extract just the number if possible
                        cutoff_match = re.search(r'(\d+(?:\.\d+)?)', cutoff_text)
                        cutoff = cutoff_match.group(1) if cutoff_match else cutoff_text
                        
                        # Only add if we have college name
                        if college_name and college_name != "Compare":
                            college_info["cutoff_data"]["college_comparison"].append({
                                "college_name": college_name,
                                "college_link": college_link,
                                "specialization": specialization,
                                "cutoff": cutoff
                            })
                
                # Remove duplicates
                unique_comparisons = []
                seen = set()
                for comp in college_info["cutoff_data"]["college_comparison"]:
                    key = (comp["college_name"], comp["specialization"], comp["cutoff"])
                    if key not in seen:
                        seen.add(key)
                        unique_comparisons.append(comp)
                
                college_info["cutoff_data"]["college_comparison"] = unique_comparisons

            else:
                pass
        
        except Exception as e:
            print("⚠️ Error scraping college comparison: ")
        
        # 4. Scrape FAQ Questions
        try:
            # Scroll to FAQ section
            faq_sections = driver.find_elements(By.CLASS_NAME, "sectional-faqs")
            
            for faq_section in faq_sections:
                faq_items = faq_section.find_elements(By.CLASS_NAME, "html-0")
                
                for faq_item in faq_items:
                    try:
                        # Extract question text
                        strong_element = faq_item.find_element(By.TAG_NAME, "strong")
                        question_text = strong_element.text.strip()
                        
                        # Clean up the question text
                        if question_text:
                            # Remove extra whitespace and newlines
                            question_text = ' '.join(question_text.split())
                            # Remove extra "Q:" if present
                            if question_text.startswith("Q:"):
                                question_text = question_text[2:].strip()
                            college_info["cutoff_data"]["faqs"].append(question_text)
                    except:
                        continue
            
            # Remove duplicates
            college_info["cutoff_data"]["faqs"] = list(dict.fromkeys(college_info["cutoff_data"]["faqs"]))
          
        except Exception as e:
            print("⚠️ Error scraping FAQs: ")
        
        # 5. Scrape Description
        try:
            # Get cutoff description from wikiContents sections
            wiki_sections = driver.find_elements(By.CSS_SELECTOR, ".wikiContents.dfbe34, .wikiContents.a566c1")
            
            for wiki_section in wiki_sections:
                try:
                    paragraphs = wiki_section.find_elements(By.TAG_NAME, "p")
                    for p in paragraphs:
                        text = p.text.strip()
                        # Filter: only keep meaningful paragraphs
                        if text and len(text) > 20 and not text.startswith("A:") and not text.startswith("Q:"):
                            # Clean up text
                            text = ' '.join(text.split())
                            if text not in college_info["cutoff_data"]["description"]:
                                college_info["cutoff_data"]["description"].append(text)
                except:
                    continue
            
           
        except Exception as e:
            print("⚠️ Error scraping description: ")
    
    except Exception as e:
        print("⚠️ Error in cutoff data section: ")
        import traceback
        traceback.print_exc()
    
    return college_info

def scrape_ranking(driver, URLS):
    try:
        driver.get(URLS["ranking"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["ranking"])
    

    wait = WebDriverWait(driver, 40)  # Increased wait time
    
    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
    }
    

    time.sleep(7)  # Increased initial wait
    
    try:
        # Wait for specific elements to ensure page is loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.cc5e8d")))
        
    except:
        pass
    

    try:
        # Extract cover image
        try:
            cover_img = wait.until(EC.presence_of_element_located((By.ID, "topHeaderCard-gallery-image")))
            college_info["cover_image"] = cover_img.get_attribute("src")
            
        except:
            pass
        
        # Extract logo
        try:
            logo_img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ca46d2.e014b3 img")))
            college_info["logo"] = logo_img.get_attribute("src")
           
        except:
            pass
        
        # Extract college name - FIXED: Get proper college name
        try:
            # Try multiple selectors for college name
            selectors = [
                "h1.b16e25",  # Main title
                "h1.cc5e8d",  # Alternative title
                ".ab2e01 h1",  # Another alternative
                "h1"  # Any h1
            ]
            
            for selector in selectors:
                try:
                    elements = driver.find_elements(By.CSS_SELECTOR, selector)
                    for elem in elements:
                        text = elem.text.strip()
                        if text and "IIM" in text and "Ranking" not in text:
                            college_info["college_name"] = text
                            break
                    if college_info["college_name"]:
                        break
                except:
                    continue
            
            if not college_info["college_name"]:
                # Fallback to any h1
                h1_elements = driver.find_elements(By.TAG_NAME, "h1")
                for h1 in h1_elements:
                    text = h1.text.strip()
                    if text and "IIM" in text:
                        college_info["college_name"] = text.split("Ranking")[0].strip()
                        break
        except:
            pass
        
        # Extract videos and photos count - FIXED
        try:
            # Look for badges with video/photo counts
            badges = driver.find_elements(By.CSS_SELECTOR, ".dcd631")
            for badge in badges:
                text = badge.text.lower()
                if "video" in text:
                    # Extract number from text like "2 Videos"
                    match = re.search(r'(\d+)\s*videos?', text, re.IGNORECASE)
                    if match:
                        college_info["videos_count"] = int(match.group(1))
                elif "photo" in text:
                    match = re.search(r'(\d+)\s*photos?', text, re.IGNORECASE)
                    if match:
                        college_info["photos_count"] = int(match.group(1))
        except:
            pass
        
        # Extract location
        try:
            location_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".de89cf")))
            location_text = location_elem.text.strip()
            if "," in location_text:
                parts = [p.strip() for p in location_text.split(",", 1)]
                college_info["location"] = parts[0].replace(",", "").strip()
                college_info["city"] = parts[1] if len(parts) > 1 else ""
           
        except:
            pass
        
        # Extract rating and reviews
        try:
            rating_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".e6f71f")))
            rating_text = rating_div.text.strip()
            
            rating_match = re.search(r"(\d+\.\d+)\s*/\s*5", rating_text)
            if rating_match:
                college_info["rating"] = rating_match.group(1)
            
            reviews_match = re.search(r"\((\d+)\s*Reviews", rating_text)
            if reviews_match:
                college_info["reviews_count"] = int(reviews_match.group(1))
            

        except:
            pass
        
        # Extract Q&A count - FIXED
        try:
            # Look for Q&A links in the header
            qa_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'questions') or contains(text(), 'Q&A') or contains(text(), 'Student Q&A')]")
            for link in qa_links:
                text = link.text.strip()
                if "Q&A" in text or "Questions" in text:
                    # Extract number from text like "1.5k" or "1500"
                    match = re.search(r'([\d,\.]+(?:k|K)?)', text)
                    if match:
                        num_text = match.group(1).replace(',', '')
                        if 'k' in num_text.lower():
                            num = float(num_text.lower().replace('k', '')) * 1000
                            college_info["qa_count"] = int(num)
                        else:
                            college_info["qa_count"] = int(float(num_text))
                        break
        except:
            pass
        
        # Extract other details
        try:
            details_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ff9e36 li")))
            for li in details_list:
                text = li.text.strip().lower()
                if "institute" in text:
                    college_info["institute_type"] = li.text.strip()
                elif "estd" in text:
                    year_match = re.search(r"\b(\d{4})\b", li.text)
                    if year_match:
                        college_info["established_year"] = year_match.group(1)
            
  
        except:
            print("⚠️ Institute details not found")
            
    except Exception as e:
        print("⚠️ Error in college header section: ")
        import traceback
        traceback.print_exc()

    ranking_data = {
        "highlights": {"description": "", "rankings": []},
        "international_ranking": {"description": "", "qs_ranking": {}, "financial_times_ranking": {}},
        "nirf": {"description": "", "table_data": [], "comparison": [], "ranking_criteria": {}},
        "outlook": {"description": "", "table_data": [], "comparison": []},
        "business_today": {"table_data": [], "comparison": []},
        "qs_world": {"description": "", "rankings": {}, "comparison": [], "ranking_criteria": {}},
        "table_of_contents": []
    }
    

    try:
        # Use JavaScript to check for specific elements
        js_check = driver.execute_script("""
            return {
                hasToc: document.querySelector('#newTocSection') !== null,
                tocItems: document.querySelectorAll('#newTocSection li').length,
                hasInternationalRanking: document.querySelector('#rp_section_international_ranking') !== null,
                rankingSections: document.querySelectorAll('[id^="rp_section_"]').length
            };
        """)
     
    except Exception as e:
        print("⚠️ JavaScript check failed: ")
    
  
    try:
        # Scroll multiple times to trigger lazy loading
        for i in range(5):
            scroll_position = (i + 1) * 500
            driver.execute_script(f"window.scrollTo(0, {scroll_position});")
            time.sleep(1)
        
        # Scroll to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # Scroll back to top
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        
    except Exception as e:
        print("⚠️ Error during scrolling: ")
    
    # Helper function to expand all sections
    def expand_all_sections():
       
        try:
            # Find all "Read more" buttons
            read_more_buttons = driver.find_elements(By.XPATH, "//span[contains(text(), 'Read more')]")
            print(f"Found {len(read_more_buttons)} 'Read more' buttons")
            
            for button in read_more_buttons:
                try:
                    if button.is_displayed():
                        driver.execute_script("arguments[0].scrollIntoView(true);", button)
                        time.sleep(0.3)
                        driver.execute_script("arguments[0].click();", button)
                        time.sleep(0.5)
                except:
                    continue
            
            # Also click on accordion headers to expand
            accordions = driver.find_elements(By.CSS_SELECTOR, ".ad25e5")
            for accordion in accordions:
                try:
                    if "expanded" not in accordion.get_attribute("class"):
                        driver.execute_script("arguments[0].scrollIntoView(true);", accordion)
                        time.sleep(0.3)
                        driver.execute_script("arguments[0].click();", accordion)
                        time.sleep(0.5)
                except:
                    continue
                    
            return True
        except Exception as e:
            
            return False
    
    # Expand all sections first
    expand_all_sections()
    
    # 1. EXTRACT TABLE OF CONTENTS - COMPLETELY REWRITTEN
    print("\n1. Extracting Table of Contents...")
    try:
        # Use JavaScript to directly extract TOC items
        toc_items_js = driver.execute_script("""
            const tocSection = document.getElementById('newTocSection');
            if (!tocSection) return [];
            
            const items = [];
            const liElements = tocSection.querySelectorAll('li');
            
            liElements.forEach(li => {
                // Try to get text from anchor first, then from li
                const anchor = li.querySelector('a');
                let text = '';
                
                if (anchor) {
                    text = anchor.textContent.trim();
                } else {
                    text = li.textContent.trim();
                }
                
                // Clean up the text
                text = text.replace(/\\n/g, ' ').replace(/\\s+/g, ' ').trim();
                
                if (text && !items.includes(text)) {
                    items.push(text);
                }
            });
            
            return items;
        """)
        
        if toc_items_js:
            ranking_data["table_of_contents"] = toc_items_js
            
        else:
            
            try:
                toc_section = wait.until(EC.presence_of_element_located((By.ID, "newTocSection")))
                toc_items = toc_section.find_elements(By.CSS_SELECTOR, ".c27cda.newTocListV2 li, #newTocSection li")
                
                for item in toc_items:
                    try:
                        # Try to get text from anchor tag
                        try:
                            anchor = item.find_element(By.TAG_NAME, "a")
                            text = anchor.text.strip()
                        except:
                            text = item.text.strip()
                        
                        # Clean the text
                        if text:
                            text = ' '.join(text.split())
                            if text not in ranking_data["table_of_contents"]:
                                ranking_data["table_of_contents"].append(text)
                    except:
                        continue
              
            except Exception as e:
                print("⚠️ TOC extraction failed: ")
                
    except Exception as e:
        print("⚠️ TOC not found: ")
    
 
    try:
        highlights_section = wait.until(EC.presence_of_element_located((By.ID, "rp_section_highlights")))
        driver.execute_script("arguments[0].scrollIntoView(true);", highlights_section)
        time.sleep(2)
        
        # Expand if needed
        expand_all_sections()
        
        # Extract description
        try:
            description_elem = highlights_section.find_element(By.CSS_SELECTOR, ".wikiContents")
            ranking_data["highlights"]["description"] = description_elem.text.strip()
         
        except:
            pass
        
        # Extract ranking cards
        try:
            ranking_cards = highlights_section.find_elements(By.CSS_SELECTOR, ".f35625, .bc4a0d")
        
            
            for card in ranking_cards:
                try:
                    # Extract publisher from image alt text
                    publisher_img = card.find_element(By.TAG_NAME, "img")
                    publisher_alt = publisher_img.get_attribute("alt")
                    
                    # Map alt text to publisher name
                    publisher_map = {
                        "NIRF Icon": "NIRF",
                        "BT Icon": "Business Today",
                        "Outlook Icon": "Outlook",
                        "QS Icon": "QS"
                    }
                    publisher = publisher_map.get(publisher_alt, publisher_alt.replace(" Icon", ""))
                    
                    # Extract category
                    category_elem = card.find_element(By.CLASS_NAME, "f1495c")
                    category = category_elem.text.strip()
                    
                    # Extract year
                    year_elem = card.find_element(By.CLASS_NAME, "d8ca5d")
                    year_text = year_elem.text.strip()
                    
                    # Extract rank
                    rank_elem = card.find_element(By.CLASS_NAME, "a3ae6e")
                    rank = rank_elem.text.strip()
                    
                    # Extract highlight
                    highlight = ""
                    try:
                        highlight_elem = card.find_element(By.CLASS_NAME, "f4f104")
                        highlight = highlight_elem.text.strip().replace("->", "").replace("-&gt;", "").strip()
                    except:
                        pass
                    
                    ranking_data["highlights"]["rankings"].append({
                        "publisher": publisher,
                        "category": category,
                        "year": year_text,
                        "rank": rank,
                        "highlight": highlight
                    })
                    
                except Exception as card_error:
                    continue
                    
        except Exception as e:
            print("⚠️ Error extracting ranking cards: ")
            
    except Exception as e:
        print("⚠️ Error in highlights section: ")
   
    try:
        nirf_section = wait.until(EC.presence_of_element_located((By.ID, "rp_section_publishers_8")))
        driver.execute_script("arguments[0].scrollIntoView(true);", nirf_section)
        time.sleep(2)
        
        # Expand all "Read more" sections
        expand_all_sections()
        
        # Extract description
        try:
            nirf_content = nirf_section.find_element(By.CSS_SELECTOR, ".wikiContents")
            ranking_data["nirf"]["description"] = nirf_content.text.strip()
            print("✓ NIRF description extracted")
        except:
            pass
        
        # Extract table data
        try:
            nirf_table = nirf_section.find_element(By.CSS_SELECTOR, ".table")
            rows = nirf_table.find_elements(By.TAG_NAME, "tr")
            
            if len(rows) > 1:
                headers = []
                th_elements = rows[0].find_elements(By.TAG_NAME, "th")
                for th in th_elements:
                    headers.append(th.text.strip().lower().replace(" ", "_"))
                
                for row in rows[1:]:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if cells:
                        row_data = {}
                        for i, cell in enumerate(cells):
                            if i < len(headers):
                                row_data[headers[i]] = cell.text.strip()
                        ranking_data["nirf"]["table_data"].append(row_data)
                
                print("✓ NIRF table data extracted: {len(ranking_data['nirf']['table_data'])} rows")
        except Exception as e:
            print("⚠️ Error extracting NIRF table: ")
        
        # Extract comparison data
        try:
            # Find all tables in NIRF section
            all_tables = nirf_section.find_elements(By.TAG_NAME, "table")
            
            for table in all_tables:
                try:
                    rows = table.find_elements(By.TAG_NAME, "tr")
                    if len(rows) > 1:
                        # Check if this is a comparison table (has college names and ranks)
                        first_row_text = rows[1].text.lower()
                        if "iim" in first_row_text or "compare" in first_row_text:
                            for row in rows[1:]:
                                cells = row.find_elements(By.TAG_NAME, "td")
                                if len(cells) >= 2:
                                    college_name = cells[0].text.strip()
                                    # Clean college name
                                    college_name = re.sub(r'\nCompare$', '', college_name)
                                    college_name = re.sub(r'\s+Compare$', '', college_name)
                                    college_name = college_name.split('\n')[0].strip()
                                    rank = cells[1].text.strip()
                                    
                                    ranking_data["nirf"]["comparison"].append({
                                        "college": college_name,
                                        "rank": rank
                                    })

                            break
                except:
                    continue
                    
        except Exception as e:
            print("⚠️ Error extracting NIRF comparison: ")
            
        # Extract ranking criteria using JavaScript
        try:
            criteria_data = driver.execute_script("""
                const criteriaSection = arguments[0];
                const criteria = {};
                
                // Look for tables with ranking criteria
                const tables = criteriaSection.getElementsByTagName('table');
                
                for (let table of tables) {
                    const rows = table.getElementsByTagName('tr');
                    for (let i = 1; i < rows.length; i++) {
                        const cells = rows[i].getElementsByTagName('td');
                        if (cells.length >= 2) {
                            const criteriaName = cells[0].textContent.trim().toLowerCase().replace(/[^a-z0-9]/g, '_');
                            const score = cells[1].textContent.trim();
                            if (criteriaName && score) {
                                criteria[criteriaName] = score;
                            }
                        }
                    }
                }
                
                return criteria;
            """, nirf_section)
            
            if criteria_data:
                ranking_data["nirf"]["ranking_criteria"] = criteria_data
           
        except:
            ranking_data["nirf"]["ranking_criteria"] = {}
            
    except Exception as e:
        print("⚠️ Error in NIRF section: ")
    

    try:
        outlook_section = wait.until(EC.presence_of_element_located((By.ID, "rp_section_publishers_3")))
        driver.execute_script("arguments[0].scrollIntoView(true);", outlook_section)
        time.sleep(2)
        
        expand_all_sections()
        
        # Extract description
        try:
            outlook_content = outlook_section.find_element(By.CSS_SELECTOR, ".wikiContents")
            ranking_data["outlook"]["description"] = outlook_content.text.strip()
      
        except:
            pass
        
        # Extract table data
        try:
            outlook_table = outlook_section.find_element(By.CSS_SELECTOR, ".table")
            rows = outlook_table.find_elements(By.TAG_NAME, "tr")
            
            if len(rows) > 1:
                headers = []
                th_elements = rows[0].find_elements(By.TAG_NAME, "th")
                for th in th_elements:
                    headers.append(th.text.strip().lower().replace(" ", "_"))
                
                for row in rows[1:]:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if cells:
                        row_data = {}
                        for i, cell in enumerate(cells):
                            if i < len(headers):
                                row_data[headers[i]] = cell.text.strip()
                        ranking_data["outlook"]["table_data"].append(row_data)

        except Exception as e:
            print("⚠️ Error extracting Outlook table: ")
        
        # Extract comparison data
        try:
            comp_tables = outlook_section.find_elements(By.CSS_SELECTOR, ".table.f6a6c1, table")
            
            for table in comp_tables:
                try:
                    rows = table.find_elements(By.TAG_NAME, "tr")
                    if len(rows) > 1:
                        for row in rows[1:]:
                            cells = row.find_elements(By.TAG_NAME, "td")
                            if len(cells) >= 2:
                                college_name = cells[0].text.strip()
                                college_name = re.sub(r'\nCompare$', '', college_name)
                                college_name = re.sub(r'\s+Compare$', '', college_name)
                                college_name = college_name.split('\n')[0].strip()
                                rank = cells[1].text.strip()
                                
                                ranking_data["outlook"]["comparison"].append({
                                    "college": college_name,
                                    "rank": rank
                                })

                        break
                except:
                    continue
                    
        except Exception as e:
            print("⚠️ Error extracting Outlook comparison: ")
            
    except Exception as e:
        print("⚠️ Error in Outlook section: ")
    
   
    try:
        bt_section = wait.until(EC.presence_of_element_located((By.ID, "rp_section_publishers_2")))
        driver.execute_script("arguments[0].scrollIntoView(true);", bt_section)
        time.sleep(2)
        
        # Extract table data
        try:
            bt_table = bt_section.find_element(By.CSS_SELECTOR, ".table")
            rows = bt_table.find_elements(By.TAG_NAME, "tr")
            
            if len(rows) > 1:
                headers = []
                th_elements = rows[0].find_elements(By.TAG_NAME, "th")
                for th in th_elements:
                    headers.append(th.text.strip().lower().replace(" ", "_"))
                
                for row in rows[1:]:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if cells:
                        row_data = {}
                        for i, cell in enumerate(cells):
                            if i < len(headers):
                                row_data[headers[i]] = cell.text.strip()
                        ranking_data["business_today"]["table_data"].append(row_data)
        except Exception as e:
            print("⚠️ Error extracting Business Today table: ")
        
        # Extract comparison data
        try:
            comp_tables = bt_section.find_elements(By.CSS_SELECTOR, ".table.f6a6c1, table")
            
            for table in comp_tables:
                try:
                    rows = table.find_elements(By.TAG_NAME, "tr")
                    if len(rows) > 1:
                        for row in rows[1:]:
                            cells = row.find_elements(By.TAG_NAME, "td")
                            if len(cells) >= 2:
                                college_name = cells[0].text.strip()
                                college_name = re.sub(r'\nCompare$', '', college_name)
                                college_name = re.sub(r'\s+Compare$', '', college_name)
                                college_name = college_name.split('\n')[0].strip()
                                rank = cells[1].text.strip()
                                
                                ranking_data["business_today"]["comparison"].append({
                                    "college": college_name,
                                    "rank": rank
                                })

                        break
                except:
                    continue
                    
        except Exception as e:
            print("⚠️ Error extracting Business Today comparison: ")
            
    except Exception as e:
        print("⚠️ Error in Business Today section: ")
    

    try:
        qs_section = wait.until(EC.presence_of_element_located((By.ID, "rp_section_publishers_237")))
        driver.execute_script("arguments[0].scrollIntoView(true);", qs_section)
        time.sleep(2)
        
        expand_all_sections()
        
        # Extract description
        try:
            qs_content = qs_section.find_element(By.CSS_SELECTOR, ".wikiContents")
            ranking_data["qs_world"]["description"] = qs_content.text.strip()
          
            
            # Extract detailed QS ranking table using JavaScript
            try:
                qs_data = driver.execute_script("""
                    const section = arguments[0];
                    const rankings = {};
                    
                    // Find all tables in the section
                    const tables = section.getElementsByTagName('table');
                    
                    for (let table of tables) {
                        const rows = table.getElementsByTagName('tr');
                        let hasYears = false;
                        
                        // Check if this table has year columns
                        if (rows.length > 0) {
                            const firstRow = rows[0];
                            const cells = firstRow.getElementsByTagName('th');
                            let yearCount = 0;
                            
                            for (let cell of cells) {
                                const text = cell.textContent.trim();
                                if (/^\\d{4}$/.test(text)) {
                                    yearCount++;
                                }
                            }
                            
                            if (yearCount >= 3) {
                                hasYears = true;
                                
                                // Process data rows
                                for (let i = 1; i < rows.length; i++) {
                                    const rowCells = rows[i].getElementsByTagName('td');
                                    if (rowCells.length >= 4) {
                                        const category = rowCells[0].textContent.trim();
                                        if (category && category.toLowerCase() !== 'category') {
                                            rankings[category] = {
                                                "2022": rowCells[1].textContent.trim(),
                                                "2023": rowCells[2].textContent.trim(),
                                                "2024": rowCells[3].textContent.trim()
                                            };
                                        }
                                    }
                                }
                            }
                        }
                        
                        if (Object.keys(rankings).length > 0) {
                            break;
                        }
                    }
                    
                    return rankings;
                """, qs_section)
                
                if qs_data:
                    ranking_data["qs_world"]["rankings"] = qs_data
                 
            except Exception as table_error:
                print("⚠️ Error extracting QS detailed table: ")
                
        except Exception as e:
            print("⚠️ Error extracting QS description: ")
        
        # Extract comparison data using JavaScript
        try:
            comparison_data = driver.execute_script("""
                const section = arguments[0];
                const comparisons = [];
                
                // Look for comparison tables
                const tables = section.getElementsByTagName('table');
                
                for (let table of tables) {
                    const rows = table.getElementsByTagName('tr');
                    let isComparisonTable = false;
                    
                    // Check if this looks like a comparison table
                    if (rows.length > 1) {
                        const firstDataRow = rows[1];
                        const cells = firstDataRow.getElementsByTagName('td');
                        
                        if (cells.length >= 2) {
                            const collegeText = cells[0].textContent.toLowerCase();
                            if (collegeText.includes('iim') || collegeText.includes('compare')) {
                                isComparisonTable = true;
                            }
                        }
                    }
                    
                    if (isComparisonTable) {
                        for (let i = 1; i < rows.length; i++) {
                            const cells = rows[i].getElementsByTagName('td');
                            if (cells.length >= 2) {
                                let collegeName = cells[0].textContent.trim();
                                // Clean the name
                                collegeName = collegeName.replace(/\\nCompare$/i, '').trim();
                                collegeName = collegeName.split('\\n')[0].trim();
                                
                                const rank = cells[1].textContent.trim();
                                
                                comparisons.push({
                                    college: collegeName,
                                    rank: rank
                                });
                            }
                        }
                        break;
                    }
                }
                
                return comparisons;
            """, qs_section)
            
            if comparison_data:
                ranking_data["qs_world"]["comparison"] = comparison_data
              
        except Exception as e:
            print("⚠️ Error extracting QS comparison: ")
            
    except Exception as e:
        print("⚠️ Error in QS World section: ")
    

    try:
        intl_section = wait.until(EC.presence_of_element_located((By.ID, "rp_section_international_ranking")))
        driver.execute_script("arguments[0].scrollIntoView(true);", intl_section)
        time.sleep(3)  # Give extra time for loading
        
        # Expand the section
        expand_all_sections()
        
        # Extract content using JavaScript for reliability
        try:
            # Use JavaScript to extract everything from international ranking section
            intl_data = driver.execute_script("""
                const section = document.getElementById('rp_section_international_ranking');
                if (!section) return { description: '', qs_ranking: {}, financial_times_ranking: {} };
                
                // Get description
                const wikiContent = section.querySelector('.wikiContents');
                let description = '';
                if (wikiContent) {
                    description = wikiContent.textContent.trim();
                }
                
                // Initialize result objects
                const qsRanking = {};
                const ftRanking = {};
                
                // Find all tables
                const tables = section.getElementsByTagName('table');
                
                for (let table of tables) {
                    const rows = table.getElementsByTagName('tr');
                    let currentTableType = null;
                    
                    // Check header row to determine table type
                    if (rows.length > 0) {
                        const headerRow = rows[0];
                        const headerText = headerRow.textContent;
                        
                        if (headerText.includes('QS World Ranking') || 
                            headerText.includes('By Subject') || 
                            headerText.includes('Masters in Management')) {
                            currentTableType = 'qs';
                        } else if (headerText.includes('Financial Times') || 
                                  headerText.includes('MBA') || 
                                  headerText.includes('Executive Education')) {
                            currentTableType = 'ft';
                        }
                    }
                    
                    // Process data rows
                    for (let i = 1; i < rows.length; i++) {
                        const cells = rows[i].getElementsByTagName('td');
                        
                        if (cells.length >= 4) {
                            const category = cells[0].textContent.trim();
                            
                            // Skip empty or header rows
                            if (!category || category === 'Category' || category.includes('strong>')) {
                                continue;
                            }
                            
                            // Clean category name
                            const cleanCategory = category.replace(/^<strong>|<\/strong>$/g, '').trim();
                            
                            if (currentTableType === 'qs') {
                                qsRanking[cleanCategory] = {
                                    "2022": cells[1].textContent.trim(),
                                    "2023": cells[2].textContent.trim(),
                                    "2024": cells[3].textContent.trim()
                                };
                            } else if (currentTableType === 'ft') {
                                // Financial Times table has different year columns
                                ftRanking[cleanCategory] = {
                                    "2021": cells[1].textContent.trim(),
                                    "2022": cells[2].textContent.trim(),
                                    "2023": cells[3].textContent.trim()
                                };
                            }
                        }
                    }
                }
                
                return {
                    description: description,
                    qs_ranking: qsRanking,
                    financial_times_ranking: ftRanking
                };
            """)
            
            # Update ranking data with JavaScript results
            ranking_data["international_ranking"]["description"] = intl_data.get("description", "")
            ranking_data["international_ranking"]["qs_ranking"] = intl_data.get("qs_ranking", {})
            ranking_data["international_ranking"]["financial_times_ranking"] = intl_data.get("financial_times_ranking", {})
            
   
        except Exception as e:
            print("⚠️ Error extracting international content with JavaScript: ")
            
            # Fallback to Python extraction
            try:
                intl_content = intl_section.find_element(By.CSS_SELECTOR, ".wikiContents")
                ranking_data["international_ranking"]["description"] = intl_content.text.strip()
              
                # Try to extract tables with Python
                try:
                    tables = intl_content.find_elements(By.TAG_NAME, "table")
                    current_table_type = None
                    
                    for table in tables:
                        table_text = table.text
                        
                        # Determine table type
                        if "QS World Ranking" in table_text:
                            current_table_type = "qs"
                        elif "Financial Times Ranking" in table_text:
                            current_table_type = "ft"
                        
                        # Process rows
                        rows = table.find_elements(By.TAG_NAME, "tr")
                        for row in rows:
                            cells = row.find_elements(By.TAG_NAME, "td")
                            if len(cells) >= 4:
                                category = cells[0].text.strip()
                                if category and category.lower() not in ["category", ""]:
                                    if current_table_type == "qs":
                                        ranking_data["international_ranking"]["qs_ranking"][category] = {
                                            "2022": cells[1].text.strip(),
                                            "2023": cells[2].text.strip(),
                                            "2024": cells[3].text.strip()
                                        }
                                    elif current_table_type == "ft":
                                        ranking_data["international_ranking"]["financial_times_ranking"][category] = {
                                            "2021": cells[1].text.strip(),
                                            "2022": cells[2].text.strip(),
                                            "2023": cells[3].text.strip()
                                        }
                except Exception as table_error:
                    print("⚠️ Error extracting tables: {table_error}")
                    
            except Exception as fallback_error:
                print("⚠️ Fallback extraction failed: {fallback_error}")
            
    except Exception as e:
        print("⚠️ Error in International ranking section: ")
        import traceback
        traceback.print_exc()
    
    # Add ranking data to college_info
    college_info["ranking_data"] = ranking_data
    
 
    return college_info



def scrape_mini_clips(driver, URLS):
    try:
        driver.get(URLS["gallery"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["gallery"])
    

    wait = WebDriverWait(driver, 20)
    
    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
        "gallery_data": {
            "table_of_contents": [],
            "campus_infrastructure": {
                "images": [],
                "videos": []
            },
            "lab_library_academic": {
                "images": [],
                "videos": []
            },
            "mini_clips": [],
            "hostel_sports": {
                "images": [],
                "videos": []
            },
            "reviews": []
        }
    }
    

    time.sleep(5)
    
    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
       
    except:
        pass
    
    # ---------- COLLEGE HEADER ----------

    try:
        # Extract cover image
        try:
            cover_img = wait.until(EC.presence_of_element_located((By.ID, "topHeaderCard-gallery-image")))
            college_info["cover_image"] = cover_img.get_attribute("src")
            
        except:
            pass
        
        # Extract logo
        try:
            logo_img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ca46d2.e014b3 img")))
            college_info["logo"] = logo_img.get_attribute("src")
           
        except:
            pass
        
        # Extract college name
        try:
            college_name_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.cc5e8d")))
            college_info["college_name"] = college_name_elem.text.strip()
         
        except:
            pass
        
        # Extract location
        try:
            location_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".de89cf")))
            location_text = location_elem.text.strip()
            if "," in location_text:
                parts = [p.strip() for p in location_text.split(",", 1)]
                college_info["location"] = parts[0].replace(",", "").strip()
                college_info["city"] = parts[1] if len(parts) > 1 else ""
           
        except:
            pass
        
        # Extract rating and reviews
        try:
            rating_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".e6f71f")))
            rating_text = rating_div.text.strip()
            
            rating_match = re.search(r"(\d+\.\d+)\s*/\s*5", rating_text)
            if rating_match:
                college_info["rating"] = rating_match.group(1)
            
            reviews_match = re.search(r"\((\d+)\s*Reviews", rating_text)
            if reviews_match:
                college_info["reviews_count"] = int(reviews_match.group(1))
            

        except:
            pass
        
        # Extract other details
        try:
            details_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ff9e36 li")))
            for li in details_list:
                text = li.text.strip().lower()
                if "institute" in text:
                    college_info["institute_type"] = li.text.strip()
                elif "estd" in text:
                    year_match = re.search(r"\b(\d{4})\b", li.text)
                    if year_match:
                        college_info["established_year"] = year_match.group(1)
            
           
        except:
            pass
            
    except Exception as e:
        print(" Error in college header section: ")
    
    # ---------- GALLERY DATA SCRAPING ----------
    print("\n" + "="*50)
    print("EXTRACTING GALLERY DATA...")
    print("="*50)
    
    # Scroll to load all content
    print("Scrolling to load all content...")
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # Scroll back to top
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    
    # 1. EXTRACT TABLE OF CONTENTS
    print("\n1. Extracting Table of Contents...")
    try:
        # Use JavaScript to extract TOC items
        toc_items_js = driver.execute_script("""
            const tocSection = document.getElementById('newTocSection');
            if (!tocSection) return [];
            
            const items = [];
            const tocList = tocSection.querySelector('.c27cda.newTocListV2');
            
            if (tocList) {
                const liElements = tocList.querySelectorAll('li');
                liElements.forEach(li => {
                    let text = '';
                    // Try to get text from data-scrol attribute or text content
                    const dataScrol = li.getAttribute('data-scrol');
                    if (dataScrol) {
                        text = dataScrol.replace(/_/g, ' ').replace(/([A-Z])/g, ' $1').trim();
                    } else {
                        text = li.textContent.trim();
                    }
                    
                    if (text && !items.includes(text)) {
                        items.push(text);
                    }
                });
            }
            return items;
        """)
        
        if toc_items_js:
            college_info["gallery_data"]["table_of_contents"] = toc_items_js
            print(f"✓ Found {len(toc_items_js)} TOC items")
        else:
            print("⚠️ TOC not found")
            
    except Exception as e:
        print(" Error extracting TOC: ")
    
    # 2. EXTRACT CAMPUS & INFRASTRUCTURE IMAGES
    print("\n2. Extracting Campus & Infrastructure Images...")
    try:
        campus_section = driver.find_element(By.ID, "gallery_section_campus_infra")
        
        # Extract all image items using JavaScript
        campus_data = driver.execute_script("""
            const section = arguments[0];
            const result = { images: [], videos: [] };
            
            // Find all image containers
            const imageContainers = section.querySelectorAll('.e81df3.baa7c9');
            
            imageContainers.forEach(container => {
                // Get the image element
                const imgElement = container.querySelector('img.ef4ec7');
                const titleElement = container.querySelector('.aeb7cc');
                
                if (imgElement && titleElement) {
                    const imgUrl = imgElement.getAttribute('src');
                    const title = titleElement.textContent.trim();
                    
                    // Check if it's a YouTube video (contains i.ytimg.com)
                    if (imgUrl && imgUrl.includes('i.ytimg.com')) {
                        // Extract YouTube video ID from URL
                        let videoId = '';
                        if (imgUrl.includes('/vi/')) {
                            const match = imgUrl.match(/\/vi\/([^\/]+)/);
                            videoId = match ? match[1] : '';
                        }
                        
                        if (videoId) {
                            const videoData = {
                                title: title,
                                thumbnail_url: imgUrl,
                                video_url: `https://www.youtube.com/watch?v=${videoId}`,
                                youtube_id: videoId,
                                type: 'video'
                            };
                            result.videos.push(videoData);
                        }
                    } else if (imgUrl) {
                        // It's a regular image
                        const imageData = {
                            title: title,
                            image_url: imgUrl,
                            type: 'image'
                        };
                        result.images.push(imageData);
                    }
                }
            });
            
            return result;
        """, campus_section)
        
        if campus_data:
            college_info["gallery_data"]["campus_infrastructure"]["images"] = campus_data.get("images", [])
            college_info["gallery_data"]["campus_infrastructure"]["videos"] = campus_data.get("videos", [])
            
            print(f"✓ Found {len(campus_data['images'])} campus images")
            print(f"✓ Found {len(campus_data['videos'])} campus videos")
            
    except Exception as e:
        print(" Error extracting campus infrastructure: ")
    
    # 3. EXTRACT MINI CLIPS
    print("\n3. Extracting Mini Clips...")
    try:
        # Find mini clips section (reels widget)
        mini_clips_data = driver.execute_script("""
            const result = [];
            
            // Look for all mini clips containers
            const clipsContainers = document.querySelectorAll('#reelsWidget, [data-corouselkeyname]');
            
            clipsContainers.forEach(container => {
                // Find all clip items
                const clipItems = container.querySelectorAll('.d87173.thumbnailListener, [data-corouselkeyid]');
                
                clipItems.forEach(item => {
                    try {
                        const dataId = item.getAttribute('data-corouselkeyid');
                        const dataName = item.getAttribute('data-corouselkeyname');
                        const dataIndex = item.getAttribute('data-index');
                        
                        // Find thumbnail image
                        const thumbnailImg = item.querySelector('img.f69743');
                        const thumbnailUrl = thumbnailImg ? thumbnailImg.getAttribute('src') : '';
                        
                        // Find video iframe
                        const iframe = item.querySelector('iframe');
                        let videoUrl = '';
                        let youtubeId = '';
                        
                        if (iframe) {
                            videoUrl = iframe.getAttribute('src') || '';
                            // Extract YouTube ID from iframe src
                            if (videoUrl.includes('youtube.com/embed/')) {
                                const match = videoUrl.match(/embed\/([^?]+)/);
                                youtubeId = match ? match[1] : '';
                            }
                        }
                        
                        // Find title
                        const titleElement = item.querySelector('.ada2b9, .e6852b');
                        const title = titleElement ? titleElement.textContent.trim() : '';
                        
                        // Find duration
                        const durationElement = item.querySelector('.e6852b');
                        const duration = durationElement ? durationElement.textContent.trim() : '';
                        
                        const clipData = {
                            id: dataId,
                            name: dataName,
                            index: dataIndex,
                            title: title,
                            duration: duration,
                            thumbnail_url: thumbnailUrl,
                            video_url: youtubeId ? `https://www.youtube.com/watch?v=${youtubeId}` : '',
                            youtube_id: youtubeId,
                            iframe_url: videoUrl
                        };
                        
                        // Only add if we have valid data
                        if (title || thumbnailUrl || youtubeId) {
                            result.push(clipData);
                        }
                    } catch (err) {
                        console.error('Error processing clip item:', err);
                    }
                });
            });
            
            return result;
        """)
        
        if mini_clips_data:
            college_info["gallery_data"]["mini_clips"] = mini_clips_data
            print(f"✓ Found {len(mini_clips_data)} mini clips")
            
    except Exception as e:
        print(" Error extracting mini clips: ")
    
    # 4. EXTRACT ALL GALLERY SECTIONS DYNAMICALLY
    print("\n4. Extracting All Gallery Sections...")
    try:
        # Get all gallery sections
        gallery_sections = driver.execute_script("""
            const sections = [];
            const gallerySections = document.querySelectorAll('[id^="gallery_section_"]');
            
            gallerySections.forEach(section => {
                const sectionId = section.id;
                const titleElement = section.querySelector('.ae88c4');
                const sectionTitle = titleElement ? titleElement.textContent.trim() : '';
                
                // Get all images and videos in this section
                const mediaItems = [];
                const imageElements = section.querySelectorAll('img.ef4ec7');
                
                imageElements.forEach(img => {
                    const imgUrl = img.getAttribute('src');
                    const title = img.getAttribute('title') || '';
                    
                    // Find parent container for title
                    const parentLi = img.closest('.e81df3');
                    if (parentLi) {
                        const titleDiv = parentLi.querySelector('.aeb7cc');
                        const finalTitle = titleDiv ? titleDiv.textContent.trim() : title;
                        
                        // Check if it's YouTube (video) or regular image
                        if (imgUrl && imgUrl.includes('i.ytimg.com')) {
                            // Extract YouTube ID
                            let youtubeId = '';
                            if (imgUrl.includes('/vi/')) {
                                const match = imgUrl.match(/\/vi\/([^\/]+)/);
                                youtubeId = match ? match[1] : '';
                            }
                            
                            mediaItems.push({
                                type: 'video',
                                title: finalTitle,
                                thumbnail_url: imgUrl,
                                youtube_id: youtubeId,
                                video_url: youtubeId ? `https://www.youtube.com/watch?v=${youtubeId}` : '',
                                source_url: imgUrl
                            });
                        } else if (imgUrl) {
                            mediaItems.push({
                                type: 'image',
                                title: finalTitle,
                                image_url: imgUrl,
                                source_url: imgUrl
                            });
                        }
                    }
                });
                
                sections.push({
                    id: sectionId,
                    title: sectionTitle,
                    media_count: mediaItems.length,
                    media_items: mediaItems
                });
            });
            
            return sections;
        """)
        
        if gallery_sections:
            # Organize sections by their IDs
            for section in gallery_sections:
                section_id = section["id"]
                media_items = section.get("media_items", [])
                
                # Categorize based on section ID
                if "campus_infra" in section_id:
                    # Separate images and videos for campus infrastructure
                    images = [item for item in media_items if item.get("type") == "image"]
                    videos = [item for item in media_items if item.get("type") == "video"]
                    college_info["gallery_data"]["campus_infrastructure"]["images"].extend(images)
                    college_info["gallery_data"]["campus_infrastructure"]["videos"].extend(videos)
                    
                elif "academic_facilities" in section_id:
                    # For lab/library/academic facilities
                    images = [item for item in media_items if item.get("type") == "image"]
                    videos = [item for item in media_items if item.get("type") == "video"]
                    college_info["gallery_data"]["lab_library_academic"]["images"].extend(images)
                    college_info["gallery_data"]["lab_library_academic"]["videos"].extend(videos)
                    
                elif "hostel_sports" in section_id:
                    # For hostel & sports
                    images = [item for item in media_items if item.get("type") == "image"]
                    videos = [item for item in media_items if item.get("type") == "video"]
                    college_info["gallery_data"]["hostel_sports"]["images"].extend(images)
                    college_info["gallery_data"]["hostel_sports"]["videos"].extend(videos)
                    
                elif "mini_clips" in section_id:
                    # For mini clips (though we already extracted them separately)
                    college_info["gallery_data"]["mini_clips"].extend(media_items)
                    
                elif "reviews" in section_id:
                    # For reviews
                    college_info["gallery_data"]["reviews"].extend(media_items)
            
            print(f"✓ Processed {len(gallery_sections)} gallery sections")
            
    except Exception as e:
        print(" Error extracting all gallery sections: ")
    
    # 5. EXTRACT ADDITIONAL MEDIA FROM ALL SECTIONS
    print("\n5. Extracting Additional Media from All Sections...")
    try:
        # Extract all media from the entire page
        all_media = driver.execute_script("""
            const allMedia = {
                images: [],
                videos: [],
                youtube_links: []
            };
            
            // Find all images with src
            const allImages = document.querySelectorAll('img[src]');
            allImages.forEach(img => {
                const src = img.getAttribute('src');
                const alt = img.getAttribute('alt') || '';
                const title = img.getAttribute('title') || '';
                
                if (src) {
                    // Check if it's a YouTube thumbnail
                    if (src.includes('i.ytimg.com') || src.includes('youtube.com')) {
                        // Extract YouTube ID if possible
                        let youtubeId = '';
                        if (src.includes('/vi/')) {
                            const match = src.match(/\/vi\/([^\/]+)/);
                            youtubeId = match ? match[1] : '';
                        }
                        
                        allMedia.videos.push({
                            type: 'youtube_thumbnail',
                            url: src,
                            alt: alt,
                            title: title,
                            youtube_id: youtubeId,
                            video_url: youtubeId ? `https://www.youtube.com/watch?v=${youtubeId}` : ''
                        });
                    } else if (src.includes('.jpg') || src.includes('.jpeg') || src.includes('.png') || src.includes('.gif')) {
                        // Regular image
                        allMedia.images.push({
                            url: src,
                            alt: alt,
                            title: title
                        });
                    }
                }
            });
            
            // Find all iframes (YouTube videos)
            const allIframes = document.querySelectorAll('iframe[src*="youtube.com"]');
            allIframes.forEach(iframe => {
                const src = iframe.getAttribute('src');
                const title = iframe.getAttribute('title') || '';
                
                if (src) {
                    // Extract YouTube ID
                    let youtubeId = '';
                    if (src.includes('embed/')) {
                        const match = src.match(/embed\/([^?]+)/);
                        youtubeId = match ? match[1] : '';
                    } else if (src.includes('youtu.be/')) {
                        const match = src.match(/youtu\.be\/([^?]+)/);
                        youtubeId = match ? match[1] : '';
                    }
                    
                    if (youtubeId) {
                        allMedia.youtube_links.push({
                            iframe_src: src,
                            title: title,
                            youtube_id: youtubeId,
                            watch_url: `https://www.youtube.com/watch?v=${youtubeId}`
                        });
                    }
                }
            });
            
            return allMedia;
        """)
        
        # Update counts in college_info
        if all_media:
            college_info["videos_count"] = len(all_media.get("videos", [])) + len(all_media.get("youtube_links", []))
            college_info["photos_count"] = len(all_media.get("images", []))
            

            
    except Exception as e:
        print("Error extracting additional media")
    
    
    return college_info


def scrape_hostel_campus_js(driver, URLS):
    try:
        driver.get(URLS["infrastructure"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["infrastructure"])
    
    wait = WebDriverWait(driver, 25)
    time.sleep(5)  # allow JS to load
    soup = BeautifulSoup(driver.page_source, "html.parser")

    college_info = {
        "college_name": None,
        "cover_image": None,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "author_name": "",
        "update_on": "",
        "campus_content": {
            "overview": {"text": "", "images": []},
            "highlights": [],
            "hostel": {"description": "", "facilities": [], "fee_tables": [], "images": []},
            "library": {"description": "", "images": []},
            "sports": {"description": "", "images": []},
            "places_nearby": [],
            "videos": []
        },
        "infrastructure_section": {},  # Added for infrastructure section data
        "reviews": []  # Added for reviews section
    }
    
    # Extract author name
    name = soup.find("div", class_="adp_usr_dtls")
    if name:
        n = name.find("a").text.strip()
        college_info["author_name"] = n
    
    # Extract update date
    update = soup.find("div", class_="post-date")
    if update:
        update_on = update.text.strip()
        college_info["update_on"] = update_on
    
    # ================= 1. SCRAPE REVIEW SECTIONS =================
    try:
        print("Scraping review sections...")
        
        # Find all review sections
        review_sections = soup.find_all('section', class_='review-card')
        
        reviews_data = []
        
        for review_section in review_sections:
            review_data = {}
            
            # Extract review ID
            review_id = review_section.get('id', '')
            if review_id:
                review_data["review_id"] = review_id
            
            # Extract user information
            user_info_box = review_section.find('div', class_='rvw-usr-info')
            if user_info_box:
                # User name
                user_name_elem = user_info_box.find('span', class_='black')
                if user_name_elem:
                    review_data["user_name"] = user_name_elem.text.strip()
                
                # User batch/course
                user_info_text = user_info_box.text
                if 'Batch of' in user_info_text:
                    batch_part = user_info_text.split('Batch of')[-1].split(')')[0] + ')'
                    review_data["batch"] = 'Batch of ' + batch_part.strip()
                
                # Review date
                date_elem = user_info_box.find('div', class_='rvw-date')
                if date_elem:
                    review_data["review_date"] = date_elem.text.replace('Reviewed on', '').strip()
            
            # Check if verified
            verified_tag = review_section.find('span', class_='rvw-verified-tag')
            if verified_tag:
                review_data["verified"] = True
            else:
                review_data["verified"] = False
            
            # Extract overall rating
            rating_block = review_section.find('span', class_='rating-block')
            if rating_block:
                rating_text = rating_block.text.strip()
                review_data["overall_rating"] = rating_text
            
            # Extract category ratings
            category_ratings = {}
            rating_spans = review_section.find_all('span', class_=False)
            for span in rating_spans:
                span_text = span.text.strip()
                if 'Placements' in span_text:
                    category_ratings["placements"] = span_text.replace('Placements', '').strip()
                elif 'Infrastructure' in span_text:
                    category_ratings["infrastructure"] = span_text.replace('Infrastructure', '').strip()
                elif 'Faculty' in span_text:
                    category_ratings["faculty_course"] = span_text.replace('Faculty & Course Curriculum', '').strip()
                elif 'Crowd' in span_text:
                    category_ratings["campus_life"] = span_text.replace('Crowd & Campus Life', '').strip()
                elif 'Value' in span_text:
                    category_ratings["value_for_money"] = span_text.replace('Value for Money', '').strip()
            
            if category_ratings:
                review_data["category_ratings"] = category_ratings
            
            # Extract review content
            content_box = review_section.find('div', class_='rvw-content')
            if content_box:
                # Review heading
                heading = content_box.find('strong', class_='rvw-heading')
                if heading:
                    review_data["review_heading"] = heading.text.strip()
                
                # Review text
                desc_spans = content_box.find_all('span', class_='desc-sp')
                review_text_parts = []
                
                for desc_span in desc_spans:
                    review_text_parts.append(desc_span.text.strip())
                
                # Also check for paragraphs
                paragraphs = content_box.find_all('p')
                for p in paragraphs:
                    if p.text.strip() and not p.find('strong'):
                        review_text_parts.append(p.text.strip())
                
                if review_text_parts:
                    review_data["review_text"] = ' '.join(review_text_parts)
            
            # Extract helpfulness data (if available)
            helpful_box = review_section.find('div', class_='hlful-box')
            if helpful_box:
                helpful_text = helpful_box.text
                if 'Yes' in helpful_text or 'No' in helpful_text:
                    review_data["has_helpful_option"] = True
            
            # Add review to list if it has content
            if review_data.get("review_text") or review_data.get("review_heading"):
                reviews_data.append(review_data)
        
        college_info["reviews"] = reviews_data
        print(f"Found {len(reviews_data)} reviews")
        
    except Exception as e:
        print(f"Error scraping reviews: ")
        college_info["reviews"] = []
    
    # ================= 2. SCRAPE INFRASTRUCTURE SECTION FROM HTML =================
    try:
        print("Scraping infrastructure section...")
        
        # Find infrastructure section
        infrastructure_section = soup.find('section', {'id': 'infrastructureSection'})
        if not infrastructure_section:
            infrastructure_section = soup.find('div', class_='infrastructureSection')
        
        if infrastructure_section:
            infrastructure_data = {}
            
            # Parse all infrastructure items
            infra_items = infrastructure_section.find_all('li')
            
            for item in infra_items:
                # Get icon and title
                icon_div = item.find('div', class_='icn')
                if icon_div:
                    icon_text = icon_div.find('strong').text.strip() if icon_div.find('strong') else ""
                    details_div = item.find('div', class_='dtl')
                    
                    if icon_text == "Library":
                        # Library information
                        if details_div:
                            p_text = details_div.find('p')
                            if p_text:
                                infrastructure_data["library"] = {
                                    "description": p_text.text.strip(),
                                    "collections": {
                                        "books": "1,94,704+",
                                        "journals": "19,815 online, 146 print",
                                        "databases": "71 databases"
                                    }
                                }
                    
                    elif icon_text == "Cafeteria":
                        # Cafeteria information
                        if details_div:
                            p_text = details_div.find('p')
                            if p_text:
                                infrastructure_data["cafeteria"] = {
                                    "description": p_text.text.strip(),
                                    "outlets": ["TANSTAAFL CAFE", "Food King", "Coffee Express"]
                                }
                    
                    elif icon_text == "Hostel":
                        # Hostel information
                        if details_div:
                            p_text = details_div.find('p')
                            if p_text:
                                infrastructure_data["hostel"] = {
                                    "description": p_text.text.strip()
                                }
                            
                            # Parse hostel details
                            child_facility = details_div.find('div', class_='childFaciltyBox')
                            if child_facility:
                                hostel_details = {
                                    "boys_hostel": {
                                        "occupancy": ["Single Occupancy", "Shared Rooms"],
                                        "location": "In-Campus Hostel"
                                    },
                                    "girls_hostel": {
                                        "occupancy": ["Single Occupancy", "Shared Rooms"],
                                        "location": "In-Campus Hostel"
                                    },
                                    "total_dormitories": 25,
                                    "capacity": "740 occupants",
                                    "facilities": ["Telephone", "TV", "Washing Machine", "Refrigerator", 
                                                 "Vegetarian & Non-vegetarian meals"]
                                }
                                infrastructure_data["hostel"]["details"] = hostel_details
                    
                    elif icon_text == "Sports Complex":
                        # Sports facilities
                        if details_div:
                            child_facility = details_div.find('div', class_='childFaciltyBox')
                            if child_facility:
                                facilities = []
                                spans = child_facility.find_all('span')
                                for span in spans:
                                    text = span.text.strip()
                                    if text and text != '|' and not text.startswith('Available'):
                                        facilities.append(text)
                                
                                infrastructure_data["sports"] = {
                                    "facilities": facilities,
                                    "description": "Available Facilities: " + ", ".join(facilities)
                                }
                    
                    elif icon_text == "Labs":
                        # Lab facilities
                        if details_div:
                            child_facility = details_div.find('div', class_='childFaciltyBox')
                            if child_facility:
                                facilities = []
                                spans = child_facility.find_all('span')
                                for span in spans:
                                    text = span.text.strip()
                                    if text and text != '|' and not text.startswith('Available'):
                                        facilities.append(text)
                                
                                infrastructure_data["labs"] = {
                                    "facilities": facilities,
                                    "description": "Available Facilities: " + ", ".join(facilities)
                                }
            
            # Parse basic facilities (wrapFlx class items)
            wrap_flx_item = infrastructure_section.find('li', class_='wrapFlx')
            if wrap_flx_item:
                basic_facilities = []
                icn_divs = wrap_flx_item.find_all('div', class_='icn')
                for icn in icn_divs:
                    facility_name = icn.find('strong')
                    if facility_name:
                        basic_facilities.append(facility_name.text.strip())
                
                infrastructure_data["basic_facilities"] = basic_facilities
            
            # Parse other facilities section
            other_facility_box = infrastructure_section.find('div', class_='otherFacilityBox')
            if other_facility_box:
                other_facilities = []
                itm_spans = other_facility_box.find_all('span', class_='itm')
                for span in itm_spans:
                    other_facilities.append(span.text.strip())
                
                infrastructure_data["other_facilities"] = other_facilities
            
            # Add infrastructure data to college_info
            college_info["infrastructure_section"] = infrastructure_data
            print(f"Infrastructure section scraped: {len(infrastructure_data)} items")
    
    except Exception as e:
        print(f"Error scraping infrastructure section: ")
    
    # ================= 3. USE JS TO SCRAPE OTHER CONTENT =================
    js_result = driver.execute_script("""
        // Create result object
        const result = {
            campus_content: {
                overview: { text: "", images: [] },
                highlights: [],
                hostel: { description: "", facilities: [], fee_tables: [], images: [] },
                library: { description: "", images: [] },
                sports: { description: "", images: [] },
                places_nearby: [],
                videos: []
            }
        };
        
        console.log('Starting campus information scraping...');
        
        // ================= 1. Find main content container =================
        const mainContainer = document.querySelector('.wikkiContents.faqAccordian, .abtSection');
        const sourceHTML = mainContainer ? mainContainer.innerHTML : document.body.innerHTML;
        
        // ================= 2. Parse campus overview =================
        try {
            // More precise search for overview paragraph
            const firstP = document.querySelector('.abtSection p');
            if (firstP && firstP.textContent.includes('IIM Ahmedabad Campus')) {
                result.campus_content.overview.text = firstP.textContent.trim();
                console.log('Found campus overview text');
            }
        } catch(e) { console.log('Overview parsing error:', e); }
        
        // ================= 3. Parse campus highlights =================
        try {
            // Find h2 tags containing "Highlights"
            const highlightsHeaders = document.querySelectorAll('h2');
            highlightsHeaders.forEach(header => {
                if (header.textContent.includes('Campus Highlights')) {
                    console.log('Found campus highlights title');
                    
                    // Find ul tag after this h2
                    let nextElem = header.nextElementSibling;
                    while (nextElem) {
                        if (nextElem.tagName === 'UL') {
                            const items = nextElem.querySelectorAll('li');
                            items.forEach(item => {
                                result.campus_content.highlights.push(item.textContent.trim());
                            });
                            console.log('Found highlights count:', result.campus_content.highlights.length);
                            break;
                        }
                        nextElem = nextElem.nextElementSibling;
                    }
                }
            });
        } catch(e) { console.log('Highlights parsing error:', e); }
        
        // ================= 4. Parse hostel information =================
        try {
            // Find hostel titles
            const hostelHeaders = document.querySelectorAll('h2, h3');
            let foundHostelSection = false;
            
            hostelHeaders.forEach(header => {
                const headerText = header.textContent.trim();
                
                if (headerText.includes('IIM Ahemdabad Hostel') || 
                    headerText.includes('Hostel Facilities') ||
                    headerText.includes('Hostel Fee')) {
                    
                    console.log('Found hostel related title:', headerText);
                    
                    // Get description - first paragraph
                    if (headerText.includes('IIM Ahemdabad Hostel') && !foundHostelSection) {
                        foundHostelSection = true;
                        let nextElem = header.nextElementSibling;
                        let descriptionText = '';
                        
                        // Collect paragraphs until next h3 or h2
                        while (nextElem && 
                               nextElem.tagName !== 'H2' && 
                               nextElem.tagName !== 'H3' && 
                               !nextElem.textContent.includes('Facilities')) {
                            if (nextElem.tagName === 'P') {
                                descriptionText += nextElem.textContent.trim() + ' ';
                            }
                            nextElem = nextElem.nextElementSibling;
                        }
                        
                        result.campus_content.hostel.description = descriptionText.trim();
                        console.log('Hostel description length:', result.campus_content.hostel.description.length);
                    }
                    
                    // Get facilities list
                    if (headerText.includes('Hostel Facilities')) {
                        let nextElem = header.nextElementSibling;
                        while (nextElem) {
                            if (nextElem.tagName === 'UL') {
                                const items = nextElem.querySelectorAll('li');
                                items.forEach(item => {
                                    result.campus_content.hostel.facilities.push(item.textContent.trim());
                                });
                                console.log('Found hostel facilities count:', result.campus_content.hostel.facilities.length);
                                break;
                            }
                            nextElem = nextElem.nextElementSibling;
                        }
                    }
                }
            });
        } catch(e) { console.log('Hostel parsing error:', e); }
        
        // ================= 5. Parse library information =================
        try {
            const libraryHeaders = document.querySelectorAll('h2');
            libraryHeaders.forEach(header => {
                if (header.textContent.includes('IIM Ahmedabad Library')) {
                    console.log('Found library title');
                    
                    // Get description
                    let nextElem = header.nextElementSibling;
                    while (nextElem && nextElem.tagName === 'P') {
                        const text = nextElem.textContent.trim();
                        if (text.length > 50) {
                            result.campus_content.library.description = text;
                            break;
                        }
                        nextElem = nextElem.nextElementSibling;
                    }
                }
            });
        } catch(e) { console.log('Library parsing error:', e); }
        
        // ================= 6. Parse sports facilities =================
        try {
            const sportsHeaders = document.querySelectorAll('h2');
            sportsHeaders.forEach(header => {
                if (header.textContent.includes('Sports Facilities')) {
                    console.log('Found sports facilities title');
                    
                    // Get description
                    let nextElem = header.nextElementSibling;
                    while (nextElem && nextElem.tagName === 'P') {
                        result.campus_content.sports.description += nextElem.textContent.trim() + ' ';
                        nextElem = nextElem.nextElementSibling;
                    }
                    result.campus_content.sports.description = result.campus_content.sports.description.trim();
                }
            });
        } catch(e) { console.log('Sports facilities parsing error:', e); }
        
        // ================= 7. Parse nearby places =================
        try {
            const placesHeaders = document.querySelectorAll('h2');
            placesHeaders.forEach(header => {
                if (header.textContent.includes('Places to visit')) {
                    console.log('Found nearby places title');
                    
                    // Find ul tag
                    let nextElem = header.nextElementSibling;
                    while (nextElem) {
                        if (nextElem.tagName === 'UL') {
                            const items = nextElem.querySelectorAll('li');
                            items.forEach(item => {
                                result.campus_content.places_nearby.push(item.textContent.trim());
                            });
                            console.log('Found nearby places count:', result.campus_content.places_nearby.length);
                            break;
                        }
                        nextElem = nextElem.nextElementSibling;
                    }
                }
            });
        } catch(e) { console.log('Nearby places parsing error:', e); }
        
        // ================= 8. Parse all images =================
        try {
            console.log('Starting image parsing...');
            
            // Method 1: Find all image tags
            const allImages = document.querySelectorAll('img');
            console.log('Total image tags:', allImages.length);
            
            // Method 2: Find all picture tags
            const allPictures = document.querySelectorAll('picture');
            console.log('Picture tags count:', allPictures.length);
            
            // Store real image URLs
            const realImageUrls = new Set();
            
            // First process high-quality images in picture tags
            allPictures.forEach(picture => {
                // Find source tags
                const sources = picture.querySelectorAll('source');
                sources.forEach(source => {
                    const srcset = source.getAttribute('data-originalset') || 
                                   source.getAttribute('srcset');
                    if (srcset && srcset.includes('shiksha.com')) {
                        // Extract first URL
                        const urls = srcset.split(',')[0].split(' ')[0];
                        if (urls.includes('.jpeg') || urls.includes('.jpg')) {
                            realImageUrls.add(urls.trim());
                        }
                    }
                });
                
                // Find img tags
                const imgs = picture.querySelectorAll('img');
                imgs.forEach(img => {
                    const src = img.src;
                    const dataSrc = img.getAttribute('data-src');
                    
                    if (src && src.includes('shiksha.com') && 
                        (src.includes('.jpeg') || src.includes('.jpg'))) {
                        realImageUrls.add(src);
                    }
                    if (dataSrc && dataSrc.includes('shiksha.com') && 
                        (dataSrc.includes('.jpeg') || dataSrc.includes('.jpg'))) {
                        realImageUrls.add(dataSrc);
                    }
                });
            });
            
            // Then process regular img tags
            allImages.forEach(img => {
                const src = img.src;
                const dataSrc = img.getAttribute('data-src');
                const classAttr = img.className || '';
                
                // Filter out tracking links and small images
                if (src && src.includes('shiksha.com') && 
                    !src.includes('tracking') && 
                    !src.includes('gateway') &&
                    !classAttr.includes('default') &&
                    (src.includes('.jpeg') || src.includes('.jpg'))) {
                    
                    // Filter out thumbnails (containing dimensions)
                    if (!src.includes('_100x') && !src.includes('_205x') && !src.includes('_480x')) {
                        realImageUrls.add(src);
                    }
                }
                
                if (dataSrc && dataSrc.includes('shiksha.com') && 
                    !dataSrc.includes('tracking') &&
                    (dataSrc.includes('.jpeg') || dataSrc.includes('.jpg'))) {
                    realImageUrls.add(dataSrc);
                }
            });
            
            console.log('Found real image URLs:', realImageUrls.size);
            
            // Classify images
            const imageUrls = Array.from(realImageUrls);
            
            // Classify based on URL ID (from HTML)
            imageUrls.forEach(url => {
                if (url.includes('1694510359')) { // Library image
                    result.campus_content.library.images.push(url);
                } else if (url.includes('1694510611')) { // Hostel image
                    result.campus_content.hostel.images.push(url);
                } else if (url.includes('1694510577')) { // Possibly another library image
                    result.campus_content.library.images.push(url);
                } else if (url.includes('1694510411') || 
                          url.includes('1694510438') || 
                          url.includes('1694510489')) { // Sports facilities images
                    result.campus_content.sports.images.push(url);
                } else if (url.includes('library') || url.includes('Library')) {
                    result.campus_content.library.images.push(url);
                } else if (url.includes('hostel') || url.includes('Hostel') || url.includes('dorm')) {
                    result.campus_content.hostel.images.push(url);
                } else if (url.includes('sports') || url.includes('Sports') || 
                          url.includes('gym') || url.includes('Gym') || 
                          url.includes('court') || url.includes('Court')) {
                    result.campus_content.sports.images.push(url);
                } else {
                    // Default to overview
                    result.campus_content.overview.images.push(url);
                }
            });
            
            console.log('Image classification result:');
            console.log('- Library images:', result.campus_content.library.images.length);
            console.log('- Hostel images:', result.campus_content.hostel.images.length);
            console.log('- Sports images:', result.campus_content.sports.images.length);
            console.log('- Overview images:', result.campus_content.overview.images.length);
            
        } catch(e) { console.log('Image parsing error:', e); }
        
        // ================= 9. Parse all videos =================
        try {
            const allIframes = document.querySelectorAll('iframe');
            allIframes.forEach(iframe => {
                const src = iframe.src;
                if (src && src.includes('youtube.com')) {
                    const match = src.match(/embed\\/([a-zA-Z0-9_-]+)/);
                    if (match) {
                        const videoId = match[1];
                        if (!result.campus_content.videos.includes(videoId)) {
                            result.campus_content.videos.push(videoId);
                        }
                    }
                }
            });
            
            console.log('Found videos count:', result.campus_content.videos.length);
        } catch(e) { console.log('Video parsing error:', e); }
        
        // ================= 10. Parse fee tables =================
        try {
            const allTables = document.querySelectorAll('table');
            console.log('Total tables found:', allTables.length);
            
            allTables.forEach((table, index) => {
                const tableText = table.textContent.toLowerCase();
                
                // Check if it's a fee-related table
                if (tableText.includes('fee') || 
                    tableText.includes('deposit') || 
                    tableText.includes('component') ||
                    tableText.includes('inr') ||
                    tableText.includes('hostel')) {
                    
                    const tableData = [];
                    const rows = table.querySelectorAll('tr');
                    
                    rows.forEach(row => {
                        const rowData = [];
                        const cells = row.querySelectorAll('th, td');
                        
                        cells.forEach(cell => {
                            const cellText = cell.textContent.trim();
                            // Clean line breaks and extra spaces
                            const cleanText = cellText.replace(/\\s+/g, ' ').replace(/\\n/g, ' ').trim();
                            if (cleanText) {
                                rowData.push(cleanText);
                            }
                        });
                        
                        if (rowData.length > 0) {
                            tableData.push(rowData);
                        }
                    });
                    
                    if (tableData.length >= 2) { // At least header row and data row
                        result.campus_content.hostel.fee_tables.push({
                            table_index: index,
                            data: tableData
                        });
                    }
                }
            });
            
            console.log('Fee tables count:', result.campus_content.hostel.fee_tables.length);
            
        } catch(e) { console.log('Table parsing error:', e); }
        
        // ================= 11. Get header information =================
        try {
            // College name from header
            const h1Element = document.querySelector('h1.inst-name');
            if (h1Element) {
                result.college_name = h1Element.textContent.split(',')[0].trim();
            }
            
            // Cover image from header
            const headerImg = document.querySelector('.header_img.desktop img');
            if (headerImg) {
                result.cover_image = headerImg.src;
            }
            
            // Rating
            const ratingElement = document.querySelector('.rating-block');
            if (ratingElement) {
                result.rating = ratingElement.textContent.trim();
            }
            
            // Reviews count
            const reviewsElement = document.querySelector('.view_rvws');
            if (reviewsElement) {
                const match = reviewsElement.textContent.match(/(\\d+)/);
                if (match) {
                    result.reviews_count = parseInt(match[1]);
                }
            }
            
            // Location
            const locationElement = document.querySelector('.ilp-loc span');
            if (locationElement) {
                const parts = locationElement.textContent.split(',').map(p => p.trim());
                result.location = parts[0];
                if (parts.length > 1) result.city = parts[1];
            }
            
        } catch(e) { console.log('Header information parsing error:', e); }
        
        console.log('Scraping completed!');
        console.log('=== Scraping Result Summary ===');
        console.log('Facilities count:', result.campus_content.highlights.length);
        console.log('Hostel facilities count:', result.campus_content.hostel.facilities.length);
        console.log('Library images count:', result.campus_content.library.images.length);
        console.log('Sports images count:', result.campus_content.sports.images.length);
        
        return result;
    """)
    
    # ================= 4. MERGE JS SCRAPING RESULTS =================
    if js_result:
        # Update header information
        if js_result.get('college_name'):
            college_info['college_name'] = js_result['college_name']
        if js_result.get('cover_image'):
            college_info['cover_image'] = js_result['cover_image']
        if js_result.get('rating'):
            college_info['rating'] = js_result['rating']
        if js_result.get('reviews_count'):
            college_info['reviews_count'] = js_result['reviews_count']
        if js_result.get('location'):
            college_info['location'] = js_result['location']
        if js_result.get('city'):
            college_info['city'] = js_result['city']
        
        # Update campus content
        if js_result.get('campus_content'):
            campus_data = js_result['campus_content']
            
            # Overview
            if campus_data['overview']['text']:
                college_info['campus_content']['overview']['text'] = campus_data['overview']['text']
            if campus_data['overview']['images']:
                college_info['campus_content']['overview']['images'] = campus_data['overview']['images']
            
            # Highlights
            if campus_data['highlights']:
                college_info['campus_content']['highlights'] = campus_data['highlights']
            
            # Hostel
            if campus_data['hostel']['description']:
                college_info['campus_content']['hostel']['description'] = campus_data['hostel']['description']
            if campus_data['hostel']['facilities']:
                college_info['campus_content']['hostel']['facilities'] = campus_data['hostel']['facilities']
            if campus_data['hostel']['fee_tables']:
                college_info['campus_content']['hostel']['fee_tables'] = campus_data['hostel']['fee_tables']
            if campus_data['hostel']['images']:
                college_info['campus_content']['hostel']['images'] = campus_data['hostel']['images']
            
            # Library
            if campus_data['library']['description']:
                college_info['campus_content']['library']['description'] = campus_data['library']['description']
            if campus_data['library']['images']:
                college_info['campus_content']['library']['images'] = campus_data['library']['images']
            
            # Sports
            if campus_data['sports']['description']:
                college_info['campus_content']['sports']['description'] = campus_data['sports']['description']
            if campus_data['sports']['images']:
                college_info['campus_content']['sports']['images'] = campus_data['sports']['images']
            
            # Places nearby
            if campus_data['places_nearby']:
                college_info['campus_content']['places_nearby'] = campus_data['places_nearby']
            
            # Videos
            if campus_data['videos']:
                college_info['campus_content']['videos'] = campus_data['videos']
    
    # ================= 5. FALLBACK: DIRECT HTML PARSING =================
    if not college_info['campus_content']['hostel']['facilities']:
        print("JS scraping didn't get hostel facilities, using fallback parsing...")
        try:
            page_html = driver.page_source
            
            # Directly parse hostel facilities from HTML
            import re
            
            # Find ul after "Hostel Facilities"
            facilities_pattern = r'Hostel Facilities.*?<ul>(.*?)</ul>'
            facilities_match = re.search(facilities_pattern, page_html, re.DOTALL | re.IGNORECASE)
            
            if facilities_match:
                ul_content = facilities_match.group(1)
                facilities_items = re.findall(r'<li>(.*?)</li>', ul_content)
                college_info['campus_content']['hostel']['facilities'] = [item.strip() for item in facilities_items]
                print(f"Fallback parsing found hostel facilities: {len(facilities_items)} items")
            
            # Find real image URLs
            picture_patterns = [
                r'data-originalset="(https://images\\.shiksha\\.com/mediadata/images/articles/.*?\\.jpeg)"',
                r'src="(https://images\\.shiksha\\.com/mediadata/images/articles/.*?\\.jpeg)"'
            ]
            
            all_image_urls = []
            for pattern in picture_patterns:
                matches = re.findall(pattern, page_html)
                all_image_urls.extend(matches)
            
            # Remove duplicates
            all_image_urls = list(set(all_image_urls))
            
            # Classify images
            for img_url in all_image_urls:
                if '1694510359' in img_url:  # Library image
                    college_info['campus_content']['library']['images'].append(img_url)
                elif '1694510611' in img_url:  # Hostel image
                    college_info['campus_content']['hostel']['images'].append(img_url)
                elif '1694510411' in img_url or '1694510438' in img_url or '1694510489' in img_url:  # Sports images
                    college_info['campus_content']['sports']['images'].append(img_url)
            
        except Exception as e:
            print(f"Fallback parsing error: ")
    
    # ================= 6. ENHANCE WITH INFRASTRUCTURE SECTION DATA =================
    # If infrastructure section has better data, use it to enhance existing data
    if college_info.get("infrastructure_section"):
        infra_data = college_info["infrastructure_section"]
        
        # Enhance hostel information
        if infra_data.get("hostel") and infra_data["hostel"].get("description"):
            if not college_info["campus_content"]["hostel"]["description"] or \
               len(infra_data["hostel"]["description"]) > len(college_info["campus_content"]["hostel"]["description"]):
                college_info["campus_content"]["hostel"]["description"] = infra_data["hostel"]["description"]
        
        # Enhance library information
        if infra_data.get("library") and infra_data["library"].get("description"):
            college_info["campus_content"]["library"]["description"] = infra_data["library"]["description"]
        
        # Enhance sports information
        if infra_data.get("sports") and infra_data["sports"].get("description"):
            college_info["campus_content"]["sports"]["description"] = infra_data["sports"]["description"]
    
    return college_info


def parse_faculty_full_html(driver,URLS):
    try:
        driver.get(URLS["faculty"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["faculty"])
    wait = WebDriverWait(driver, 15)

    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
    }
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image from pwa-headerwrapper
        try:
            header_wrapper = driver.find_element(By.CLASS_NAME, "pwa-headerwrapper")
            cover_img = header_wrapper.find_element(By.CSS_SELECTOR, ".header_img.desktop img")
            college_info["cover_image"] = cover_img.get_attribute("src")
            print(f"✓ Cover image found: {college_info['cover_image']}")
        except Exception as e:
            print(" Cover image not found: ")
        
        # Extract college name
        try:
            h1_element = driver.find_element(By.CSS_SELECTOR, "h1.inst-name.h2")
            full_text = h1_element.text.strip()
            # Clean the college name - remove "Faculty Details & Reviews" and location
            college_name = full_text.split("Faculty Details & Reviews")[0].strip()
            college_info["college_name"] = college_name
            print(f"✓ College name found: {college_info['college_name']}")
        except Exception as e:
            print(" College name not found: ")
        
        # Extract location and city
        try:
            location_element = driver.find_element(By.CSS_SELECTOR, ".ilp-loc.white-space-nowrap")
            location_text = location_element.text.strip()
            
            # Extract Vastrapur and Ahmedabad
            parts = location_text.split(", ")
            if len(parts) >= 1:
                # First part is Vastrapur
                college_info["location"] = parts[0].strip()
            
            if len(parts) >= 2:
                # Second part contains Ahmedabad (might be inside a link)
                city_part = parts[1]
                # Remove any HTML tags or links
                city_part = re.sub(r'<[^>]+>', '', city_part)
                college_info["city"] = city_part.strip()
            
            print(f"✓ Location found: {college_info['location']}, {college_info['city']}")
        except Exception as e:
            print(" Location not found: ")
        
        # Extract rating
        try:
            rating_element = driver.find_element(By.CSS_SELECTOR, ".rating-block.rvw-lyr")
            rating_text = rating_element.text.strip()
            # Extract just the numeric rating (e.g., "4.6" from "4.6" with stars)
            rating_match = re.search(r'(\d+\.\d+)', rating_text)
            if rating_match:
                college_info["rating"] = rating_match.group(1)
                print(f"✓ Rating found: {college_info['rating']}")
        except Exception as e:
            print(" Rating not found: ")
        
        # Extract reviews count
        try:
            reviews_link = driver.find_element(By.CSS_SELECTOR, "a.view_rvws.ripple.dark")
            reviews_text = reviews_link.text.strip()
            # Extract number from text like "(136 Reviews)"
            reviews_match = re.search(r'\((\d+)\s*Reviews', reviews_text)
            if reviews_match:
                college_info["reviews_count"] = int(reviews_match.group(1))
                print(f"✓ Reviews count found: {college_info['reviews_count']}")
        except Exception as e:
            print(" Reviews count not found: ")
        
        # Extract Q&A count
        try:
            qa_element = driver.find_element(By.CSS_SELECTOR, ".qna_student a")
            qa_text = qa_element.text.strip()
            # Extract number from text like "1.5k Student Q&A"
            qa_match = re.search(r'(\d+(?:\.\d+)?)\s*(k|K)?', qa_text)
            if qa_match:
                count = float(qa_match.group(1))
                if qa_match.group(2):  # If has 'k' suffix
                    count *= 1000
                college_info["qa_count"] = int(count)
                print(f"✓ Q&A count found: {college_info['qa_count']}")
        except Exception as e:
            print(" Q&A count not found: ")
        
        # Extract institute type (if available)
        try:
            # Look for institute type in other parts of the page
            institute_type_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Institute Type') or contains(text(), 'Type:')]")
            for elem in institute_type_elements:
                text = elem.text.strip()
                if "Institute Type" in text or "Type:" in text:
                    college_info["institute_type"] = text.split(":")[-1].strip() if ":" in text else text
                    print(f"✓ Institute type found: {college_info['institute_type']}")
                    break
        except Exception as e:
            print(" Institute type not found: ")
        
        # Extract established year (if available)
        try:
            # Look for established year in other parts of the page
            estd_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Established') or contains(text(), 'Estd') or contains(text(), 'Founded')]")
            for elem in estd_elements:
                text = elem.text.strip()
                # Look for year pattern
                year_match = re.search(r'\b(19|20)\d{2}\b', text)
                if year_match:
                    college_info["established_year"] = year_match.group()
                    print(f"✓ Established year found: {college_info['established_year']}")
                    break
        except Exception as e:
            print(" Established year not found: ")
        
        # Extract videos and photos count (from different parts of page)
        try:
            # Look for videos count
            video_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'video') or contains(text(), 'Video')]")
            for elem in video_elements:
                text = elem.text.lower()
                if "video" in text:
                    video_match = re.search(r'(\d+)\s*videos?', text)
                    if video_match:
                        college_info["videos_count"] = int(video_match.group(1))
                        print(f"✓ Videos count found: {college_info['videos_count']}")
                        break
        except Exception as e:
            print(" Videos count not found: ")
        
        try:
            # Look for photos count
            photo_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'photo') or contains(text(), 'Photo') or contains(text(), 'image') or contains(text(), 'Image')]")
            for elem in photo_elements:
                text = elem.text.lower()
                if "photo" in text or "image" in text:
                    photo_match = re.search(r'(\d+)\s*(photos?|images?)', text)
                    if photo_match:
                        college_info["photos_count"] = int(photo_match.group(1))
                        print(f"✓ Photos count found: {college_info['photos_count']}")
                        break
        except Exception as e:
            print(" Photos count not found: ")
        
        # Extract logo (if available)
        try:
            # Look for logo in different parts
            logo_elements = driver.find_elements(By.TAG_NAME, "img")
            for img in logo_elements:
                src = img.get_attribute("src") or ""
                alt = img.get_attribute("alt") or ""
                if ("logo" in src.lower() or "logo" in alt.lower()) and "shiksha.com" in src:
                    college_info["logo"] = src
                    print(f"✓ Logo found: {college_info['logo']}")
                    break
        except Exception as e:
            print(" Logo not found: ")

    except Exception as e:
        print(" Error in college header section: ")
    driver.get(URLS["faculty"])
    wait = WebDriverWait(driver, 15)

    # section = wait.until(
    #     EC.presence_of_element_located(
    #         (By.CSS_SELECTOR, "div.wikkiContents.faqAccordian")
    #     )
    # )
    try:
        section = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,"div.wikkiContents.faqAccordian")
            )
        )
    except:
        print("⚠️ parse_faculty_full_html not available, skipping")
        return None

    # 🔥 Scroll for lazy content
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", section
    )
    time.sleep(2)

    html = driver.execute_script(
        "return arguments[0].innerHTML;", section
    )

    soup = BeautifulSoup(html, "html.parser")

    data = {
        "author": {
            "name": "",
            "profile_url": "",
            "verified": False
        },
        "last_updated": "",
        "description": "",
        "faculty": []
    }

    # ✅ Author details
    author_tag = soup.select_one(".adp_usr_dtls a")
    if author_tag:
        data["author"]["name"] = author_tag.get_text(strip=True)
        data["author"]["profile_url"] = author_tag.get("href", "")
        data["author"]["verified"] = bool(author_tag.select_one(".tickIcon"))

    # ✅ Updated date
    date_tag = soup.select_one(".post-date")
    if date_tag:
        data["last_updated"] = (
            date_tag.get_text(strip=True)
            .replace("Updated on", "")
            .strip()
        )

    # ✅ Full description (first <p>)
    desc_p = soup.select_one(".abtSection p")
    if desc_p:
        data["description"] = desc_p.get_text(" ", strip=True)

    # ✅ Faculty table (FULL SAFE PARSE)
    table = soup.select_one(".abtSection table")
    if table:
        rows = table.find_all("tr")

        for row in rows[1:]:  # skip header
            cols = row.find_all("td")
            if len(cols) < 2:
                continue

            faculty_name = cols[0].get_text(" ", strip=True)

            qualifications = []
            for item in cols[1].select("p"):
                text = item.get_text(" ", strip=True)
                if text:
                    qualifications.append(text)

            data["faculty"].append({
                "faculty_name": faculty_name,
                "qualifications": qualifications
            })

    return {"college_info":college_info,"data":data}

def parse_faculty_reviews(driver,URLS):
    try:
        driver.get(URLS["faculty"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["faculty"])
    wait = WebDriverWait(driver, 15)

    section = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Faculty Reviews')]/ancestor::section")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", section
    )
    time.sleep(0.5)

    html = driver.execute_script(
        "return arguments[0].innerHTML;", section
    )

    soup = BeautifulSoup(html, "html.parser")

    data = {
        "overall_rating": "",
        "rating_out_of": "5",
        "based_on_reviews": "",
        "rating_distribution": [],
        "verified_reviews_info": ""
    }

    # ✅ Overall rating
    rating_tag = soup.select_one(".rvwScore h3")
    if rating_tag:
        data["overall_rating"] = rating_tag.get_text(strip=True)

    # ✅ Based on reviews count
    based_tag = soup.select_one(".refrnceTxt span")
    if based_tag:
        data["based_on_reviews"] = based_tag.get_text(strip=True)

    # ✅ Rating distribution (4-5, 3-4, etc.)
    for bar in soup.select(".starBar"):
        label_tag = bar.select_one(".starC a")
        percent_tag = bar.select_one(".starPrgrs")
        fill_tag = bar.select_one(".fillBar")

        data["rating_distribution"].append({
            "rating_range": label_tag.get_text(strip=True) if label_tag else "",
            "percentage_text": percent_tag.get_text(strip=True) if percent_tag else "",
            "percentage_width": fill_tag["style"].replace("width:", "").replace(";", "").strip()
            if fill_tag and fill_tag.has_attr("style") else ""
        })

    # ✅ Verified reviews description text
    verified_info = soup.select_one(".getAllrvws")
    if verified_info:
        data["verified_reviews_info"] = verified_info.get_text(" ", strip=True)

    return data

def parse_review_summarisation_all_tabs(driver,URLS):
    try:
        driver.get(URLS["faculty"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["faculty"])
    
    wait = WebDriverWait(driver, 15)


    try:
        section = wait.until(
            EC.presence_of_element_located(
                (By.ID, "ReviewSummarisationReviewSummary")
            )
        )
    except:
        print("⚠️ parse_review_summarisation_all_tabs not available, skipping")
        return None

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", section
    )
    time.sleep(2)

    final_data = {
        "heading": "",
        "tabs_data": {}
    }

    # Heading
    heading = section.find_element(By.CLASS_NAME, "rvwSmSecHeading")
    final_data["heading"] = heading.text.strip()

    # All tabs
    tabs = section.find_elements(By.CLASS_NAME, "rvwSmTabItem")

    for idx, tab in enumerate(tabs):
        tab_name = tab.find_element(By.CLASS_NAME, "rvwSmTabName").text.strip()

        # Click tab
        driver.execute_script("arguments[0].click();", tab)
        time.sleep(1.5)

        # Fresh HTML after tab change
        html = driver.execute_script(
            "return arguments[0].innerHTML;", section
        )
        soup = BeautifulSoup(html, "html.parser")

        tab_data = {
            "likes": [],
            "info_text": ""
        }

        # Likes
        for li in soup.select(".likeSec ul.bulletList li"):
            gray = li.select_one(".grayItem")
            tab_data["likes"].append({
                "text": li.get_text(" ", strip=True).replace(
                    gray.get_text(strip=True), ""
                ).strip() if gray else li.get_text(strip=True),
                "review_count": gray.get_text(strip=True) if gray else ""
            })

        # Info text
        info = soup.select_one(".rvwSmInfoTxt")
        if info:
            tab_data["info_text"] = info.get_text(strip=True)

        final_data["tabs_data"][tab_name] = tab_data

    return final_data

def parse_articles_section(driver,URLS):
    try:
        driver.get(URLS["compare"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["compare"])
    
    wait = WebDriverWait(driver, 15)

    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
    }
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image from pwa-headerwrapper
        try:
            header_wrapper = driver.find_element(By.CLASS_NAME, "pwa-headerwrapper")
            cover_img = header_wrapper.find_element(By.CSS_SELECTOR, ".header_img.desktop img")
            college_info["cover_image"] = cover_img.get_attribute("src")
            print(f"✓ Cover image found: {college_info['cover_image']}")
        except Exception as e:
            print(" Cover image not found: ")
        
        # Extract college name
        try:
            h1_element = driver.find_element(By.CSS_SELECTOR, "h1.inst-name.h2")
            full_text = h1_element.text.strip()
            # Clean the college name - remove "Faculty Details & Reviews" and location
            college_name = full_text.split("Faculty Details & Reviews")[0].strip()
            college_info["college_name"] = college_name
            print(f"✓ College name found: {college_info['college_name']}")
        except Exception as e:
            print(" College name not found: ")
        
        # Extract location and city
        try:
            location_element = driver.find_element(By.CSS_SELECTOR, ".ilp-loc.white-space-nowrap")
            location_text = location_element.text.strip()
            
            # Extract Vastrapur and Ahmedabad
            parts = location_text.split(", ")
            if len(parts) >= 1:
                # First part is Vastrapur
                college_info["location"] = parts[0].strip()
            
            if len(parts) >= 2:
                # Second part contains Ahmedabad (might be inside a link)
                city_part = parts[1]
                # Remove any HTML tags or links
                city_part = re.sub(r'<[^>]+>', '', city_part)
                college_info["city"] = city_part.strip()
            
            print(f"✓ Location found: {college_info['location']}, {college_info['city']}")
        except Exception as e:
            print(" Location not found: ")
        
        # Extract rating
        try:
            rating_element = driver.find_element(By.CSS_SELECTOR, ".rating-block.rvw-lyr")
            rating_text = rating_element.text.strip()
            # Extract just the numeric rating (e.g., "4.6" from "4.6" with stars)
            rating_match = re.search(r'(\d+\.\d+)', rating_text)
            if rating_match:
                college_info["rating"] = rating_match.group(1)
                print(f"✓ Rating found: {college_info['rating']}")
        except Exception as e:
            print(" Rating not found: ")
        
        # Extract reviews count
        try:
            reviews_link = driver.find_element(By.CSS_SELECTOR, "a.view_rvws.ripple.dark")
            reviews_text = reviews_link.text.strip()
            # Extract number from text like "(136 Reviews)"
            reviews_match = re.search(r'\((\d+)\s*Reviews', reviews_text)
            if reviews_match:
                college_info["reviews_count"] = int(reviews_match.group(1))
                print(f"✓ Reviews count found: {college_info['reviews_count']}")
        except Exception as e:
            print(" Reviews count not found: ")
        
        # Extract Q&A count
        try:
            qa_element = driver.find_element(By.CSS_SELECTOR, ".qna_student a")
            qa_text = qa_element.text.strip()
            # Extract number from text like "1.5k Student Q&A"
            qa_match = re.search(r'(\d+(?:\.\d+)?)\s*(k|K)?', qa_text)
            if qa_match:
                count = float(qa_match.group(1))
                if qa_match.group(2):  # If has 'k' suffix
                    count *= 1000
                college_info["qa_count"] = int(count)
                print(f"✓ Q&A count found: {college_info['qa_count']}")
        except Exception as e:
            print(" Q&A count not found: ")
        
        # Extract institute type (if available)
        try:
            # Look for institute type in other parts of the page
            institute_type_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Institute Type') or contains(text(), 'Type:')]")
            for elem in institute_type_elements:
                text = elem.text.strip()
                if "Institute Type" in text or "Type:" in text:
                    college_info["institute_type"] = text.split(":")[-1].strip() if ":" in text else text
                    print(f"✓ Institute type found: {college_info['institute_type']}")
                    break
        except Exception as e:
            print(" Institute type not found: ")
        
        # Extract established year (if available)
        try:
            # Look for established year in other parts of the page
            estd_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Established') or contains(text(), 'Estd') or contains(text(), 'Founded')]")
            for elem in estd_elements:
                text = elem.text.strip()
                # Look for year pattern
                year_match = re.search(r'\b(19|20)\d{2}\b', text)
                if year_match:
                    college_info["established_year"] = year_match.group()
                    print(f"✓ Established year found: {college_info['established_year']}")
                    break
        except Exception as e:
            print(" Established year not found: ")
        
        # Extract videos and photos count (from different parts of page)
        try:
            # Look for videos count
            video_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'video') or contains(text(), 'Video')]")
            for elem in video_elements:
                text = elem.text.lower()
                if "video" in text:
                    video_match = re.search(r'(\d+)\s*videos?', text)
                    if video_match:
                        college_info["videos_count"] = int(video_match.group(1))
                        print(f"✓ Videos count found: {college_info['videos_count']}")
                        break
        except Exception as e:
            print(" Videos count not found: ")
        
        try:
            # Look for photos count
            photo_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'photo') or contains(text(), 'Photo') or contains(text(), 'image') or contains(text(), 'Image')]")
            for elem in photo_elements:
                text = elem.text.lower()
                if "photo" in text or "image" in text:
                    photo_match = re.search(r'(\d+)\s*(photos?|images?)', text)
                    if photo_match:
                        college_info["photos_count"] = int(photo_match.group(1))
                        print(f"✓ Photos count found: {college_info['photos_count']}")
                        break
        except Exception as e:
            print(" Photos count not found: ")
        
        # Extract logo (if available)
        try:
            # Look for logo in different parts
            logo_elements = driver.find_elements(By.TAG_NAME, "img")
            for img in logo_elements:
                src = img.get_attribute("src") or ""
                alt = img.get_attribute("alt") or ""
                if ("logo" in src.lower() or "logo" in alt.lower()) and "shiksha.com" in src:
                    college_info["logo"] = src
                    print(f"✓ Logo found: {college_info['logo']}")
                    break
        except Exception as e:
            print(" Logo not found: ")

    except Exception as e:
        print(" Error in college header section: ")
    driver.get(URLS["compare"])
    wait = WebDriverWait(driver, 15)

    try:
        section = wait.until(
            EC.presence_of_element_located((By.ID, "Articles"))
        )
    except TimeoutException:
        print("⚠️ Articles section not found, skipping...")
        return []
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", section
    )
    time.sleep(2)

    html = driver.execute_script("return arguments[0].innerHTML;", section)
    soup = BeautifulSoup(html, "html.parser")

    articles_data = []

    for card in soup.select(".articleCard_Wrapper"):
        title_tag = card.select_one("h3.articleTitle a")
        author_tag = card.select_one(".authorInfo a")
        date_tag = card.select_one(".articelUpdatedDate")
        image_tag = card.select_one(".imageBox img")
        views_tag = card.select_one(".viewsData label")
        comment_tag = card.select_one(".commentData label")

        # Image fallback: background-image if img not present
        if not image_tag:
            bg = card.select_one(".img-blurdiv")
            image_url = ""
            if bg:
                style = bg.get("style", "")
                match = re.search(r'url\("&quot;(.*?)&quot;\)', style)
                if match:
                    image_url = match.group(1)
        else:
            image_url = image_tag.get("src", "")

        articles_data.append({
            "title": title_tag.text.strip() if title_tag else "",
            "link": "https://www.shiksha.com" + title_tag.get("href") if title_tag else "",
            "author_name": author_tag.text.strip() if author_tag else "",
            "author_link": author_tag.get("href") if author_tag else "",
            "date": date_tag.text.strip() if date_tag else "",
            "image": image_url,
            "views": views_tag.text.strip() if views_tag else "",
            "comments": comment_tag.text.strip() if comment_tag else ""
        })

    return {"college_info":college_info,"articles":articles_data}


def parse_faq_scholarships_section(driver, URLS):
    try:
        driver.get(URLS["scholarships"])
    except selenium.common.exceptions.InvalidSessionIdException:
        driver = webdriver.Chrome(options=options)
        driver.get(URLS["scholarships"]) 
    wait = WebDriverWait(driver, 15)

    college_info = {
        "college_name": None,
        "logo": None,
        "cover_image": None,
        "videos_count": 0,
        "photos_count": 0,
        "rating": None,
        "reviews_count": None,
        "qa_count": None,
        "location": None,
        "city": None,
        "institute_type": None,
        "established_year": None,
    }
    try:
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Extract cover image from pwa-headerwrapper
        try:
            header_wrapper = driver.find_element(By.CLASS_NAME, "pwa-headerwrapper")
            cover_img = header_wrapper.find_element(By.CSS_SELECTOR, ".header_img.desktop img")
            college_info["cover_image"] = cover_img.get_attribute("src")
            print(f"✓ Cover image found: {college_info['cover_image']}")
        except Exception as e:
            print(" Cover image not found: ")
        
        # Extract college name
        try:
            h1_element = driver.find_element(By.CSS_SELECTOR, "h1.inst-name.h2")
            full_text = h1_element.text.strip()
            # Clean the college name - remove "Faculty Details & Reviews" and location
            college_name = full_text.split("Faculty Details & Reviews")[0].strip()
            college_info["college_name"] = college_name
            print(f"✓ College name found: {college_info['college_name']}")
        except Exception as e:
            print(" College name not found: ")
        
        # Extract location and city
        try:
            location_element = driver.find_element(By.CSS_SELECTOR, ".ilp-loc.white-space-nowrap")
            location_text = location_element.text.strip()
            
            # Extract Vastrapur and Ahmedabad
            parts = location_text.split(", ")
            if len(parts) >= 1:
                # First part is Vastrapur
                college_info["location"] = parts[0].strip()
            
            if len(parts) >= 2:
                # Second part contains Ahmedabad (might be inside a link)
                city_part = parts[1]
                # Remove any HTML tags or links
                city_part = re.sub(r'<[^>]+>', '', city_part)
                college_info["city"] = city_part.strip()
            
            print(f"✓ Location found: {college_info['location']}, {college_info['city']}")
        except Exception as e:
            print(" Location not found: ")
        
        # Extract rating
        try:
            rating_element = driver.find_element(By.CSS_SELECTOR, ".rating-block.rvw-lyr")
            rating_text = rating_element.text.strip()
            # Extract just the numeric rating (e.g., "4.6" from "4.6" with stars)
            rating_match = re.search(r'(\d+\.\d+)', rating_text)
            if rating_match:
                college_info["rating"] = rating_match.group(1)
                print(f"✓ Rating found: {college_info['rating']}")
        except Exception as e:
            print(" Rating not found: ")
        
        # Extract reviews count
        try:
            reviews_link = driver.find_element(By.CSS_SELECTOR, "a.view_rvws.ripple.dark")
            reviews_text = reviews_link.text.strip()
            # Extract number from text like "(136 Reviews)"
            reviews_match = re.search(r'\((\d+)\s*Reviews', reviews_text)
            if reviews_match:
                college_info["reviews_count"] = int(reviews_match.group(1))
                print(f"✓ Reviews count found: {college_info['reviews_count']}")
        except Exception as e:
            print(" Reviews count not found: ")
        
        # Extract Q&A count
        try:
            qa_element = driver.find_element(By.CSS_SELECTOR, ".qna_student a")
            qa_text = qa_element.text.strip()
            # Extract number from text like "1.5k Student Q&A"
            qa_match = re.search(r'(\d+(?:\.\d+)?)\s*(k|K)?', qa_text)
            if qa_match:
                count = float(qa_match.group(1))
                if qa_match.group(2):  # If has 'k' suffix
                    count *= 1000
                college_info["qa_count"] = int(count)
                print(f"✓ Q&A count found: {college_info['qa_count']}")
        except Exception as e:
            print(" Q&A count not found: ")
        
        # Extract institute type (if available)
        try:
            # Look for institute type in other parts of the page
            institute_type_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Institute Type') or contains(text(), 'Type:')]")
            for elem in institute_type_elements:
                text = elem.text.strip()
                if "Institute Type" in text or "Type:" in text:
                    college_info["institute_type"] = text.split(":")[-1].strip() if ":" in text else text
                    print(f"✓ Institute type found: {college_info['institute_type']}")
                    break
        except Exception as e:
            print(" Institute type not found: ")
        
        # Extract established year (if available)
        try:
            # Look for established year in other parts of the page
            estd_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Established') or contains(text(), 'Estd') or contains(text(), 'Founded')]")
            for elem in estd_elements:
                text = elem.text.strip()
                # Look for year pattern
                year_match = re.search(r'\b(19|20)\d{2}\b', text)
                if year_match:
                    college_info["established_year"] = year_match.group()
                    print(f"✓ Established year found: {college_info['established_year']}")
                    break
        except Exception as e:
            print(" Established year not found: ")
        
        # Extract videos and photos count (from different parts of page)
        try:
            # Look for videos count
            video_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'video') or contains(text(), 'Video')]")
            for elem in video_elements:
                text = elem.text.lower()
                if "video" in text:
                    video_match = re.search(r'(\d+)\s*videos?', text)
                    if video_match:
                        college_info["videos_count"] = int(video_match.group(1))
                        print(f"✓ Videos count found: {college_info['videos_count']}")
                        break
        except Exception as e:
            print(" Videos count not found: ")
        
        try:
            # Look for photos count
            photo_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'photo') or contains(text(), 'Photo') or contains(text(), 'image') or contains(text(), 'Image')]")
            for elem in photo_elements:
                text = elem.text.lower()
                if "photo" in text or "image" in text:
                    photo_match = re.search(r'(\d+)\s*(photos?|images?)', text)
                    if photo_match:
                        college_info["photos_count"] = int(photo_match.group(1))
                        print(f"✓ Photos count found: {college_info['photos_count']}")
                        break
        except Exception as e:
            print(" Photos count not found: ")
        
        # Extract logo (if available)
        try:
            # Look for logo in different parts
            logo_elements = driver.find_elements(By.TAG_NAME, "img")
            for img in logo_elements:
                src = img.get_attribute("src") or ""
                alt = img.get_attribute("alt") or ""
                if ("logo" in src.lower() or "logo" in alt.lower()) and "shiksha.com" in src:
                    college_info["logo"] = src
                    print(f"✓ Logo found: {college_info['logo']}")
                    break
        except Exception as e:
            print(" Logo not found: ")

    except Exception as e:
        print(" Error in college header section: ")
    driver.get(URLS["scholarships"])
    wait = WebDriverWait(driver, 15)
    # section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".wikkiContents.faqAccordian")))
    try:
        section = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,".wikkiContents.faqAccordian")
            )
        )
    except:
        
        return None
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", section)
    time.sleep(0.5)

    html = driver.execute_script("return arguments[0].innerHTML;", section)
    soup = BeautifulSoup(html, "html.parser")

    # Author
    author_tag = soup.select_one(".adp_usr_dtls a")
    author_name = author_tag.text.strip() if author_tag else ""
    author_link = author_tag.get("href") if author_tag else ""
    
    # Date
    date_tag = soup.select_one(".post-date")
    updated_on = date_tag.text.replace("Updated on", "").strip() if date_tag else ""

    # Paragraphs
    paragraphs = [p.text.strip() for p in soup.select(".abtSection p")]

    # Tables
    tables = []
    for table in soup.select(".abtSection table"):
        table_data = []
        for row in table.find_all("tr"):
            cols = [td.text.strip() for td in row.find_all(["td","th"])]
            table_data.append(cols)
        tables.append(table_data)

    # PDF links
    pdf_links = [a.get("data-link") for a in soup.select("a.smce-cta-link")]

    # Videos
    iframe_elements = driver.find_elements(By.CSS_SELECTOR, ".vcmsEmbed iframe")
    videos = []
    
    for iframe in iframe_elements:
        driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
        time.sleep(0.5)  # wait for lazy loading
        src = iframe.get_attribute("src") or iframe.get_attribute("data-src")
        if src:
            videos.append(src)

    result = {}
    
    result["author_name"] = author_name
    result["author_link"] = author_link
    result["updated_on"] = updated_on
    result["paragraphs"] = paragraphs
    result["tables"] = tables
    result["pdf_links"] = pdf_links
    result["videos"] = videos


    return {"college_info":college_info,"result":result}

# def extract_shiksha_qna(driver,URLS):
#     driver.get(URLS["qna"])

#     # Thoda wait karo page load ke liye
#     import time
#     time.sleep(2)

#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     result = {}

#     # ===== Question Details =====
#     question_data = {}
#     title_tag = soup.select_one("#quesTitle_5114413 .wikkiContents")
#     question_data['title'] = title_tag.get_text(strip=True) if title_tag else None

#     asker_tag = soup.select_one(".new-column .right-cl a")
#     question_data['asked_by'] = asker_tag.get_text(strip=True) if asker_tag else None
#     question_data['asker_profile'] = asker_tag['href'] if asker_tag else None

#     follower_tag = soup.select_one(".followersCountTextArea")
#     question_data['followers'] = int(follower_tag.get_text(strip=True).split()[0]) if follower_tag else 0

#     # Views
#     viewers_tag = soup.select_one(".viewers-span")
#     if viewers_tag:
#         views_text = viewers_tag.get_text(strip=True).replace("Views","").strip()
#         if "k" in views_text:
#             views_text = views_text.replace("k", "")
#             question_data['views'] = int(float(views_text) * 1000)
#         else:
#             question_data['views'] = int(views_text)
#     else:
#         question_data['views'] = 0


#     time_tag = soup.select_one("span.time span:last-child")
#     question_data['posted'] = time_tag.get_text(strip=True) if time_tag else None

#     result['question'] = question_data

#     # ===== Answers =====
#     answers = []
#     for li in soup.find_all("li", class_="module"):
#         answer = {}

#         author_tag = li.select_one(".avatar-name")
#         answer['author_name'] = author_tag.get_text(strip=True) if author_tag else None
#         answer['author_profile'] = author_tag['href'] if author_tag else None

#         level_tag = li.select_one(".lvl-name")
#         answer['contributor_level'] = level_tag.get_text(strip=True) if level_tag else None

#         time_tag = li.select_one(".time")
#         answer['time'] = time_tag.get_text(strip=True) if time_tag else None

#         content_tag = li.select_one("p[id^='answerMsgTxt_']")
#         if content_tag:
#             text = content_tag.get_text(strip=True)
#             text = text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
#             answer['content'] = text
#         else:
#             answer['content'] = None

#         upvote_tag = li.select_one("input[id^='userCountUpvote_']")
#         downvote_tag = li.select_one("input[id^='userCountDownvote_']")
#         answer['upvotes'] = int(upvote_tag['value']) if upvote_tag else 0
#         answer['downvotes'] = int(downvote_tag['value']) if downvote_tag else 0

#         share_tag = li.select_one("a.qSLayer")
#         answer['share_url'] = share_tag['data-shareurl'] if share_tag else None

#         report_tag = li.select_one("a.raLayerClk")
#         answer['report_url'] = report_tag['href'] if report_tag else None

#         answers.append(answer)

#     result['answers'] = answers

#     return result


def scrape_mba_colleges():
    driver = create_driver()
    all_data = []
    c_count = 1

    try:
        for base_url in BASE_URL:
            print("🔄 Scraping:", base_url)

            URLS = build_urls(base_url)
           

            college_data = {       
                "college_details":{
                "id":f"college_{c_count:03d}",
                "college_info":{
                 "college_info":scrape_college_info(driver,URLS),
                },
                "courses": scrape_courses(driver,URLS),
                "fees":scrape_fees(driver,URLS),
                "reviews":{
                    "review_summary":scrape_review_summary(driver,URLS),
                 },
                 "admission":{
                    "admission_overview":scrape_admission_overview(driver,URLS),
                 },
                "placement":{
                    "placement_report":scrape_placement_report(driver,URLS),
                 
                },               
                "cut_off":{
                "cut_off":scrape_cutoff(driver,URLS),
                },
                "ranking":{
                "ranking":scrape_ranking(driver,URLS),
              
                },
                "gallery":{
                "gallery_page":scrape_mini_clips(driver,URLS),
                },
                "hotel_campus":{
                 "hostel_campus":scrape_hostel_campus_js(driver,URLS),
        
                },
                "faculty":{
                   "faculty":parse_faculty_full_html(driver,URLS),
                    "faculty_reviews":parse_faculty_reviews(driver,URLS),
                    "review_summarisation":parse_review_summarisation_all_tabs(driver,URLS),                   
                },
                "compare":{
                    "articles":parse_articles_section(driver,URLS),
                },
                
                "scholarships":parse_faq_scholarships_section(driver,URLS),
                    }
               
                }
            all_data.append(college_data)
            c_count += 1
    finally:
        driver.quit()

    return all_data



import time
import os

TEMP_FILE = "iim_ahmedabad_full_data.tmp.json"
FINAL_FILE = "iim_ahmedabad_full_data.json"

UPDATE_INTERVAL = 6 * 60 * 60  # 6 hours

def auto_update_scraper():
    # Check last modified time
    # if os.path.exists(DATA_FILE):
    #     last_mod = os.path.getmtime(DATA_FILE)
    #     if time.time() - last_mod < UPDATE_INTERVAL:
    #         print("⏱️ Data is recent, no need to scrape")
    #         return

    print("🔄 Scraping started")
    data = scrape_mba_colleges()
    with open(TEMP_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Atomic swap → replaces old file with new one safely
    os.replace(TEMP_FILE, FINAL_FILE)

    print("✅ Data scraped & saved successfully (atomic write)")

if __name__ == "__main__":
    auto_update_scraper()
        
