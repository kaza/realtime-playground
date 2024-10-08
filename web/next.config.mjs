/** @type {import('next').NextConfig} */
const nextConfig = {
  webpack(config) {
    config.module.rules.push({
      test: /\.svg$/, // Look for .svg files
      use: ["@svgr/webpack"], // Use @svgr/webpack to handle them
    });

    return config; // Always return the modified config
  },
  // Add this section
  server: {
    port: process.env.PORT || 8080,
    host: '0.0.0.0'
  }
};

export default nextConfig;
