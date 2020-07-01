# Paradigms for the Cognition of Adolescent Depressive patients

Wang Kangcheng and his colleagues (Zhang Yihao and Huang Zihuang) design 11 experimental paradigms for measuring the cognitive abilities for patients of adolescent depression. These paradigms run with PsychoPy3. Because the subjects that we will assess are from China, most of materials are in Chinese.

Before running the paradigms, we suggest you to read the instruction which could be found in **documents** or **documentation** folders. __Practice.psyexp is the practice procedure. __Formal.psyexp is the formal procedure and will generate data which can be analyzed. The results of these experiments would be saved in the folder **data** as the *.csv, and can be imported and analyzed in SPSS, MATLAB and R.

They are not as polished, but could serve as a starting point for those wishing to implement things like them. They are:

* 1_Facial_Emotion_Recognition: require subjects to determine the type of facial emotion. Materials of emotional faces are from FACES database. Please cite the following research if you use it. 

Ebner, N.C., Riediger, M. & Lindenberger, U. FACES—A database of facial expressions in young, middle-aged, and older women and men: Development and validation. Behavior Research Methods 42, 351–362 (2010). https://doi.org/10.3758/BRM.42.1.351

* 2_Dot_Probe: require subjects to locate the side of dark block. We implement the attentional bias task described in Kim 2014 (doi: 10.4306/pi.2014.11.2.160). However, emotional faces are from FACES database.

Kim, Y. R., Oh, S. M., Corfield, F., Jeong, D. W., Jang, E. Y., & Treasure, J. (2014). Intranasal oxytocin lessens the attentional bias to adult negative faces: a double blind within-subject experiment. Psychiatry investigation, 11(2), 160.

* 3_Go_Nogo: Implement the classic Go/NoGo task described in Hirose 2012 (doi: 10.1523/JNEUROSCI.0540-12.2012). The second part is the modified Go/NoGo task (emotional faces: go, positive and neural faces; nogo, negative faces).

Hirose, S., Chikazoe, J., Watanabe, T., Jimura, K., Kunimatsu, A., Abe, O., ... & Konishi, S. (2012). Efficiency of go/no-go task performance implemented in the left hemisphere. Journal of Neuroscience, 32(26), 9059-9065.

* 4_Nback: 0 back, 1 back and 2 back are designed here. The material here is the number.

* 5_Stroop: First part is the classic stroop Task (word) described in Stroop 1935. 

Stroop, J. R. (1935). Studies of interference in serial verbal reactions. Journal of experimental psychology, 18(6), 643.

* 6_Scene_Recognition_Task: Implement the classic Scene Recognition Task described in Hartley 2007 (doi: 10.1002/hipo.20240)

Hartley, T., Bird, C. M., Chan, D., Cipolotti, L., Husain, M., Vargha‐Khadem, F., & Burgess, N. (2007). The hippocampus is required for short‐term topographical memory in humans. Hippocampus, 17(1), 34-48.

* 7_Flanker: Implement the Erikson Flanker Task described in Huyser 2011 (doi: 10.1111/j.1469-7610.2011.02439.x)

Huyser, C., Veltman, D. J., Wolters, L. H., de Haan, E., & Boer, F. (2011). Developmental aspects of error and high‐conflict‐related brain activity in pediatric obsessive–compulsive disorder: a fMRI study with a Flanker task before and after CBT. Journal of Child Psychology and Psychiatry, 52(12), 1251-1260.

* 8_Task_Switching : Implement the adjusting amount task described in Cubillo 2010 (doi: 10.1016/j.jpsychires.2009.11.016)

Cubillo, A., Halari, R., Ecker, C., Giampietro, V., Taylor, E., & Rubia, K. (2010). Reduced activation and inter-regional functional connectivity of fronto-striatal networks in adults with childhood Attention-Deficit Hyperactivity Disorder (ADHD) and persisting symptoms during tasks of motor inhibition and cognitive switching. Journal of psychiatric research, 44(10), 629-639.

* 9_Simple_Guessing_Task: require subjects to determine whether the number of dice is large (4,5 and 6) or small (1,2 and 3). This is similar to task described in Belden 2016 (doi: 10.1016/j.jaac.2016.09.503)
Belden, Andy C., et al. "Neural correlates of reward processing in depressed and healthy preschool-age children." Journal of the American Academy of Child & Adolescent Psychiatry 55.12 (2016): 1081-1089.

* 10_Delay_Discounting_Task: Implement the adjusting amount task described in Frye 2016 (doi: 10.3791/53584)

Frye, C. C., Galizio, A., Friedel, J. E., DeHart, W. B., & Odum, A. L. (2016). Measuring delay discounting in humans using an adjusting amount task. JoVE (Journal of Visualized Experiments), (107), e53584.

* 11_Time_Perception : require subjects to copy the time of auditory and visual materials.



