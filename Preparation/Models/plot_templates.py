import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set global style for publication-quality plots
plt.rcParams['font.family'] = 'sans-serif' # Use 'SimHei' if you need Chinese characters
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
sns.set_theme(style="whitegrid", context="notebook", font_scale=1.2)

def set_chinese_font():
    """Call this if you need to display Chinese characters in plots."""
    plt.rcParams['font.sans-serif'] = ['SimHei'] # Commonly used Chinese font
    plt.rcParams['axes.unicode_minus'] = False

def plot_line(x, y, title="Line Plot", xlabel="X-axis", ylabel="Y-axis", save_path=None):
    """
    Draws a line plot with markers.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x, y=y, marker='o', linewidth=2.5)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
        print(f"Plot saved to {save_path}")
    plt.show()

def plot_multi_line(df, x_col, y_cols, title="Multi-Line Plot", xlabel="X-axis", ylabel="Y-axis", save_path=None):
    """
    Draws multiple lines from a DataFrame.
    """
    plt.figure(figsize=(10, 6))
    for col in y_cols:
        sns.lineplot(data=df, x=x_col, y=col, label=col, marker='o')
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.legend()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

def plot_scatter(x, y, hue=None, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis", save_path=None):
    """
    Draws a scatter plot, optionally colored by a categorical variable (hue).
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, hue=hue, s=100, alpha=0.8, edgecolor='k')
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

def plot_heatmap(corr_matrix, title="Correlation Heatmap", cmap="coolwarm", save_path=None):
    """
    Draws a heatmap for a correlation matrix.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap=cmap, square=True, linewidths=.5, cbar_kws={"shrink": .8})
    plt.title(title, fontsize=16, fontweight='bold')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

def plot_bar(x, y, title="Bar Chart", xlabel="Category", ylabel="Value", save_path=None):
    """
    Draws a bar chart.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, palette="viridis", edgecolor='black')
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

def plot_3d_surface(x, y, z, title="3D Surface Plot", xlabel="X", ylabel="Y", zlabel="Z", save_path=None):
    """
    Draws a 3D surface plot.
    x, y, z must be 2D arrays (meshgrid format).
    """
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_zlabel(zlabel, fontsize=12)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

if __name__ == "__main__":
    # Test cases
    print("Generating demo plots...")
    
    # 1. Line Plot
    x = np.linspace(0, 10, 20)
    y = np.sin(x)
    plot_line(x, y, title="Sine Wave Demo")

    # 2. Heatmap
    data = pd.DataFrame(np.random.rand(10, 10), columns=[f'Var{i}' for i in range(10)])
    corr = data.corr()
    plot_heatmap(corr, title="Random Correlation Matrix")

    # 3. 3D Plot
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    plot_3d_surface(X, Y, Z, title="3D Wave Demo")
    
    print("Done. Check the plots window.")
