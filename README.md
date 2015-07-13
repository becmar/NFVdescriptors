
Example of NSD - VNFD 
======
Introduction 
------
 
 This set of descriptors serve as an example for the definition of the appropriate VNFD and NSD required for the composotion of a NS comprised by a  **single dataplane VNF** in this case a Virtual Traffic Classifier VNF. The basic functionality of the VNF is to accept incoming packets (data-in) analyse heade and payload information and forward the traffic (_data-out_) after the appropriate marking/prioritisation policies have been places on the packets categorised under certain service/application categories. 
 
 The VNFD and NSD are based on the current ETSI ISG NFV proposal as laid out in [ETSI GS NFV-MAN 001 v 1.1.1](http://www.uoi.gr "click to download"). Project related sections have been added in order to acommodate its developements and requirements. 
 Notably you may find additional sections for the Marketplace, Monitoring, EPA and VNF configuration. 
 
 Definitions
------
 As suggested by ETSI documentation the relation model for a VNFD is illustrated in the following ![figure](Figures/rel_model.jpg "VNFD relation Model")
 
 In order to simplify the model it is assumed that each VDU contains only one VNFC. 
 
VNF Architecture 
------ 
 
### VNF Requirements 
### VNF Monitoring  
### VNF Configuration  
 
Deployment Model  
------ 
Assumptions 
------ 
 
1.	NS comprises a single VNF 
2.	A vdu comprises of a single VNFC 
3.	The network model for VNF deployment assumes the creation of 4 tenant networks namely: 
 	*	Management: used for internal management communication and signaling 
	*	Monitoring: used for the monitoring agent communications with the VNFC
	*	Storage: used for connecting VNFC to persistent or non-persistent storage 
	*	Datapath: used for the data that traverse the VNFC

