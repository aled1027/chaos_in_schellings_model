library(dplyr)
library(ggplot2)
library(tidyr)

# ----
# NEAREST MEMBERS
# ----

#Load data
nearest_3_3_data <- read.csv('nearest_data_0.300000_0.300000.csv')
nearest_sim33 <- data.frame(nearest_3_3_data[2:52])
nearest_hap33 <- data.frame(nearest_3_3_data[53:103])

# Shape into vertical table
meanhap <- summarise_each(nearest_hap33, funs(mean)) %>%
  t() %>%
  data.frame()
meanhap$iter <- 0:50
names(meanhap)[1] <- "mean_happiness"

meansim <- summarise_each(nearest_sim33, funs(mean)) %>%
  t() %>%
  data.frame() 
meansim$iter <- 0:50
names(meansim)[1] <- "mean_similarity"

# Combine happiness similarity
nearest_means <- left_join(meansim, meanhap, by="iter") %>%
  gather("value", "means",c(1,3))
nearest_means$rw <- "nearest"

# -----
#  RW 
# -----

rw_3_3_data <- read.csv('rw_data_0.300000_0.300000.csv')

rw_sim33 <- data.frame(rw_3_3_data[2:52])
rw_hap33 <- data.frame(rw_3_3_data[53:103])

meanhaprw <- summarise_each(rw_hap33, funs(mean)) %>%
  t() %>%
  data.frame()
meanhaprw$iter <- 0:50
names(meanhaprw)[1] <- "mean_happiness"

meansimrw <- summarise_each(rw_sim33, funs(mean)) %>%
  t() %>%
  data.frame() 
meansimrw$iter <- 0:50
names(meansimrw)[1] <- "mean_similarity"


rw_means <- left_join(meansimrw, meanhaprw, by="iter") %>%
  gather("value", "means",c(1,3))
rw_means$rw <- "random_walk"

# combine data sets.
means <- bind_rows(nearest_means, rw_means)


ggplot(data = means, aes(x = iter, y= means, col = as.factor(rw), shape=as.factor(value))) + 
  geom_point() +
  coord_cartesian(ylim = c(0,1)) +
  xlab("Iterations")
