# Programming-class
Repositorio para almacenar los ejercicios y ejemplos de la clase de "Pensamiento Computacional para Ingeniería" Semestre AD23

<![endif]-->

**Tema del Proyecto:**

Mi idea de proyecto se basa en que las personas van a acudir a él para preguntarle por una mejor rutina de skincare, de cabello y de qué pueden hacer para mantener una buena alimentación dependiendo de su tipo de piel, de la forma que quieren tener su cabello y de cual es el goal qué tienen para su alimentación.

A mi se me hace interesante esto debido a que varias mujeres en especial adolescentes no saben a dónde acudir para poder obtener este tipo de información o que información es verídica y con este software podrán tener una variedad de información en una sola plataforma.

**Algoritmo:**
	
	
	edad=0
	resta=0
	Preguntar por la edad de la persona:
	while edad <= 25:
		resta= 25 - edad
		print ("Todavía no es tarde para cuidar tu piel o tu cabello, te faltan",resta, "para llegar a los 25, esa es la edad cuando la piel empieza a envejecer :( .")
	else:
		print("Esperamos poder ayudarte con algo para el cuidado de tu cuerpo")
	
	Mientras si quiere saber de:
	lista1=list (("1-skincare","2-cuidados del cabello))
	1=skincare,
	2= cuidados del cabello 
	print(lista1)
	
	 
	Preguntar si quiere la definición de ambos términos:
	terminos= list(("y=yes,si", "n=no,no"))
	y= yes, si
	n= no
	print(terminos)
		
		While terminos==y:
			imprimir definición de skincare y de cuidados del cabello
		
		Si quiere saber de 1:
		
			Mientras quiera preguntar sobre cara o cuerpo:
			lista2= list((a=cara,"b=cuerpo"))
			print(lista2)

				Mientras quiera preguntar de a:
		
					Preguntar qué tratamiento quiere saber, si contra acné, rosácea, etc…
						trata=list (("4=acné,"5=rosácea"))
						print(trata)

							Si quiere saber de 4:

								Dar información de acné

							Si quiere saber de 5:

								Dar información de rosácea
							Sino:
								fin si

				Mientras quiera preguntar de b:
				hello== list(("6=humectación,"7=exfoliación","8=depilación"))
				print(hello)
					Preguntar si quiere información sobre humectación, exfoliación o depilación. 

						Si quiere información de 6:

							Dar información sobre humectación corporal

						Si quiere información de 7:

							Dar información de exfoliación corporal

						Si quiere información sobre 8:

							Preguntar sí quiere saber sobre costos, duración o cuidados antes y después del tratamiento.
							halo=list((co=costos","du=duración","cu=cuidados"))
							print(halo)
								Si quiere saber sobre co:

									Dar información sobre costos

								Si quiere saber sobre du:

									Dar información sobre la duración

								Si quiere saber sobre cu:

									Dar información sobre los cuidados que se deben llevar.

	Si quiere saber sobre 2:
		Preguntar el tipo de cabello que tiene (rizado, ondulado, lacio)
		class= list (("ri=rizado","on=ondulado","la=lacio"))
		print(class)
		
			Si tiene el cabello ri:

				Preguntar si el cabello es graso o seco:
				voila= list(("gr=graso","se=seco"))
				print(voila)
				
					Si es gr:

						Dar información sobre mantenimiento, crecimiento, productos buenos y consejos

					Si es se:

						Dar información sobre mantenimiento, crecimiento, productos buenos y consejos.

			Si tiene el cabello on:

				Preguntar si el cabello es graso o seco:
				monsieur= list(("gr=graso","se=seco"))
				print(monsieur)

					Si es gr:

						Dar información sobre mantenimiento, crecimiento, productos buenos y consejos

					Si es se:

						Dar información sobre mantenimiento, crecimiento, productos buenos y consejos.

		Si tiene el cabello la:

			Preguntar si el cabello es graso o seco:
			payton= list(("gr=graso","se=seco"))
			print(payton)

				Si es gr:

					Dar información sobre mantenimiento, crecimiento, productos buenos y consejos

				Si es se:

					Dar información sobre mantenimiento, crecimiento, productos buenos y consejos.


	pregunta=Preguntar si quiere volver a preguntar acerca de algo:
	10=yes
	11=no
	si pregunta=10:
		repetir ciclo
	sino:
		fin ciclo
			print(“Gracias por usar y tener confianza en nuestra información..”)
