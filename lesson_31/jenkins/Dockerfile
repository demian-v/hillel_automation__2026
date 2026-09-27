# Образ Jenkins для ДЗ 31: Python, браузер для Playwright, Allure CLI,
# плагіни та вся конфігурація як код (без майстра першого запуску).
FROM jenkins/jenkins:lts-jdk21

USER root

# Python, щоб пайплайн міг створити venv і поставити залежності
RUN apt-get update \
 && apt-get install -y --no-install-recommends python3 python3-venv python3-pip \
 && rm -rf /var/lib/apt/lists/*

# Chromium для Playwright і його системні бібліотеки.
# Версія playwright має збігатися з lesson_31/requirements.txt —
# тоді пайплайн знайде вже встановлений браузер і не качатиме його щоразу.
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
RUN python3 -m venv /opt/playwright \
 && /opt/playwright/bin/pip install --no-cache-dir playwright==1.62.0 \
 && /opt/playwright/bin/playwright install --with-deps chromium \
 && rm -rf /opt/playwright /var/lib/apt/lists/* \
 && chown -R jenkins:jenkins /ms-playwright

# Allure CLI — ним плагін Allure генерує звіт
ARG ALLURE_VERSION=2.30.0
RUN curl -fsSL "https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz" \
    | tar -xz -C /opt \
 && mv "/opt/allure-${ALLURE_VERSION}" /opt/allure

USER jenkins

# Плагіни
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# Configuration as Code: користувач, інструмент Allure і сама джоба
COPY casc.yaml /usr/share/jenkins/casc.yaml
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/casc.yaml
ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=false
