{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/velaz7/Demographic-data-Analyzer/blob/main/demographic_data_analyzer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1WLdGJODphJp"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import plotly.express as px"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Import the data\n",
        "url = 'https://raw.githubusercontent.com/JakubPyt/Demographic_Data_Analyzer/main/adult.data.csv'\n",
        "data = pd.read_csv(url, sep=\";\")\n",
        "\n",
        "# Display first five rows of dataset\n",
        "data.head()\n",
        "data.tail()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "luEb5P-Fv4mZ",
        "outputId": "64c20b9f-67d5-4da9-d8ed-59a274687419"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       age     workclass  fnlwgt   education  education-num  \\\n",
              "32556   27       Private  257302  Assoc-acdm             12   \n",
              "32557   40       Private  154374     HS-grad              9   \n",
              "32558   58       Private  151910     HS-grad              9   \n",
              "32559   22       Private  201490     HS-grad              9   \n",
              "32560   52  Self-emp-inc  287927     HS-grad              9   \n",
              "\n",
              "           marital-status         occupation relationship   race     sex  \\\n",
              "32556  Married-civ-spouse       Tech-support         Wife  White  Female   \n",
              "32557  Married-civ-spouse  Machine-op-inspct      Husband  White    Male   \n",
              "32558             Widowed       Adm-clerical    Unmarried  White  Female   \n",
              "32559       Never-married       Adm-clerical    Own-child  White    Male   \n",
              "32560  Married-civ-spouse    Exec-managerial         Wife  White  Female   \n",
              "\n",
              "       capital-gain  capital-loss  hours-per-week native-country salary  \n",
              "32556             0             0              38  United-States  <=50K  \n",
              "32557             0             0              40  United-States   >50K  \n",
              "32558             0             0              40  United-States  <=50K  \n",
              "32559             0             0              20  United-States  <=50K  \n",
              "32560         15024             0              40  United-States   >50K  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a2ff4535-f47b-496d-8c42-dfb8d687efb8\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>age</th>\n",
              "      <th>workclass</th>\n",
              "      <th>fnlwgt</th>\n",
              "      <th>education</th>\n",
              "      <th>education-num</th>\n",
              "      <th>marital-status</th>\n",
              "      <th>occupation</th>\n",
              "      <th>relationship</th>\n",
              "      <th>race</th>\n",
              "      <th>sex</th>\n",
              "      <th>capital-gain</th>\n",
              "      <th>capital-loss</th>\n",
              "      <th>hours-per-week</th>\n",
              "      <th>native-country</th>\n",
              "      <th>salary</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>32556</th>\n",
              "      <td>27</td>\n",
              "      <td>Private</td>\n",
              "      <td>257302</td>\n",
              "      <td>Assoc-acdm</td>\n",
              "      <td>12</td>\n",
              "      <td>Married-civ-spouse</td>\n",
              "      <td>Tech-support</td>\n",
              "      <td>Wife</td>\n",
              "      <td>White</td>\n",
              "      <td>Female</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>38</td>\n",
              "      <td>United-States</td>\n",
              "      <td>&lt;=50K</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>32557</th>\n",
              "      <td>40</td>\n",
              "      <td>Private</td>\n",
              "      <td>154374</td>\n",
              "      <td>HS-grad</td>\n",
              "      <td>9</td>\n",
              "      <td>Married-civ-spouse</td>\n",
              "      <td>Machine-op-inspct</td>\n",
              "      <td>Husband</td>\n",
              "      <td>White</td>\n",
              "      <td>Male</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>40</td>\n",
              "      <td>United-States</td>\n",
              "      <td>&gt;50K</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>32558</th>\n",
              "      <td>58</td>\n",
              "      <td>Private</td>\n",
              "      <td>151910</td>\n",
              "      <td>HS-grad</td>\n",
              "      <td>9</td>\n",
              "      <td>Widowed</td>\n",
              "      <td>Adm-clerical</td>\n",
              "      <td>Unmarried</td>\n",
              "      <td>White</td>\n",
              "      <td>Female</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>40</td>\n",
              "      <td>United-States</td>\n",
              "      <td>&lt;=50K</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>32559</th>\n",
              "      <td>22</td>\n",
              "      <td>Private</td>\n",
              "      <td>201490</td>\n",
              "      <td>HS-grad</td>\n",
              "      <td>9</td>\n",
              "      <td>Never-married</td>\n",
              "      <td>Adm-clerical</td>\n",
              "      <td>Own-child</td>\n",
              "      <td>White</td>\n",
              "      <td>Male</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>20</td>\n",
              "      <td>United-States</td>\n",
              "      <td>&lt;=50K</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>32560</th>\n",
              "      <td>52</td>\n",
              "      <td>Self-emp-inc</td>\n",
              "      <td>287927</td>\n",
              "      <td>HS-grad</td>\n",
              "      <td>9</td>\n",
              "      <td>Married-civ-spouse</td>\n",
              "      <td>Exec-managerial</td>\n",
              "      <td>Wife</td>\n",
              "      <td>White</td>\n",
              "      <td>Female</td>\n",
              "      <td>15024</td>\n",
              "      <td>0</td>\n",
              "      <td>40</td>\n",
              "      <td>United-States</td>\n",
              "      <td>&gt;50K</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a2ff4535-f47b-496d-8c42-dfb8d687efb8')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-a2ff4535-f47b-496d-8c42-dfb8d687efb8 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-a2ff4535-f47b-496d-8c42-dfb8d687efb8');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-4cc842f5-dcb5-47b6-a32e-748d4fc347e8\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-4cc842f5-dcb5-47b6-a32e-748d4fc347e8')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-4cc842f5-dcb5-47b6-a32e-748d4fc347e8 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"data\",\n  \"rows\": 5,\n  \"fields\": [\n    {\n      \"column\": \"age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15,\n        \"min\": 22,\n        \"max\": 58,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          40,\n          52,\n          58\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"workclass\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Self-emp-inc\",\n          \"Private\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"fnlwgt\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 60929,\n        \"min\": 151910,\n        \"max\": 287927,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          154374,\n          287927\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"HS-grad\",\n          \"Assoc-acdm\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education-num\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 9,\n        \"max\": 12,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          9,\n          12\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"marital-status\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"Married-civ-spouse\",\n          \"Widowed\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"occupation\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"Machine-op-inspct\",\n          \"Exec-managerial\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"relationship\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"Husband\",\n          \"Own-child\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"race\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 1,\n        \"samples\": [\n          \"White\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"sex\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capital-gain\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6718,\n        \"min\": 0,\n        \"max\": 15024,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          15024\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capital-loss\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 0,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hours-per-week\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 8,\n        \"min\": 20,\n        \"max\": 40,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          38\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"native-country\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 1,\n        \"samples\": [\n          \"United-States\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"salary\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \">50K\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "race_count = data.race.value_counts()\n",
        "print(race_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1xn3-Sno4HXe",
        "outputId": "56861e4d-7cd2-4686-e007-baa2537b606d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "race\n",
            "White                 27816\n",
            "Black                  3124\n",
            "Asian-Pac-Islander     1039\n",
            "Amer-Indian-Eskimo      311\n",
            "Other                   271\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "average_age_men = round(data[data.sex == 'Male'].age.mean(),2)\n",
        "\n",
        "print(\"Average age of men:\", average_age_men)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ENxT-4ZZ4aJK",
        "outputId": "135d64f5-18c7-4bfe-f680-1a81b657141c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Average age of men: 39.43\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "percentage_bachelors = round((data.education.value_counts(normalize=True).Bachelors)*100,2)\n",
        "\n",
        "print(f\"Percentage with Bachelors degrees: {percentage_bachelors}%\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ia2uOatq4zIE",
        "outputId": "258cadc6-2aac-497e-b006-3be871aa151d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Percentage with Bachelors degrees: 16.45%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "higher_education = ( (data['education'] == 'Doctorate')\n",
        "                    | (data['education'] == 'Bachelors')\n",
        "                    | (data['education'] == 'Masters'))\n",
        "\n",
        "# I used this mask and then I did value_counts(with normalize)\n",
        "# Next I chose only row with index '>50K' and rounded its value\n",
        "higher_education_rich = round((\n",
        "            data[higher_education].salary.value_counts(normalize=True)['>50K']\n",
        "                )*100 ,2)\n",
        "\n",
        "print(f\"Percentage of people with higher education that earn >50K: {higher_education_rich}%\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6cCXowh94-XG",
        "outputId": "dc7e5f67-78f2-4f7c-d1f5-08bd559ec381"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Percentage of people with higher education that earn >50K: 46.54%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lower_education = ~higher_education\n",
        "\n",
        "# The same as for higher education\n",
        "lower_education_rich = round((\n",
        "            data[lower_education].salary.value_counts(normalize=True)['>50K']\n",
        "                )*100 ,2)\n",
        "\n",
        "print(f\"Percentage without higher education that earn >50K: {lower_education_rich}%\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e77IpKKh4_14",
        "outputId": "6bd8a804-03c4-4766-e924-2cc546bddeda"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Percentage without higher education that earn >50K: 17.37%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "min_work_hours = data['hours-per-week'].min()\n",
        "\n",
        "print(f\"Min work time: {min_work_hours} hours/week\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jx8W1Lwb5GaI",
        "outputId": "0e4a2d06-97c6-46a1-e082-cd184d77503f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Min work time: 1 hours/week\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num_min_workers = data[data['hours-per-week'] == min_work_hours]\n",
        "\n",
        "rich_percentage = round((num_min_workers.salary.value_counts(normalize=True)['>50K'])*100,2)\n",
        "\n",
        "print(f\"Percentage of rich among those who work fewest hours: {rich_percentage}%\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mZYoKD5K5TKz",
        "outputId": "84305181-f791-4834-a84f-75f93d5aac9b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Percentage of rich among those who work fewest hours: 10.0%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "highest_earning_country = (data\n",
        "    .groupby('native-country')['salary']\n",
        "    .value_counts(normalize=True)[:,'>50K']\n",
        "    .sort_values(ascending=False)\n",
        "    .index[0])\n",
        "\n",
        "print(\"Country with highest percentage of rich:\", highest_earning_country)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wweOJ4Pd5env",
        "outputId": "704b2819-ba5d-4bc7-ac3e-6b461695c064"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Country with highest percentage of rich: Iran\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "highest_earning_country_percentage = (round((data\n",
        "    .groupby('native-country')['salary']\n",
        "    .value_counts(normalize=True)[:,'>50K']\n",
        "    .sort_values(ascending=False)[0])*100,2))\n",
        "\n",
        "print(f\"Highest percentage of rich people in country: {highest_earning_country_percentage}%\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n_kJdnCP5z95",
        "outputId": "4e245073-f32f-4c6a-cb2f-1fe50d3bed1c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Highest percentage of rich people in country: 41.86%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mask = (data['salary'] == '>50K') & (data['native-country'] == 'India')\n",
        "\n",
        "top_IN_occupation = (data[mask]['occupation']\n",
        "    .value_counts()[:1]\n",
        "    .index[0])\n",
        "\n",
        "print(\"Most popular occupation for those who earn >50K in India:\", top_IN_occupation)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GdhT-44S51z3",
        "outputId": "d8cca21e-dbc3-4520-a4f6-8c55cfe55512"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Most popular occupation for those who earn >50K in India: Prof-specialty\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN02bdiqRnt0V4tKASe48pB",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}