Ce dossier contient toutes les classes qui vont servir de tremplain
entre les modeles et les vues

Il sagit des classes services, toutes operations d'ajout, de recherche, de suppression 
ou de mise a jour doit imperativement passe par les ervices

L'avantage d'utiliser les Classes de type de services dans un framework MCV est que notre application
est facilement maintenable meme dans le cas ou les standars lies au modele change la logique
cache derriere les services restent la meme

Il serait donc plus facile de modifer une fonction dans service que de modfier toues les fonctions
utilisees dans les vues a cet effet.