# Contribuciones bienvenidas

¡Gracias por su interés en contribuir con **PoliCaptcha**! Contribuir a proyectos de código abierto como este puede ser una forma gratificante de aprender, enseñar y adquirir experiencia. No solo eso, contribuir es una excelente manera de involucrarse con la _codificación social_. Estamos emocionados de ver las increíbles contribuciones que hará, así como también cómo sus contribuciones beneficiarán a otros.

Si es nuevo en contribuir a proyectos de código abierto, el proceso puede ser intimidante. ¡No es para preocuparse! Para ayudar a garantizar que tanto usted como la comunidad aprovechen al máximo sus contribuciones, hemos elaborado las siguientes pautas.

## Tabla de contenido

1. [Tipos de contribuciones](#tipos-de-contribuciones)
1. [Reglas básicas y expectativas](#reglas-básicas--expectativas)
1. [Cómo contribuir](#cómo-contribuir)

---

## Tipos de Contribuciones

El concepto erróneo común acerca de contribuir a un proyecto de código abierto es que necesita contribuir con el código. De hecho, existen numerosas formas en las que puede contribuir directamente. Para darle algunas ideas de cómo puede contribuir, aquí hay algunos ejemplos de los tipos de contribuciones que estamos buscando:

### Los desarrolladores pueden:

* Eche un vistazo a los [problemas abiertos][issues] y encuentre uno que pueda abordar.

* Localizar y corregir errores.

* Implementar nuevas características innovadoras e impresionantes.

* Ayuda a mejorar herramientas y pruebas.

### Los organizadores y planificadores pueden:

* Vínculo a problemas duplicados y sugiera nuevas etiquetas de problemas para ayudar a mantener las cosas organizadas.

* Revise los [problemas abiertos][issues] y sugiera cerrar los antiguos.

* Hacer preguntas aclaratorias sobre temas abiertos recientemente para hacer avanzar la discusión.

* Ayuda a organizar reuniones sobre el proyecto.

### Los escritores pueden:

* Ayuda para arreglar o mejorar la documentación del proyecto.

* Contribuir a la [Wiki][wiki] del proyecto.

### Los diseñadores pueden:

* Diseñe marcos de alambre, maquetas, activos gráficos y logotipos.

* Elaborar una guía de estilo para ayudar a que el proyecto tenga un diseño visual coherente.

### Los seguidores pueden:

* Responder preguntas de personas sobre temas abiertos, o sobre el proyecto en general.

* Ayuda a moderar foros de discusión o canales de conversación.

## Reglas básicas & expectativas

Dado que el proyecto se actualiza constantemente con contribuciones de todo tipo, es importante establecer reglas básicas y expectativas. Esto ayuda a garantizar la mejor experiencia posible para los usuarios de la aplicación Google Maps Navigator sin conexión, así como a fomentar una comunidad positiva, útil y animada de colaboradores activos como usted.

Asegúrese de leer nuestro [código de conducta][code-of-conduct] antes de contribuir.

## Cómo contribuir

Si desea contribuir, un buen lugar para comenzar es buscar en los [problemas][issues] y [solicitudes de extracción][pull-requests] para ver si alguien más tuvo una idea o pregunta similar.

Si no ve su idea en la lista y cree que se ajusta a los objetivos del proyecto, debe:

* **Contribución menor _(p. ej., corrección de errores tipográficos)_:** Abra una solicitud de extracción
* **Contribución principal _(p. ej., nueva función)_:** Comience abriendo una edición primero. De esa manera, otras personas pueden opinar sobre la discusión y la planificación antes de hacer cualquier trabajo.

Para empezar a hacer una contribución:

1. `Bifurque` el repositorio del proyecto haciendo clic en el botón **fork** en GitHub.![fork](https://help.github.com/assets/images/help/repository/fork_button.jpg)

1. `clonar` su repositorio bifurcado (_consejo de novato: el comando real que escribe es todo lo que está después de $_):

   ```shell
   $ git clone https://github.com/<YOUR-USERNAME>/PoliCaptcha
   ```

1. Agregue un nuevo control remoto que apunte al proyecto original para que pueda sincronizar los cambios del proyecto con su copia local:

   ```shell
   $ git remote add upstream https://github.com/Afkerian/PoliCaptcha/
   ```

1. Tire de los cambios ascendentes en la rama `bugFix` de sus repositorios locales:

   ```shell
   $ git checkout bugFix
   $ git pull upstream development && git push origin development
   ```

1. Cree una nueva rama desde la rama `bugFix`:
![rama](https://help.github.com/assets/images/help/branch/branch-selection-dropdown.png)

   **IMPORTANTE:** Asegúrate de estar primero en la rama `bugFix`.

   ```shell
   $ git checkout -b <YOUR-NEW-BRANCH>
   ```

1. Haz tu contribución al código del proyecto.

1. Escriba o adapte las pruebas según sea necesario.

1. Agregue o cambie la documentación según sea necesario.

1. Después de confirmar los cambios, empuje su rama a su bifurcación en Github, el `origen` remoto:

   **IMPORTANTE:** Su mensaje de confirmación debe estar en tiempo presente y debe describir lo que la confirmación, cuando se aplica, hace al código, no lo que usted hizo con el código.

   ```concha
   $ git push -u origin <TU-NUEVA-RAMA>
   ```

1. Desde su repositorio de GitHub bifurcado, abra una solicitud de extracción en la rama que contiene sus contribuciones. Diríjase a la rama `bugFix` del proyecto para la solicitud de incorporación de cambios.

1. En este punto, su contribución ha sido enviada para revisión. Tenga paciencia mientras se revisa su contribución, ya que esto puede llevar algún tiempo. Mientras tanto, si hay preguntas o comentarios sobre su contribución, responda y/o actualice con compromisos futuros.

1. Una vez que se aprueba y fusiona la solicitud de incorporación de cambios, puede extraer los cambios desde "upstream" a su repositorio local y eliminar su(s) rama(s) adicional(es).

1. No olvide consultar más [sobre] este proyecto

¡Feliz contribución!

Este código de conducta esta basado en el código de conducta del proyecto [Navi]

[issues]: https://github.com/Afkerian/PoliCaptcha/issues
[pull-requests]: https://github.com/Afkerian/PoliCaptcha/pulls
[wiki]: https://github.com/Afkerian/PoliCaptcha/wiki
[code-of-conduct]: ./CODE_OF_CONDUCT.md
[sobre]: https://github.com/Afkerian/PoliCaptcha/blob/main/README.md
[Navi]: https://github.com/TheDevPath/Navi/blob/development/CONTRIBUTING.md
