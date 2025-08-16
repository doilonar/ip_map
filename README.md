# IP Map


IP Map is a Python utility that visualizes the geographic location of IP addresses on an interactive map. It uses the GeoLite2-City database to look up IP coordinates and `nmap` to optionally scan for open ports.

## Features
-   Generates an interactive HTML map of IP locations using Folium.
-   Sources IPs either by generating them randomly or by reading from a user-provided text file.
-   Integrates with `nmap` to scan for open ports on target IPs.
-   Optionally filters the map to show only IPs with detected open ports.
-   Automatically reassembles the required GeoLite2-City database from split files (`db0`, `db1`, etc.) on the first run.

## Setup

1.  Clone the repository:
    ```sh
    git clone https://github.com/doilonar/ip_map.git
    cd ip_map
    ```

2.  Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
    *Note: You may also need to have `nmap` installed on your system for the port scanning feature to work.*

## Usage

1.  Run the script from your terminal:
    ```sh
    python main.py
    ```

2.  Follow the interactive prompts in your terminal:
    -   **`read random / read from file(r/f):`**
        -   Enter `r` to generate random IPs.
        -   Enter `f` to read IPs from a file. You will be prompted for the filename. The file should contain one IP address per line.
    -   **`how many?:`**
        -   Enter the total number of IPs you wish to process and plot.
    -   **`show only with open ports(y/n):`**
        -   Enter `y` to scan each IP and only show ones with open ports. The open port numbers will be listed in the map marker's popup.
        -   Enter `n` to plot all IPs without scanning.

3.  After the script completes, it will generate a `test.html` file in the project directory. Open this file in any web browser to view the interactive map.

## Example Output

![IP Map Example](https://github.com/doilonar/ip_map/assets/31927364/15e48657-99d7-44b5-a7a1-f62d0394fb4f)
