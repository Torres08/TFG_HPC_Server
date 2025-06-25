---
theme: neversink

layout: cover
color: amber
title: Portada

transition: slide-left

---

<style>
@media print {
  .fade-up-stairs-1,
  .fade-up-stairs-2,
  .fade-up-stairs-3,
  .fade-up-stairs-4,
  .fade-up-stairs-5,
  .fade-left-stairs-1,
  .fade-left-stairs-2,
  .fade-left-stairs-3,
  .fade-left-stairs-4,
  .fade-left-stairs-5 {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
  }
}
</style>

# Servidor HPC para LLM: Despliegue, Benchmarking y Operaciones SRE

<div class="flex flex-wrap items-center justify-between w-full">
    <div class="w-3/5">
        <strong>Autor:</strong> Juan Luis Torres Ramos<br>
        <strong>Supervisores:</strong> Alberto Guillén Perales y Juan Manuel Tenorio del Moral<br>    <strong>Universidad de Granada</strong><br>
        <strong>Fecha:</strong> 09/06/2025
    </div>
    <div class="w-1/3 flex justify-end">
        <img src="./images/image71.png" alt="Logo ETSIIT" width="300" />
    </div>
</div>

<!-- ---
title: Índice
layout: side-title
color: amber-light

side: l
titlewidth: is-3
align: cm-lm

transition: slide-left

:: title ::
# Índice


:: content ::
<style>
.ol-amber > li::marker {
  color: #f59e42;           /* Tailwind amber-500 */
  font-weight: bold;
  font-size: 1.1em;
}
</style>

<ol class="ol-amber ml-6 space-y-4 text-base">
  <li>Introducción y Motivación</li>
  <li>Objetivos</li>
  <li>Estado del Arte</li>
  <li>Propuesta y Metodología</li>
  <li>Infraestructura y Puesta a Punto</li>
  <li>Ejecución de LLM en Contenedores</li>
  <li>Evaluación de Rendimiento</li>
  <li>Gestión Operativa y SRE</li>
  <li>Conclusiones y Trabajos Futuros</li>
</ol> -->



---
title:  Introducción y Motivación
layout: top-title-two-cols
color: amber-light

align: l-lm-cm
columns: is-4

transition: slide-left
---

:: title ::
# Introducción y Motivación

:: left ::
<style>
.ol-amber > li::marker {
  color: #f59e42;           /* Tailwind amber-500 */
  font-weight: bold;
  font-size: 1.1em;
}
</style>

<ol class="ol-amber ml-6 space-y-4 text-base">
  <li>Era de los Datos</li>
  <li>High Performing Computing</li>
  <li>AlphaFold y Human Brain Project</li>
  <li>Alta demanda de LLM y practicas SRE</li>
</ol>



:: right ::
<figure class="flex flex-col justify-center h-full">
  <img src="./images/alphafold.png" alt="Comparativa de rendimiento de modelos estadounidenses y chinos en LMSYS Chatbot Arena" class="rounded-lg shadow-lg my-8" style="max-width: 100%; margin-bottom: 0.3rem;" />
  <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
    AlphaFold: Artificial intelligence program by DeepMind (Google)
  </figcaption>
</figure>




<!-- 
Importancia de HPC y LLMs en la actualidad
Retos: escalabilidad, fiabilidad y seguridad
Motivación personal y profesional
-->


---
title: Objetivos Generales
layout: top-title-two-cols
color: amber-light

align: l-cm-lm
columns: is-5

transition: slide-left
---
:: title ::
# Objetivos Generales

:: right ::

<div class="flex flex-col py-4">
  <ul class="mb-4 space-y-2">
    <li><span class="text-amber-600 font-semibold">Propuesta:</span> Servidor HPC para LLMs con Enfoque SRE.</li>
  </ul>
  <div class="grid grid-cols-1 gap-4">
    <div class="rounded-xl shadow-lg p-4 bg-lime-100 border-l-8 border-lime-400 flex items-center">
      <span class="text-lime-700 font-semibold mr-2">OG1:</span>
      <span class="text-gray-800">Montaje y Configuración de Hardware.</span>
    </div>
    <div class="rounded-xl shadow-lg p-4 bg-red-100 border-l-8 border-red-400 flex items-center">
      <span class="text-red-700 font-semibold mr-2">OG2:</span>
      <span class="text-gray-800">Despliegue y Evaluación de LLM.</span>
    </div>
    <div class="rounded-xl shadow-lg p-4 bg-indigo-100 border-l-8 border-indigo-400 flex items-center">
      <span class="text-indigo-700 font-semibold mr-2">OG3:</span>
      <span class="text-gray-800">Gestión Operativa con Enfoque SRE.</span>
    </div>
  </div>
</div>

:: left ::

<div class="w-full flex justify-center items-center">
  <figure class="flex flex-col items-center">
    <img src="./images/goal.png" alt="Ilustración de objetivos alcanzados en el proyecto" style="max-width: 90%;" />
  </figure>
</div>


---
title: Preguntas de Investigación
layout: side-title
color: amber-light

side: right
titlewidth: is-3
align: lm-lm

transition: slide-left
---
:: title ::
# Preguntas de Investigación

:: content ::
<style>
.card-default {
  border: 2px solid #e5e7eb;
  border-radius: 1rem;
  background: #fff;
  box-shadow: 0 4px 16px 0 rgba(0,0,0,0.08);
  padding: 1.25rem;
  margin-bottom: 0.5rem;
}
@keyframes fadeLeftStairs-1 {
  from { opacity: 0; transform: translateX(-32px);}
  to { opacity: 1; transform: translateX(0);}
}
@keyframes fadeLeftStairs-2 {
  from { opacity: 0; transform: translateX(-32px);}
  to { opacity: 1; transform: translateX(0);}
}
@keyframes fadeLeftStairs-3 {
  from { opacity: 0; transform: translateX(-32px);}
  to { opacity: 1; transform: translateX(0);}
}
@keyframes fadeLeftStairs-4 {
  from { opacity: 0; transform: translateX(-32px);}
  to { opacity: 1; transform: translateX(0);}
}
.fade-left-stairs-1 {
  animation: fadeLeftStairs-1 1.2s cubic-bezier(0.4,0,0.2,1) 0s both;
  will-change: opacity, transform;
}
.fade-left-stairs-2 {
  animation: fadeLeftStairs-2 1.2s cubic-bezier(0.4,0,0.2,1) 0.2s both;
  will-change: opacity, transform;
}
.fade-left-stairs-3 {
  animation: fadeLeftStairs-3 1.2s cubic-bezier(0.4,0,0.2,1) 0.4s both;
  will-change: opacity, transform;
}
.fade-left-stairs-4 {
  animation: fadeLeftStairs-4 1.2s cubic-bezier(0.4,0,0.2,1) 0.6s both;
  will-change: opacity, transform;
}
</style>

<div class="flex flex-col py-12">
  <div class="grid grid-cols-2 gap-6 w-full">
    <div class="card-default flex flex-row items-start text-left min-h-[120px] w-full fade-left-stairs-1">
      <span class="font-bold text-amber-600 mr-2 mt-1">1.</span>
      <span>¿Qué ventajas y limitaciones presentan las estrategias de despliegue de LLM en HPC?</span>
    </div>
    <div class="card-default flex flex-row items-start text-left min-h-[120px] w-full fade-left-stairs-2">
      <span class="font-bold text-amber-600 mr-2 mt-1">2.</span>
      <span>¿Cómo afecta la cuantización avanzada al rendimiento y calidad de los modelos?</span>
    </div>
    <div class="card-default flex flex-row items-start text-left min-h-[120px] w-full fade-left-stairs-3">
      <span class="font-bold text-amber-600 mr-2 mt-1">3.</span>
      <span>¿Qué métricas y metodologías son más adecuadas para evaluar LLMs en HPC?</span>
    </div>
    <div class="card-default flex flex-row items-start text-left min-h-[120px] w-full fade-left-stairs-4">
      <span class="font-bold text-amber-600 mr-2 mt-1">4.</span>
      <span>¿Qué impacto tienen las prácticas SRE y la automatización en la robustez?</span>
    </div>
  </div>
</div>

---
title: Herramientas Clave
layout: top-title
side: l
color: amber-light

titlewidth: is-4
align: lm

transition: slide-left
---

:: title ::
# Herramientas Clave


:: content ::

<style>
@keyframes fadeUpStairs-1 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-2 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-3 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
.fade-up-stairs-1 {
  animation: fadeUpStairs-1 1.2s cubic-bezier(0.4,0,0.2,1) 0s both;
  will-change: opacity, transform;
}
.fade-up-stairs-2 {
  animation: fadeUpStairs-2 1.2s cubic-bezier(0.4,0,0.2,1) 0.3s both;
  will-change: opacity, transform;
}
.fade-up-stairs-3 {
  animation: fadeUpStairs-3 1.2s cubic-bezier(0.4,0,0.2,1) 0.6s both;
  will-change: opacity, transform;
}

@media print {
  .fade-up-stairs-1,
  .fade-up-stairs-2,
  .fade-up-stairs-3,
  .fade-up-stairs-4 {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
  }
}

</style>

<div class="flex flex-col items-center justify-center w-full min-h-[320px] py-12">
  <div class="grid grid-cols-3 gap-10">
    <div class="bg-gray-100 rounded-2xl shadow-lg p-6 flex flex-col items-center w-[240px] h-[240px] fade-up-stairs-1">
      <img src="./images/vllm.png" alt="vLLM" class="rounded-lg mb-4" style="max-width: 64px;" />
      <span class="font-bold text-gray-800 text-lg mt-2">vLLM</span>
      <span class="text-sm text-gray-600 text-center mt-2">Motor eficiente para inferencia de LLMs</span>
    </div>
    <div class="bg-gray-100 rounded-2xl shadow-lg p-6 flex flex-col items-center w-[240px] h-[240px] fade-up-stairs-2">
      <img src="./images/deepseek.png" alt="DeepSeek-Chat" class="rounded-lg mb-4" style="max-width: 64px;" />
      <span class="font-bold text-gray-800 text-lg mt-2">DeepSeek-Chat</span>
      <span class="text-sm text-gray-600 text-center mt-2">Modelo open source de alto rendimiento</span>
    </div>
    <div class="bg-gray-100 rounded-2xl shadow-lg p-6 flex flex-col items-center w-[240px] h-[240px] fade-up-stairs-3">
      <img src="./images/openshift.png" alt="OpenShift" class="rounded-lg mb-4" style="max-width: 64px;" />
      <span class="font-bold text-gray-800 text-lg mt-2">OpenShift</span>
      <span class="text-sm text-gray-600 text-center mt-2">Orquestador con enfoque SRE y escalabilidad</span>
    </div>
  </div>
</div>





---
title: Metodología y Enfoque
layout: top-title
side: l
color: amber-light

titlewidth: is-4
align: lm

transition: slide-left
---

:: title ::
# Metodología y Enfoque

:: content :: 
<style>
@keyframes fadeUpStairs-1 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-2 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-3 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-4 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-5 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
.fade-up-stairs-1 {
  animation: fadeUpStairs-1 1.2s cubic-bezier(0.4,0,0.2,1) 0s both;
  will-change: opacity, transform;
}
.fade-up-stairs-2 {
  animation: fadeUpStairs-2 1.2s cubic-bezier(0.4,0,0.2,1) 0.2s both;
  will-change: opacity, transform;
}
.fade-up-stairs-3 {
  animation: fadeUpStairs-3 1.2s cubic-bezier(0.4,0,0.2,1) 0.4s both;
  will-change: opacity, transform;
}
.fade-up-stairs-4 {
  animation: fadeUpStairs-4 1.2s cubic-bezier(0.4,0,0.2,1) 0.6s both;
  will-change: opacity, transform;
}
.fade-up-stairs-5 {
  animation: fadeUpStairs-5 1.2s cubic-bezier(0.4,0,0.2,1) 0.8s both;
  will-change: opacity, transform;
}

@media print {
  .fade-up-stairs-1,
  .fade-up-stairs-2,
  .fade-up-stairs-3,
  .fade-up-stairs-4 {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
  }
}
</style>

<div class="flex flex-col items-center w-full py-2 gap-6">
  <div class="flex flex-row flex-wrap justify-center items-center gap-6 mb-4">
    <div class="bg-gray-100 rounded-2xl shadow-lg flex flex-col items-center fade-up-stairs-1" style="width: 180px; height: 180px; padding: 1rem;">
      <img src="./images/notion.png" alt="Notion" class="rounded-lg mb-2" style="max-width: 64px;" />
      <span class="font-semibold text-gray-800 mt-2 mb-1">Notion</span>
      <span class="text-xs text-gray-600 text-center px-1 py-1">Gestión de tareas y documentación</span>
    </div>
    <div class="bg-gray-100 rounded-2xl shadow-lg flex flex-col items-center fade-up-stairs-2" style="width: 180px; height: 180px; padding: 1rem;">
      <img src="./images/oreilly.png" alt="O'Reilly" class="rounded-lg mb-2" style="max-width: 40px;" />
      <span class="font-semibold text-gray-800 mt-2 mb-1">O'Reilly</span>
      <span class="text-xs text-gray-600 text-center px-1 py-1">Guía de referencia técnica</span>
    </div>
    <div class="bg-gray-100 rounded-2xl shadow-lg flex flex-col items-center fade-up-stairs-3" style="width: 180px; height: 180px; padding: 1rem;">
      <img src="./images/clockify.png" alt="Clockify" class="rounded-lg mb-2" style="max-width: 40px;" />
      <span class="font-semibold text-gray-800 mt-2 mb-1">Clockify</span>
      <span class="text-xs text-gray-600 text-center px-1 py-1">Seguimiento de tiempos</span>
    </div>
  </div>
  <div class="flex flex-row flex-wrap justify-center items-center gap-6">
    <div class="bg-gray-100 rounded-2xl shadow-lg flex flex-col items-center fade-up-stairs-4" style="width: 180px; height: 180px; padding: 1rem;">
      <img src="./images/erasmus.png" alt="Erasmus" class="rounded-lg mb-2" style="max-width: 44px;" />
      <span class="font-semibold text-gray-800 mt-2 mb-1">Erasmus</span>
      <span class="text-xs text-gray-600 text-center px-1 py-1">Experiencia internacional en TI</span>
    </div>
    <div class="bg-gray-100 rounded-2xl shadow-lg flex flex-col items-center fade-up-stairs-5" style="width: 180px; height: 180px; padding: 1rem;">
      <img src="./images/redhat.png" alt="Red Hat" class="rounded-lg mb-2" style="max-width: 44px;" />
      <span class="font-semibold text-gray-800 mt-2 mb-1">Red Hat</span>
      <span class="text-xs text-gray-600 text-center px-1 py-1">Curso Red Hat Openshift D0180</span>
    </div>
  </div>
</div>

---
title: Metodología del Proyecto y Recursos de Apoyo II 
layout: full
color: amber-light

transition: slide-left
---

<div class="flex flex-col items-center justify-center w-full pt-4">
  <img src="./images/image70.png" alt="Diagrama de las horas registradas por Clockify" class="rounded-lg shadow-lg mb-4" style="max-width: 90%;" />
  <figcaption class="text-center text-sm mt-2" style="color: #f59e42; font-weight: 600;">
    Diagrama de las horas registradas por Clockify
  </figcaption>
</div>



---
title: Recursos y Costos Estimados

layout: top-title-two-cols
color: amber-light

align: l-lm-lm
columns: is-6

transition: slide-left
---
:: title ::
# Recursos y Costos Estimados

:: right ::
- <span class="text-amber-600 font-semibold">Hardware Principal:</span> GPU NVIDIA L40S y Servidor Dell PowerEdge R7615.
- <span class="text-amber-600 font-semibold">Costos Asociados:</span> Infraestructura adicional y horas de trabajo.
- <span class="text-amber-600 font-semibold">Estimación:</span> Proyecto de alto costo (&gt;10.000&nbsp;€).
- <span class="text-amber-600 font-semibold">Viabilidad:</span> Gracias al apoyo institucional.

:: left ::

<div class="w-full flex justify-center items-center py-2">
  <figure class="flex flex-col items-center">
    <img src="./images/image56.png" alt="Dell PowerEdge R7615 en el rack" class="rounded-lg shadow-lg mb-4" style="max-width: 65%;" />
      <figcaption class="text-center text-sm text-gray-600">
      Dell PowerEdge R7615 en el rack.
    </figcaption>
  </figure>
</div>

---
layout: cover
color: lime
---

# Montaje y Configuración de Hardware

:: note ::

\* Capítulo 4



---
title: Primer contacto con la infraestructura

layout: top-title-two-cols
color: lime-light

align: l-lm-cm
columns: is-5

transition: slide-left
---

:: title ::
# Primer contacto con la infraestructura

:: left ::

- <span class="text-lime-600 font-semibold">Servidor Asignado:</span> Dell PowerEdge R7615 con GPU NVIDIA L40S.
- <span class="text-lime-600 font-semibold">Puesta a Punto en el CTT:</span> Integración en el rack y conexión de red.



:: right :: 


<figure class="flex flex-col justify-center h-full">
  <img src="./images/image47.jpg" alt="Sala de servidores del CTT." class="rounded-lg shadow-lg my-2" style="max-width: 100%; margin-bottom: 0.3rem;" />
  <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
    Sala de servidores del CTT.
  </figcaption>
</figure>





---
title: Experiencia Práctica

layout: top-title-two-cols
color: lime-light

align: l-lm-cm
columns: is-5

transition: slide-left
---

:: title ::
# Experiencia Práctica


:: left ::
- <span class="text-lime-600 font-semibold">Montajes y Cableado en Racks:</span> Experiencia real 
- <span class="text-lime-600 font-semibold">Resolución de Incidencias</span>
- <span class="text-lime-600 font-semibold">Lección Clave SRE:</span> La Precaución y Seguridad en Operaciones Físicas.


:: right :: 
<div class="w-full flex justify-center items-center">
  <figure class="flex flex-col items-center">
    <img src="./images/intership.png" alt="Ilustración de objetivos alcanzados en el proyecto" style="max-width: 85%;" />
  </figure>
</div>


---
title: Metodología del Proyecto y Recursos de Apoyo II 
layout: full
color: white

transition: slide-left
---

<style>
@keyframes fadeUpStairs-1 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-2 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-3 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
.fade-up-stairs-1 {
  animation: fadeUpStairs-1 1.2s cubic-bezier(0.4,0,0.2,1) 0s both;
  will-change: opacity, transform;
}
.fade-up-stairs-2 {
  animation: fadeUpStairs-2 1.2s cubic-bezier(0.4,0,0.2,1) 0.3s both;
  will-change: opacity, transform;
}
.fade-up-stairs-3 {
  animation: fadeUpStairs-3 1.2s cubic-bezier(0.4,0,0.2,1) 0.6s both;
  will-change: opacity, transform;
}

@media print {
  .fade-up-stairs-1,
  .fade-up-stairs-2,
  .fade-up-stairs-3,
  .fade-up-stairs-4 {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
  }
}
</style>

<div class="flex flex-row items-start justify-center w-full pt-5 space-x-8">
  <div class="flex flex-col items-center fade-up-stairs-1">
    <img src="./images/image15.jpg" alt="Diagrama 1" class="rounded-lg shadow-lg mb-4" style="max-width: 280px;" />
    <figcaption class="text-center text-sm mt-2 text-lime-600 font-semibold">
      Supermicro as-4124gs-tnr-03-wa0004 en Desion
    </figcaption>
  </div>
  <div class="flex flex-col items-center fade-up-stairs-2">
    <img src="./images/image17.jpg" alt="Diagrama 2" class="rounded-lg shadow-lg mb-4" style="max-width: 280px;" />
    <figcaption class="text-center text-sm mt-2 text-lime-600 font-semibold">
      Rack de Servidores de Schwechat (Austria)
    </figcaption>
  </div>
  <div class="flex flex-col items-center fade-up-stairs-3">
    <img src="./images/image52.jpg" alt="Diagrama 3" class="rounded-lg shadow-lg mb-4" style="max-width:  280px;" />
    <figcaption class="text-center text-sm mt-2 text-lime-600 font-semibold">
       Supermicro con 2 GPU 3090 en Desion
    </figcaption>
  </div>
</div>



---
title: Acceso Remoto al Servidor Adaptación y Automatización
layout: top-title
side: l
color: lime-light

titlewidth: is-4
align: lm

transition: slide-left
---
:: title ::
# Acceso Remoto al Servidor

:: content ::

- <span class="text-lime-600 font-semibold">Desafío:</span> Conexión segura desde ubicación remota.
- <span class="text-lime-600 font-semibold">Solución Implementada:</span> Conexión SSH con doble salto.
- <span class="text-lime-600 font-semibold">Enfoque SRE:</span> Automatización del proceso (a través de <code>~/.ssh/config</code>).

<div class="w-full flex justify-center items-center pt-12">
  <figure class="flex flex-col items-center">
    <img src="./images/diagrama.png" alt="Experiencia Erasmus y OpenShift" class="rounded-lg shadow-lg mb-4" style="max-width: 100%;" />
    <figcaption class="text-center text-sm text-gray-600 mt-2">
      Diagrama conexion SSH
    </figcaption>
  </figure>
</div>

---
title: Puesta a Punto del Sistema Operativo y Drivers

layout: top-title-two-cols
color: lime-light

align: l-lm-cm
columns: is-4

transition: slide-left
---

:: title ::
# Puesta a Punto del Sistema Operativo y Drivers

:: left ::

- <span class="text-lime-600 font-semibold">SO:</span> Fedora Server <img src="./images/fedora.png" alt="Fedora Logo" style="display:inline; vertical-align:middle; max-width:24px; margin-left:4px;" />
- <span class="text-lime-600 font-semibold">Soporte GPU:</span> Driver NVIDIA 570.133.07 y CUDA Toolkit 12.8 <img src="./images/cuda.png" alt="CUDA Logo" style="display:inline; vertical-align:middle; max-width:45px; margin-left:3px;" />
- <span class="text-lime-600 font-semibold">Problemas:</span> Manejo de reinicios y configuración de Secure Boot.



:: right :: 
<figure class="flex flex-col justify-center h-full">
  <img src="./images/image6.png" alt="Comparativa de rendimiento de modelos estadounidenses y chinos en LMSYS Chatbot Arena" class="rounded-lg shadow-lg my-8" style="max-width: 100%; margin-bottom: 0.3rem;" />
  <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
    nvidia-smi output
  </figcaption>
</figure>

---
layout: cover
color: red
---

# Despliegue y Evaluación de LLM

:: note ::

\* Capítulo 5 y 6


---
title: Comparativa de LLM

layout: top-title-two-cols
color: red-light

align: l-cm-lm
columns: is-8

transition: slide-left
---

:: title ::
# Comparativa de LLM

:: left ::

<figure class="flex flex-col justify-center h-full">
  <img src="./images/LLM.jpg" alt=" Vision Conceptual de un LLM" class="rounded-lg shadow-lg my-8" style="max-width: 100%; margin-bottom: 0.3rem;" />
  <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
    Vision Conceptual de un LLM
  </figcaption>
</figure>

:: right :: 
- <span class="text-red-600 font-semibold">Modelos:</span> DeepSeek-Chat (67B y 7B) en GPU NVIDIA L40S (48&nbsp;GB VRAM). Comparar ambos.
- <span class="text-red-600 font-semibold">Solución Inicial:</span> Despliegue con Podman (Alternativa a Docker, Modo Rootless).
- <span class="text-red-600 font-semibold">Desafío Principal:</span> Requisitos de VRAM (67B en FP16 &gt; 120&nbsp;GB).


---
title: Cuantización 

layout: side-title
color: red-light
side: l
titlewidth: is-4
align: lm-lm

transition: slide-left
---

:: title ::
# ¿Cómo optimizar un modelo que no cabe?

:: content ::

- <span class="text-red-600 font-bold">Cuantización </span>INT4: QLoRA
- Reducción de <span class="text-red-600 font-bold">124&nbsp;GB → 31&nbsp;GB</span>
- <span class="text-red-600 font-bold">vLLM + PagedAttention</span> → inferencia concurrente
- <span class="text-red-600 font-bold">Resultado:</span> Ejecución estable del modelo 67B


<div class="w-full flex justify-center items-center">
  <figure class="flex flex-col items-center">
    <img src="./images/quantization.png" alt="Concepto de Cuantificación" class="rounded-lg shadow-lg mb-8 mt-3" style="max-width: 60%; margin-bottom: 0.3rem;" />
    <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
      Concepto de Cuantificación
    </figcaption>
  </figure>
</div>


<!--  
* La imagen ilustra el concepto de cuantificación mostrando cómo un rango continuo de valores (representado por la curva negra y los puntos morados para FP32) se mapea a un conjunto discreto y limitado de valores (representado por los puntos rojos en las cajas INT4).
 *
 * Específicamente:
 *
 * - FP32 (Punto Flotante de 32 bits): La parte superior de la imagen, etiquetada como "FP32", representa valores con alta precisión. La curva negra suave simboliza una distribución continua de posibles valores, y los puntos morados en la curva representan valores específicos en este formato de mayor precisión.
 * - INT4 (Entero de 4 bits): La parte inferior, etiquetada como "INT4", muestra el resultado de la cuantificación, donde los valores se reducen a un formato entero de menor precisión (enteros de 4 bits). Las flechas grises discontinuas indican que los valores originales de FP32 se redondean o se mapean al valor discreto INT4 más cercano disponible. Los puntos rojos dentro de las cajas vacías representan estos valores cuantificados. Las cajas en blanco indican que algunos valores de la distribución continua original pueden mapearse al mismo valor cuantificado, o que hay menos valores únicos disponibles en la representación INT4 en comparación con FP32.
 *
 * En el contexto de los LLMs, esta imagen explica visualmente cómo los pesos y las activaciones de un modelo de lenguaje grande, que normalmente utilizan números de punto flotante de alta precisión (como FP32), se convierten en enteros de menor precisión (como INT4). Este proceso, conocido como cuantificación, reduce significativamente el tamaño del modelo y el uso de memoria, haciéndolo más eficiente para el despliegue y la inferencia, especialmente en hardware con recursos limitados. 
 * -->

---
title: Port Forwarding
layout: top-title
side: l
color: red-light

titlewidth: is-2
align: lm

transition: slide-left
---
:: title ::
# Port Forwarding

:: content ::
<div class="flex flex-row w-full pt-2 gap-6">
  <!-- Columna izquierda: texto y diagrama, ahora más estrecha -->
  <div class="flex flex-col w-1/2 min-w-0">
    <div class="mb-4">
      <ul class="list-disc pl-5">
        <li>
          <span class="text-red-600 font-semibold">Acceso a la API:</span> (localhost:8000) del LLM desde máquina local.
        </li>
        <li>
          <span class="text-red-600 font-semibold">Implementación:</span> SSH Tunneling para redirección de puerto.
        </li>
        <li>
          <span class="text-red-600 font-semibold">Ventaja:</span> Acceso seguro y directo al servicio LLM.
        </li>
      </ul>
    </div>
    <div class="flex flex-col items-center justify-center">
      <figure class="flex flex-col items-center w-full">
        <img src="./images/diagrama2.png" alt="Diagrama conexión SSH" class="rounded-lg shadow-lg mb-2" style="max-width: 90%; height: auto;" />
      </figure>
    </div>
  </div>
  <!-- Columna derecha: imagen fastapi más grande y centrada verticalmente -->
  <div class="flex flex-col w-1/2 items-end justify-center">
    <figure class="flex flex-col items-center w-full">
      <img src="./images/image63.png" alt="Terminal SSH / FastAPI" class="rounded-lg shadow-lg mb-2" style="max-width: 400px; height: 360px; object-fit: contain; margin-top: 0.5rem;" />
      <figcaption class="text-center text-sm text-gray-600 mt-2">
        Terminal SSH mostrando FastAPI en ejecución
      </figcaption>
    </figure>
  </div>
</div>

---
title: Evaluación de Rendimiento Metodología

layout: top-title-two-cols
color: red-light

align: l-lm-cm
columns: is-6

transition: slide-left
---

:: title ::
# Evaluación de Rendimiento: Metodología

:: left ::
<ul class="space-y-2 list-disc ml-6 pt-10">
  <li><span class="text-red-600 font-semibold">Métricas Clave:</span> Throughput (TPS), latencia y tasa de error.</li>
  <li><span class="text-red-600 font-semibold">Herramienta:</span> Apache JMeter para simular usuarios concurrentes.</li>
  <li><span class="text-red-600 font-semibold">Acceso:</span> Túnel SSH para redirección segura de puertos.</li>
  <li><span class="text-red-600 font-semibold">Formula TPS</span></li>
</ul>

<div style="padding-top: 1em;"></div>

<span style="font-size: 0.75em;">
$$
\mathrm{TPS} = \frac{\text{Solicitudes}}{\text{segundo}} \times \left( \text{tokens}_{\text{prompt}} + \text{tokens}_{\text{respuesta}} \right)
$$
</span>


:: right :: 
<figure class="flex flex-col justify-center h-full">
  <img src="./images/image50-2.png" alt="Comparativa de rendimiento de modelos estadounidenses y chinos en LMSYS Chatbot Arena" class="rounded-lg shadow-lg my-8" style="max-width: 100%; margin-bottom: 0.3rem;" />
  <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
    JMeter Benchmarking
  </figcaption>
</figure>



---
title: Escenarios de Prueba 

layout: top-title
side: l
color: red-light

titlewidth: is-4
align: lm

transition: slide-left
---
:: title ::
# Escenarios de Prueba 

:: content ::

<style>
@keyframes fadeUpStairs-1 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-2 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-3 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
.fade-up-stairs-1 {
  animation: fadeUpStairs-1 1.2s cubic-bezier(0.4,0,0.2,1) 0s both;
  will-change: opacity, transform;
}
.fade-up-stairs-2 {
  animation: fadeUpStairs-2 1.2s cubic-bezier(0.4,0,0.2,1) 0.3s both;
  will-change: opacity, transform;
}
.fade-up-stairs-3 {
  animation: fadeUpStairs-3 1.2s cubic-bezier(0.4,0,0.2,1) 0.6s both;
  will-change: opacity, transform;
}

@media print {
  .fade-up-stairs-1,
  .fade-up-stairs-2,
  .fade-up-stairs-3,
  .fade-up-stairs-4 {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
  }
}
</style>

<div class="flex flex-row justify-center items-center gap-8 py-12">
  <div class="fade-up-stairs-1 bg-red-100 border-l-8 border-red-400 rounded-2xl shadow-lg p-6 flex flex-col items-start" style="width: 320px; min-height: 170px;">
    <span class="text-red-600 font-semibold text-lg mb-2">Escenario A</span>
    <span class="text-gray-800">
      Evaluación de Latencia y Consistencia<br>
      <span class="text-sm text-gray-600">Respuestas Cortas (32 tokens) y Carga Baja (10–20 hilos)</span>
    </span>
  </div>
  <div class="fade-up-stairs-2 bg-red-200 border-l-8 border-red-500 rounded-2xl shadow-lg p-6 flex flex-col items-start" style="width: 320px; min-height: 170px;">
    <span class="text-red-700 font-semibold text-lg mb-2">Escenario B</span>
    <span class="text-gray-800">
      Evaluación de Estabilidad<br>
      <span class="text-sm text-gray-600">Respuestas Medias-Largas (64–256 tokens) y Carga Media (15 hilos)</span>
    </span>
  </div>
  <div class="fade-up-stairs-3 bg-red-300 border-l-8 border-red-600 rounded-2xl shadow-lg p-6 flex flex-col items-start" style="width: 320px; min-height: 235px;">
    <span class="text-red-800 font-semibold text-lg mb-2">Escenario C</span>
    <span class="text-gray-800">
      Búsqueda del Throughput Máximo<br>
      <span class="text-sm text-gray-600">Respuestas Largas y Carga Alta (hasta 50 hilos)</span>
    </span>
  </div>
</div>

:: left ::



---
title: Resultados Latencia

layout: top-title-two-cols
color: red-light

align: l-lm-cm
columns: is-5

transition: slide-left
---

:: title ::
# Resultados: Latencia

:: left ::

- <span class="text-red-600 font-semibold">Modelo 7B:</span> Latencia significativamente menor y más estable.
- <span class="text-red-600 font-semibold">Modelo 67B:</span> Aumento exponencial de latencia con la carga.
- <span class="italic text-gray-600">Lower is better</span>


:: right :: 
<figure class="flex flex-col justify-center h-full">
  <img src="./images/image61.png" alt="Comparativa de rendimiento de modelos estadounidenses y chinos en LMSYS Chatbot Arena" class="rounded-lg shadow-lg my-8" style="max-width: 100%; margin-bottom: 0.3rem;" />
  <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
    Grafica Resultados Latencia
  </figcaption>
</figure>

---
title: Resultados Throughput (TPS)


layout: top-title-two-cols
color: red-light

align: l-lm-cm
columns: is-5

transition: slide-left
---

:: title ::
# Resultados: Throughput (TPS)

:: left ::
- <span class="text-red-600 font-semibold">Modelo 7B:</span> Alto throughput y escalabilidad superior.
- <span class="text-red-600 font-semibold">Modelo 67B:</span> Throughput limitado.
- <span class="italic text-gray-600">Higher is better</span>


:: right :: 
<figure class="flex flex-col justify-center h-full">
  <img src="./images/image3.png" alt="Comparativa de rendimiento de modelos estadounidenses y chinos en LMSYS Chatbot Arena" class="rounded-lg shadow-lg my-8" style="max-width: 100%; margin-bottom: 0.3rem;" />
  <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
    Grafica Resultados TPS
  </figcaption>
</figure>

---
title: Conclusiones de la Evaluación de Rendimiento
layout: top-title-two-cols
color: red-light

align: l-cm-lm
columns: is-6

transition: slide-left
---
:: title ::
# Conclusiones de la Evaluación de Rendimiento

:: right ::

- <span class="text-red-600 font-semibold">¿Son resultados plausibles?</span> Pensamiento crítico.
- <span class="text-red-600 font-semibold">Visto:</span> 100% uso GPU y ~96% VRAM en todos los escenarios del 67B (según NVIDIA-SMI).
- <span class="text-red-600 font-semibold">Compromiso:</span> Trade-off claro entre el tamaño del modelo y la eficiencia.

:: left ::

<div class="w-full flex justify-center items-center">
  <figure class="flex flex-col items-center">
    <img src="./images/question.png" alt="Ilustración de objetivos alcanzados en el proyecto" style="max-width: 85%;" />
  </figure>
</div>

---
layout: cover
color: indigo
---

# Gestión Operativa con Enfoque SRE

:: note ::

\* Capítulo 7

---
title: ¿Por qué OpenShift?

layout: top-title-two-cols
color: indigo-light

align: l-lm-cm
columns: is-4

transition: slide-left
---

:: title ::
# ¿Por qué OpenShift?

:: left ::
- <span class="text-indigo-600 font-semibold">Limitaciones de Despliegue Manual:</span> Falta de monitoreo, recuperación y escalado automático.
- <span class="text-indigo-600 font-semibold">Alineado con la filosofía SRE.</span> 

:: right :: 
<figure class="flex flex-col justify-center h-full">
  <img src="./images/ejemplo.png" alt="Comparativa de rendimiento de modelos estadounidenses y chinos en LMSYS Chatbot Arena" class="rounded-lg shadow-lg my-8" style="max-width: 100%; margin-bottom: 0.3rem;" />
</figure>

---
title: Gestión Operativa Transición a OpenShift 

layout: top-title-two-cols
color: indigo-light

align: l-lm-cm
columns: is-5

transition: slide-left
---

:: title ::
# Gestión Operativa: Transición a OpenShift 

:: left ::
- <span class="text-indigo-600 font-semibold">Más que Kubernetes</span>
- <span class="text-indigo-600 font-semibold">Características Clave:</span> Declarativa, Reproducible, Escalable.
- <span class="text-indigo-600 font-semibold">Funcionalidades Integradas:</span> Autoescalado, Probes de Salud, CI/CD, Namespaces, Métricas (Prometheus, Grafana).
- <span class="text-indigo-600 font-semibold">Ideal para:</span> Servicios Fiables y Mantenibles.

:: right :: 
<figure class="flex flex-col justify-center h-full">
  <img src="./images/image40.png" alt="Proyectos de código abierto que hay en OpenShift" class="rounded-lg shadow-lg my-8" style="max-width: 100%; margin-bottom: 0.3rem;" />
  <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
     Proyectos de código abierto que hay en OpenShift
  </figcaption>
</figure>




---
title: Despliegue paso a paso

title: Herramientas Clave
layout: top-title
side: l
color: indigo-light

titlewidth: is-4
align: lm

transition: slide-left
---

:: title ::
# Despliegue paso a paso

:: content ::

<div class="flex flex-row justify-center items-center gap-8">
  <div class="flex flex-col items-center w-1/2">
    <img src="./images/image66.png" alt="Primer Pod creado" class="rounded-lg shadow-lg my-8" style="width: 380px; height: 270px; object-fit: cover; margin-bottom: 0.3rem;" />
    <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
      oc new-app https://github.com/sclorg/nodejs-ex --name=nodejs-ex
    </figcaption>
  </div>
  <div class="flex flex-col items-center w-1/2">
    <img src="./images/image44.png" alt="Aplicación desplegada pero no se puede interactuar" class="rounded-lg shadow-lg my-8" style="width: 380px; height: 270px; object-fit: cover; margin-bottom: 0.3rem;" />
    <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
      oc expose service nodejs-ex 
    </figcaption>
  </div>
</div>

---
title: Despliegue paso a paso

layout: top-title
side: l
color: indigo-light

titlewidth: is-4
align: lm

transition: slide-left
---

:: title ::
# Despliegue paso a paso II 

:: content ::

<div class="flex flex-row justify-center items-center gap-8">
  <div class="flex flex-col items-center w-1/2">
    <img src="./images/image31.png" alt="Primer Pod creado" class="rounded-lg shadow-lg my-8" style="width: 380px; height: 270px; object-fit: cover; margin-bottom: 0.3rem;" />
    <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
      oc new-app postgresql-persistent ...
    </figcaption>
  </div>
  <div class="flex flex-col items-center w-1/2">
    <img src="./images/image53.png" alt="Aplicación desplegada pero no se puede interactuar" class="rounded-lg shadow-lg my-8" style="width: 380px; height: 270px; object-fit: cover; margin-bottom: 0.3rem;" />
    <figcaption class="text-center text-sm text-gray-600" style="margin-top: 0.7rem;">
      Aplicación desplegada 
    </figcaption>
  </div>
</div>

---
title: Autoescalado y recuperación comportamiento esperado

layout: top-title
side: l
color: indigo-light

titlewidth: is-4
align: lm

transition: slide-left
---

:: title ::
# oc autoscale

:: content ::
<div class="flex flex-row flex-wrap justify-center items-start gap-6">

  <figure class="flex flex-col items-center w-[320px]">
    <img src="./images/image65.png" alt="HPA incrementa a 3 réplicas" class="rounded-lg shadow-lg my-4" style="width: 100%; max-width: 320px; height: auto;" />
    <figcaption class="text-center text-sm text-gray-600 mt-2">
      El HPA incrementa a 3 réplicas tras mantener la carga al 200&nbsp;%.
    </figcaption>
  </figure>

  <figure class="flex flex-col items-center w-[320px]">
    <img src="./images/image45.png" alt="Estado de los pods durante la prueba de carga" class="rounded-lg shadow-lg my-4" style="width: 100%; max-width: 320px; height: auto;" />
    <figcaption class="text-center text-sm text-gray-600 mt-2">
      Estado de los pods durante la prueba de carga
    </figcaption>
  </figure>

  <figure class="flex flex-col items-center w-[320px]">
    <img src="./images/image33.png" alt="Monitorización de los pods durante la prueba de carga" class="rounded-lg shadow-lg my-4" style="width: 100%; max-width: 320px; height: auto;" />
    <figcaption class="text-center text-sm text-gray-600 mt-2">
      Monitorización de los pods durante la prueba de carga
    </figcaption>
  </figure>

  <figure class="flex flex-col items-center w-[320px]">
    <img src="./images/image51.png" alt="Decrecimiento del autoescalado tras la prueba de carga" class="rounded-lg shadow-lg my-4" style="width: 100%; max-width: 320px; height: auto;" />
    <figcaption class="text-center text-sm text-gray-600 mt-2">
      Decrecimiento del autoescalado tras la prueba de carga.
    </figcaption>
  </figure>

</div>



---
title: Autoescalado y recuperación comportamiento esperado

layout: top-title
side: l
color: indigo-light

titlewidth: is-4
align: lm

transition: slide-left
---

:: title ::
# oc set probe + oc set triggers

:: content ::
<div class="flex flex-row justify-center items-start gap-8 mb-6">
  <figure class="flex flex-col items-center w-[320px]">
    <img src="./images/image7.png" alt="Decrecimiento del autoescalado tras la prueba de carga" class="rounded-lg shadow-lg my-4" style="width: 100%; max-width: 320px; height: auto;" />
    <figcaption class="text-center text-sm text-gray-600 mt-2">
      Estado CrashLoopBackOff tras fallo en la sonda de readiness 
    </figcaption>
  </figure>
  <figure class="flex flex-col items-center w-[320px]">
    <img src="./images/image2.png" alt="Decrecimiento del autoescalado tras la prueba de carga" class="rounded-lg shadow-lg my-4" style="width: 100%; max-width: 320px; height: auto;" />
    <figcaption class="text-center text-sm text-gray-600 mt-2">
      Aplicacion no disponible por culpa del cambio de puerto
    </figcaption>
  </figure>
</div>

<div class="w-full flex justify-center items-center">
  <code>oc set triggers bc/nodejs-ex --from-github=true --auto</code>
</div>

---
title: Conclusiones Finales

layout: top-title
side: l
color: amber-light

titlewidth: is-4
align: lm

transition: slide-left
---

:: title ::
# Conclusiones Finales

:: content ::
<style>
@keyframes fadeUpStairs-1 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-2 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-3 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUpStairs-4 {
  from { opacity: 0; transform: translateY(32px);}
  to { opacity: 1; transform: translateY(0);}
}
.fade-up-stairs-1 {
  animation: fadeUpStairs-1 1.2s cubic-bezier(0.4,0,0.2,1) 0s both;
  will-change: opacity, transform;
}
.fade-up-stairs-2 {
  animation: fadeUpStairs-2 1.2s cubic-bezier(0.4,0,0.2,1) 0.2s both;
  will-change: opacity, transform;
}
.fade-up-stairs-3 {
  animation: fadeUpStairs-3 1.2s cubic-bezier(0.4,0,0.2,1) 0.4s both;
  will-change: opacity, transform;
}
.fade-up-stairs-4 {
  animation: fadeUpStairs-4 1.2s cubic-bezier(0.4,0,0.2,1) 0.6s both;
  will-change: opacity, transform;
}

@media print {
  .fade-up-stairs-1,
  .fade-up-stairs-2,
  .fade-up-stairs-3,
  .fade-up-stairs-4 {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
  }
}
</style>

<div class="flex flex-row items-stretch justify-center gap-8 py-6">
  <!-- Infraestructura -->
  <div class="flex flex-col items-center flex-1 min-w-[170px] max-w-[200px] fade-up-stairs-1">
    <div class="flex items-center justify-center w-14 h-14 bg-green-100 rounded-full border-2 border-green-400 mb-3 text-2xl">
      ✔️
    </div>
    <div class="w-full flex flex-col justify-center items-center rounded-xl shadow px-4 py-4 bg-lime-100 border-l-4 border-lime-400" style="aspect-ratio: 1/1;">
      <span class="text-lime-700 font-semibold text-base mb-2">Infraestructura</span>
      <span class="text-gray-800 text-center text-sm">Servidor HPC funcional con GPU L40S.</span>
    </div>
  </div>
  <!-- Contenedores -->
  <div class="flex flex-col items-center flex-1 min-w-[150px] max-w-[200px] fade-up-stairs-2">
    <div class="flex items-center justify-center w-14 h-14 bg-red-100 rounded-full border-2 border-red-400 mb-3 text-2xl">
      🤖
    </div>
    <div class="w-full flex flex-col justify-center items-center rounded-xl shadow px-4 py-4 bg-red-100 border-l-4 border-red-400" style="aspect-ratio: 1/1;">
      <span class="text-red-700 font-semibold text-base mb-2">Contenedores</span>
      <span class="text-gray-800 text-center text-sm">Ejecución de LLMs (67B y 7B) en contenedores.</span>
    </div>
  </div>
  <!-- Benchmarking -->
  <div class="flex flex-col items-center flex-1 min-w-[150px] max-w-[200px] fade-up-stairs-3">
    <div class="flex items-center justify-center w-14 h-14 bg-red-100 rounded-full border-2 border-red-400 mb-3 text-2xl">
      📊
    </div>
    <div class="w-full flex flex-col justify-center items-center rounded-xl shadow px-4 py-4 bg-red-100 border-l-4 border-red-400" style="aspect-ratio: 1/1;">
      <span class="text-red-700 font-semibold text-base mb-2">Benchmarking</span>
      <span class="text-gray-800 text-center text-sm">Evaluación realista del rendimiento.</span>
    </div>
  </div>
  <!-- Automatización -->
  <div class="flex flex-col items-center flex-1 min-w-[150px] max-w-[200px] fade-up-stairs-4">
    <div class="flex items-center justify-center w-14 h-14 bg-indigo-100 rounded-full border-2 border-indigo-400 mb-3 text-2xl">
      ⚙️
    </div>
    <div class="w-full flex flex-col justify-center items-center rounded-xl shadow px-4 py-4 bg-indigo-100 border-l-4 border-indigo-400" style="aspect-ratio: 1/1;">
      <span class="text-indigo-700 font-semibold text-base mb-2">Automatización</span>
      <span class="text-gray-800 text-center text-sm">Orquestación con enfoque SRE.</span>
    </div>
  </div>
</div>

---
title: Trabajo a Futuro
layout: side-title
color: amber-light

side: right
titlewidth: is-3
align: lm-lm

transition: slide-left
---
:: title ::
# Trabajo a Futuro

:: content ::
<style>
@keyframes fadeLeftStairs-1 {
  from { opacity: 0; transform: translateX(-32px);}
  to { opacity: 1; transform: translateX(0);}
}
@keyframes fadeLeftStairs-2 {
  from { opacity: 0; transform: translateX(-32px);}
  to { opacity: 1; transform: translateX(0);}
}
@keyframes fadeLeftStairs-3 {
  from { opacity: 0; transform: translateX(-32px);}
  to { opacity: 1; transform: translateX(0);}
}
@keyframes fadeLeftStairs-4 {
  from { opacity: 0; transform: translateX(-32px);}
  to { opacity: 1; transform: translateX(0);}
}
.fade-left-stairs-1 {
  animation: fadeLeftStairs-1 1.2s cubic-bezier(0.4,0,0.2,1) 0s both;
  will-change: opacity, transform;
}
.fade-left-stairs-2 {
  animation: fadeLeftStairs-2 1.2s cubic-bezier(0.4,0,0.2,1) 0.2s both;
  will-change: opacity, transform;
}
.fade-left-stairs-3 {
  animation: fadeLeftStairs-3 1.2s cubic-bezier(0.4,0,0.2,1) 0.4s both;
  will-change: opacity, transform;
}
.fade-left-stairs-4 {
  animation: fadeLeftStairs-4 1.2s cubic-bezier(0.4,0,0.2,1) 0.6s both;
  will-change: opacity, transform;
}

@media print {
  .fade-up-stairs-1,
  .fade-up-stairs-2,
  .fade-up-stairs-3,
  .fade-up-stairs-4 {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
  }
}
</style>

<div class="flex flex-col gap-6 py-2 items-start justify-start">
  <div class="flex flex-row w-full max-w-[700px] fade-left-stairs-1">
    <div class="flex flex-row items-center w-full rounded-xl shadow px-4 py-4 bg-amber-100 border-l-4 border-amber-400" style="aspect-ratio: 8/1; min-height: 68px;">
      <span class="text-amber-700 font-semibold text-base mr-2">Escalabilidad</span>
      <span class="text-xl mr-3">🖥️</span>
      <span class="text-gray-800 text-left text-sm">Ampliar el sistema con más GPUs o nodos HPC.</span>
    </div>
  </div>
  <div class="flex flex-row w-full max-w-[700px] fade-left-stairs-2">
    <div class="flex flex-row items-center w-full rounded-xl shadow px-4 py-4 bg-amber-100 border-l-4 border-amber-400" style="aspect-ratio: 8/1; min-height: 68px;">
      <span class="text-amber-700 font-semibold text-base mr-2">Multi-Modelo</span>
      <span class="text-xl mr-3">🧩</span>
      <span class="text-gray-800 text-left text-sm">Comparar despliegue de varios modelos simultáneos usando Triton.</span>
    </div>
  </div>
  <div class="flex flex-row w-full max-w-[700px] fade-left-stairs-3">
    <div class="flex flex-row items-center w-full rounded-xl shadow px-4 py-4 bg-amber-100 border-l-4 border-amber-400" style="aspect-ratio: 8/1; min-height: 68px;">
      <span class="text-amber-700 font-semibold text-base mr-2">Bare Metal</span>
      <span class="text-xl mr-3">🛠️</span>
      <span class="text-gray-800 text-left text-sm">Instalar OpenShift bare metal para soporte completo de GPU.</span>
    </div>
  </div>
  <div class="flex flex-row w-full max-w-[700px] fade-left-stairs-4">
    <div class="flex flex-row items-center w-full rounded-xl shadow px-4 py-4 bg-amber-100 border-l-4 border-amber-400" style="aspect-ratio: 8/1; min-height: 68px;">
      <span class="text-amber-700 font-semibold text-base mr-2">SRE Avanzado</span>
      <span class="text-xl mr-3">⚙️</span>
      <span class="text-gray-800 text-left text-sm">Profundizar en prácticas SRE y explorar despliegues más complejos en OpenShift.</span>
    </div>
  </div>
</div>

---
layout: cover
color: amber
---

# ¡Gracias por vuestra atención!


<span style="font-size: 1.2em; font-weight: normal;">
  Fin de la presentación.<br>
  ¿Preguntas o comentarios?
</span>


:: note ::



