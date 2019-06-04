FROM debian:latest
RUN apt update
RUN apt install -y ssh
RUN apt install -y python

#First jail
RUN useradd pybeer1 -m
RUN echo "pybeer1:pybeer1" | chpasswd
COPY 1_The_first_DIRection/* /home/pybeer1/
RUN chgrp pybeer1 /home/pybeer1/*
RUN chmod 550 /home/pybeer1/*
RUN chmod o+r /home/pybeer1/jail.py
RUN sed -i.bak 's/\/home\/pybeer1:/\/home\/pybeer1:\/home\/pybeer1\/jail.py/' /etc/passwd

#Second jail
RUN useradd pybeer2 -m
RUN echo "pybeer2:H2G2{Ev3ry_PyJ41l_StARt_wi7h_a_dir()}" | chpasswd
COPY 2_Introspection/* /home/pybeer2/
RUN chgrp pybeer2 /home/pybeer2/*
RUN chmod 550 /home/pybeer2/*
RUN chmod o+r /home/pybeer2/jail.py
RUN sed -i.bak 's/\/home\/pybeer2:/\/home\/pybeer2:\/home\/pybeer2\/jail.py/' /etc/passwd

#Third jail
RUN useradd pybeer3 -m
RUN echo "pybeer3:H2G2{y0u_knOw_HOW_cL4S5es_w0rk_oN_pyth0n}" | chpasswd
COPY 3_Known_Payload/* /home/pybeer3/
RUN chgrp pybeer3 /home/pybeer3/*
RUN chmod 550 /home/pybeer3/*
RUN chmod o+r /home/pybeer3/jail.py
RUN sed -i.bak 's/\/home\/pybeer3:/\/home\/pybeer3:\/home\/pybeer3\/jail.py/' /etc/passwd

#Fourth jail
RUN useradd pybeer4 -m
RUN echo "pybeer4:H2G2{a_W3Ll_knOwN_P4yl0aD...}" | chpasswd
COPY 4_Annoying_Encapsulation/* /home/pybeer4/
RUN chgrp pybeer4 /home/pybeer4/*
RUN chmod 550 /home/pybeer4/*
RUN chmod o+r /home/pybeer4/jail.py
RUN sed -i.bak 's/\/home\/pybeer4:/\/home\/pybeer4:\/home\/pybeer4\/jail.py/' /etc/passwd


#Fifth jail
RUN useradd pybeer5 -m
RUN echo "pybeer5:H2G2{1mPR0vis3_4dApt_OveRCoMe}" | chpasswd
COPY 5_The_World_Best_Beer/jail.py /home/pybeer5/
COPY 5_The_World_Best_Beer/flag.txt /home/pybeer5/
RUN mkdir /home/pybeer5/beers
COPY 5_The_World_Best_Beer/beers/* /home/pybeer5/beers/
RUN chgrp -R pybeer5 /home/pybeer5/*
RUN chmod -R 550 /home/pybeer5/*
RUN chmod o+r /home/pybeer5/jail.py
RUN sed -i.bak 's/\/home\/pybeer5:/\/home\/pybeer5:\/home\/pybeer5\/jail.py/' /etc/passwd



RUN mkdir /var/run/sshd
RUN echo LANG="fr_FR.UTF-8" > /etc/locale.conf
ENV LANG=fr_FR.UTF-8
CMD ["/usr/sbin/sshd", "-D"]

